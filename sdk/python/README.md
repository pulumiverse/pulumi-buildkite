# Buildkite Resource Provider

The Buildkite Resource Provider lets you manage [Buildkite](https://buildkite.com/) CI/CD resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @grapl/pulumi-buildkite
```

or `yarn`:

```bash
yarn add @grapl/pulumi-buildkite
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_buildkite
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/grapl-security/pulumi-buildkite/sdk/go/...
```

## Configuration

The following configuration points are available for the `buildkite` provider:

- `buildkite:api_token` (environment: `BUILDKITE_API_TOKEN`) - A Buildkite API Access Token. Must have GraphQL access, as well as the `write_pipelines` and `read_pipelines` scopes.
- `buildkite:organization` (environment: `BUILDKITE_ORGANIZATION`) - The Buildkite organization slug.

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/buildkite/api-docs/).
