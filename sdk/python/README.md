# Buildkite Resource Provider

[![](https://img.shields.io/github/license/pulumiverse/pulumi-buildkite?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/actions/workflow/status/pulumiverse/pulumi-buildkite/verify.yml?style=for-the-badge)](https://github.com/pulumiverse/pulumi-buildkite/actions/workflows/verify.yml)
[![](https://img.shields.io/github/release-date/pulumiverse/pulumi-buildkite?style=for-the-badge)](https://github.com/pulumiverse/pulumi-buildkite/releases)
[![](https://img.shields.io/pypi/v/pulumiverse-buildkite?style=for-the-badge)](https://pypi.org/project/pulumiverse-buildkite/)
[![](https://img.shields.io/pypi/dm/pulumiverse-buildkite?style=for-the-badge)](https://pypi.org/project/pulumiverse-buildkite/)
[![](https://img.shields.io/nuget/v/Pulumiverse.Buildkite?style=for-the-badge)](https://www.nuget.org/packages/Pulumiverse.Buildkite/)
[![](https://img.shields.io/nuget/dt/Pulumiverse.Buildkite?style=for-the-badge)](https://www.nuget.org/packages/Pulumiverse.Buildkite/)
[![](https://img.shields.io/npm/v/@pulumiverse/buildkite?style=for-the-badge)](https://www.npmjs.com/package/@pulumiverse/buildkite)
[![](https://img.shields.io/npm/dm/@pulumiverse/buildkite?style=for-the-badge)](https://www.npmjs.com/package/@pulumiverse/buildkite)
[![](https://img.shields.io/github/all-contributors/pulumiverse/pulumi-buildkite?color=ee8449&style=for-the-badge)](#contributors)

The Buildkite Resource Provider lets you manage [Buildkite](http://buildkite.com) resources.

The provider is built on https://github.com/buildkite/terraform-provider-buildkite.

## Installing

> [!IMPORTANT]
> The provider version `v2.3.1` was built on the Terraform provider `v0.25.1` which was a pre-release version.
> From `v3.0.0` onwards this provider is compatible with the Terraform provider `v1.x.x`.
> Please note that backwards compatibility might not be given.

This package is available in many languages in the standard packaging formats.

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumiverse/buildkite
```

or `yarn`:

```bash
yarn add @pulumiverse/buildkite
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumiverse-buildkite
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/pulumiverse/pulumi-buildkite/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumiverse.Buildkite
```

## Configuration

The following configuration points are available for the `buildkite` provider:

- `buildkite:api_token` (required, environment: `BUILDKITE_API_TOKEN`) - A Buildkite API Access Token. Must have GraphQL access, as well as the `write_pipelines` and `read_pipelines` scopes.
- `buildkite:organization` (required, environment: `BUILDKITE_ORGANIZATION`) - The Buildkite organization slug.
- `buildkite:graphql_url` (optional, environment: `BUILDKITE_GRAPHQL_URL`) - The Buildkite GraphQL URL.
- `buildkite:rest_url` (optional, environment: `BUILDKITE_REST_URL`) - The Buildkite REST URL.

## Example

Example for *Typescript* to create a resource:

```typescript
import * as buildkite from '@pulumiverse/buildkite';

const args = {};
const vm = new buildkite.agent.AgentToken(
  'token',
  args,
);
```

## Reference

For detailed reference documentation, please visit the upstream Terraform provider's documentation at: https://registry.terraform.io/providers/buildkite/buildkite/latest

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/muhlba91"><img src="https://avatars.githubusercontent.com/u/653739?v=4?s=100" width="100px;" alt="Daniel Mühlbachler-Pietrzykowski"/><br /><sub><b>Daniel Mühlbachler-Pietrzykowski</b></sub></a><br /><a href="#maintenance-muhlba91" title="Maintenance">🚧</a> <a href="https://github.com/pulumiverse/pulumi-buildkite/commits?author=muhlba91" title="Code">💻</a> <a href="https://github.com/pulumiverse/pulumi-buildkite/commits?author=muhlba91" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/christophermaier"><img src="https://avatars.githubusercontent.com/u/207178?v=4?s=100" width="100px;" alt="Christopher Maier"/><br /><sub><b>Christopher Maier</b></sub></a><br /><a href="https://github.com/pulumiverse/pulumi-buildkite/commits?author=christophermaier" title="Code">💻</a> <a href="https://github.com/pulumiverse/pulumi-buildkite/commits?author=christophermaier" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/susanev"><img src="https://avatars.githubusercontent.com/u/5489125?v=4?s=100" width="100px;" alt="Susan Evans"/><br /><sub><b>Susan Evans</b></sub></a><br /><a href="https://github.com/pulumiverse/pulumi-buildkite/commits?author=susanev" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/stack72"><img src="https://avatars.githubusercontent.com/u/227823?v=4?s=100" width="100px;" alt="Paul Stack"/><br /><sub><b>Paul Stack</b></sub></a><br /><a href="https://github.com/pulumiverse/pulumi-buildkite/commits?author=stack72" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
