const AUTH_REALM = 'Curso SAPE/SC';
const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder('utf-8', { fatal: true });

function constantTimeEqual(received, expected) {
  const receivedBytes = textEncoder.encode(received);
  const expectedBytes = textEncoder.encode(expected);
  const maximumLength = Math.max(receivedBytes.length, expectedBytes.length);
  let difference = receivedBytes.length ^ expectedBytes.length;

  for (let index = 0; index < maximumLength; index += 1) {
    difference |= (receivedBytes[index] ?? 0) ^ (expectedBytes[index] ?? 0);
  }

  return difference === 0;
}

function readBasicCredentials(authorizationHeader) {
  if (!authorizationHeader) {
    return null;
  }

  const match = authorizationHeader.match(/^Basic\s+(.+)$/i);
  if (!match) {
    return null;
  }

  try {
    const decodedBytes = Uint8Array.from(atob(match[1]), (character) =>
      character.charCodeAt(0),
    );
    const decodedCredentials = textDecoder.decode(decodedBytes);
    const separatorIndex = decodedCredentials.indexOf(':');

    if (separatorIndex < 0) {
      return null;
    }

    return {
      username: decodedCredentials.slice(0, separatorIndex),
      password: decodedCredentials.slice(separatorIndex + 1),
    };
  } catch {
    return null;
  }
}

function unauthorizedResponse() {
  return new Response('Usuário ou senha incorretos.', {
    status: 401,
    headers: {
      'Cache-Control': 'no-store',
      'Content-Type': 'text/plain; charset=UTF-8',
      'WWW-Authenticate': `Basic realm="${AUTH_REALM}", charset="UTF-8"`,
    },
  });
}

function configurationErrorResponse() {
  return new Response('Autenticação indisponível. Verifique a configuração do site.', {
    status: 503,
    headers: {
      'Cache-Control': 'no-store',
      'Content-Type': 'text/plain; charset=UTF-8',
    },
  });
}

export async function onRequest(context) {
  const expectedUsername = context.env.COURSE_USERNAME;
  const expectedPassword = context.env.COURSE_PASSWORD;

  if (!expectedUsername || !expectedPassword) {
    return configurationErrorResponse();
  }

  const credentials = readBasicCredentials(
    context.request.headers.get('Authorization'),
  );

  const usernameIsValid = constantTimeEqual(
    credentials?.username ?? '',
    expectedUsername,
  );
  const passwordIsValid = constantTimeEqual(
    credentials?.password ?? '',
    expectedPassword,
  );

  if (!credentials || !usernameIsValid || !passwordIsValid) {
    return unauthorizedResponse();
  }

  const response = await context.next();
  const headers = new Headers(response.headers);
  headers.set('Cache-Control', 'private, no-store');
  headers.set('Vary', 'Authorization');

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}
