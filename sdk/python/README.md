# Buildkite Resource Provider

[![](https://img.shields.io/github/license/pulumiverse/pulumi-buildkite?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/actions/workflow/status/pulumiverse/pulumi-buildkite/verify-release.yml?style=for-the-badge)](https://github.com/pulumiverse/pulumi-buildkite/actions/workflows/verify-release.yml)
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

## Migrating from v2 to v3

`v3.0.0` is a major upgrade that moves from the pre-release Terraform provider `v0.25.x`
(used by `v2.3.1` and earlier) to the stable Terraform provider `v1.x`. This changes the
schema of the `buildkite:Pipeline/pipeline:Pipeline` resource, so upgrading an existing
stack requires a **one-time manual edit of the stack state**. There is currently no
automatic state mapper — see [issue #118](https://github.com/pulumiverse/pulumi-buildkite/issues/118).

### Symptom

After bumping the provider package to `v3.x`, the first `pulumi preview`/`pulumi up` fails
while trying to read the previously saved state:

```
error: Unable to Read Previously Saved State for UpgradeResourceState: There was an error reading the saved resource state using the prior resource schema defined for version 0 upgrade.

Please report this to the provider developer:

AttributeName("provider_settings"): invalid JSON, expected "[", got "{"
```

### Cause

The underlying Terraform provider changed the shape of `provider_settings` on the pipeline
resource. In v2 (Terraform provider `v0.25.x`) it was modelled as an **array**
(`[]*providerSettingsModel`); in v3 (Terraform provider `v1.x`) it is a **single object**
(`*providerSettingsModel`). State written by v2 therefore cannot be read by v3 without
adjustment. See also [buildkite/terraform-provider-buildkite#501](https://github.com/buildkite/terraform-provider-buildkite/issues/501).

### Migration steps

> [!IMPORTANT]
> The version numbers and URNs shown below are **placeholders**. Substitute your actual
> source version and the v3 version you are upgrading to (the latest release is recommended).
> Back up the exported state file before editing so you can roll back if needed.

1. Upgrade the provider package for your language to `v3.x` (see [Installing](#installing) above).

2. Export the stack state to a file:

   ```bash
   pulumi stack export -s <stackName> > stateFile.json
   ```

3. Edit `stateFile.json`:

   **a. Bump the provider version.** Find the `pulumi:providers:buildkite` resource and update
   the version string from your `2.x.x` version to the `3.x.x` version you are upgrading to.
   The version appears in three places for this resource: the `urn`, `inputs.version`, and
   `outputs.version`. Leave the `id` (GUID) unchanged. This stops Pulumi from trying to load
   the now-uninstalled v2 plugin to read the old state.

   Before:

   ```json
   {
       "urn": "urn:pulumi:<stack>::<project>::pulumi:providers:buildkite::default_2_2_0_...",
       "custom": true,
       "id": "4c1a2d5b-b292-4eec-ac4a-d4d08cd75be6",
       "type": "pulumi:providers:buildkite",
       "inputs": { "pluginDownloadURL": "...", "version": "2.2.0" },
       "outputs": { "pluginDownloadURL": "...", "version": "2.2.0" }
   }
   ```

   After (using the latest release as the target):

   ```json
   {
       "urn": "urn:pulumi:<stack>::<project>::pulumi:providers:buildkite::default_3_4_0_...",
       "custom": true,
       "id": "4c1a2d5b-b292-4eec-ac4a-d4d08cd75be6",
       "type": "pulumi:providers:buildkite",
       "inputs": { "pluginDownloadURL": "...", "version": "3.4.0" },
       "outputs": { "pluginDownloadURL": "...", "version": "3.4.0" }
   }
   ```

   **b. Fix `providerSettings` on every `buildkite:Pipeline/pipeline:Pipeline` resource.**
   Replace the v2 array-style value with the equivalent v3 object.

   For a pipeline with **no** custom provider settings, the v2 state contains the
   default-tracking marker `{"__defaults": []}`; replace it with an empty object:

   ```json
   {
       "urn": "urn:pulumi:<stack>::<project>::buildkite:Pipeline/pipeline:Pipeline::NAME_HERE",
       "type": "buildkite:Pipeline/pipeline:Pipeline",
       "inputs": {
           "providerSettings": {}
       }
   }
   ```

   > [!NOTE]
   > If a pipeline **does** configure provider settings (e.g. GitHub/GitLab options), its
   > `providerSettings` will not be `{"__defaults": []}` — it will hold real keys. In that
   > case keep those keys and only remove the stray `__defaults` entries so the value is a
   > plain object matching the v3 schema, rather than blanking it to `{}`.

4. Re-import the edited state:

   ```bash
   pulumi stack import -s <stackName> --file stateFile.json
   ```

5. Run `pulumi preview` to confirm the state loads cleanly, then `pulumi up` as usual.

> [!NOTE]
> There were additional breaking changes upstream (for example around teams), so you may see
> other diffs when moving to v3. Review your `pulumi preview` output carefully before applying.

## Configuration

The following configuration points are available for the `buildkite` provider:

- `buildkite:apiToken` (required, environment: `BUILDKITE_API_TOKEN`) - A Buildkite API Access Token. Must have GraphQL access, as well as the `write_pipelines`, `read_pipelines` and `write_suites` scopes.
- `buildkite:organization` (required, environment: `BUILDKITE_ORGANIZATION_SLUG`) - The Buildkite organization slug.
- `buildkite:graphqlUrl` (optional, environment: `BUILDKITE_GRAPHQL_URL`) - The Buildkite GraphQL URL.
- `buildkite:restUrl` (optional, environment: `BUILDKITE_REST_URL`) - The Buildkite REST URL.

> [!NOTE]
> The configuration keys are camelCase, e.g. `buildkite:apiToken`, not the snake_case names
> used by the underlying Terraform provider. Pulumi silently ignores unknown configuration
> keys, so setting `buildkite:api_token` results in requests being sent without a token and
> failing with `401 Unauthorized`.

For example, to set the API token as a secret:

```bash
pulumi config set --secret buildkite:apiToken <your-token>
```

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
