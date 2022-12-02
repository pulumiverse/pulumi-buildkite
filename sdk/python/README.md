# Buildkite Resource Provider

The Buildkite Resource Provider lets you manage [Buildkite](https://buildkite.com/) CI/CD resources.

**NOTE**: This provider is in the process of being migrated to the
[Pulumiverse](https://github.com/pulumiverse) organization. Make note
of the upcoming package name changes below for your SDK.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @grapl/pulumi-buildkite
```
Or, following the Pulumiverse migration:
```bash
npm install @pulumiverse/buildkite
```

or `yarn`:

```bash
yarn add @grapl/pulumi-buildkite
```

Or, following the Pulumiverse migration:
```bash
yarn add @pulumiverse/buildkite
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_buildkite
```

Or, following the Pulumiverse migration:
```bash
pip install pulumiverse_buildkite
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/grapl-security/pulumi-buildkite/sdk/go/...
```
Or, following the Pulumiverse migration:
```bash
go get github.com/pulumiverse/pulumi-buildkite/sdk/go/...
```

## Configuration

The following configuration points are available for the `buildkite` provider:

- `buildkite:api_token` (environment: `BUILDKITE_API_TOKEN`) - A Buildkite API Access Token. Must have GraphQL access, as well as the `write_pipelines` and `read_pipelines` scopes.
- `buildkite:organization` (environment: `BUILDKITE_ORGANIZATION`) - The Buildkite organization slug.

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/buildkite/api-docs/).
