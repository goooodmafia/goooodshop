export default function(context) {
  let httpEndpoint = process.env.APOLLO_SERVER_HTTP || 'http://localhost:8000/graphql';
  // let wsEndpoint = process.env.APOLLO_SERVER_WS || 'ws://localhost:8000/graphql';

  if (process.client) {
    httpEndpoint = process.env.APOLLO_CLIENT_HTTP || 'http://localhost/graphql';
    // wsEndpoint = process.env.APOLLO_CLIENT_WS || 'ws://localhost:4000/graphql';
  }

  return {
    httpEndpoint,
    httpLinkOptions: {
      credentials: 'same-origin',
    },
    // wsEndpoint,
  };
}
