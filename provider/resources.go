package buildkite

import (
	"fmt"
	"path/filepath"

	// This is code from *this* repository; the upstream provider places
	// its code in an `internal` directory, so we have to jump through
	// some hoops to access it.
	"github.com/buildkite/terraform-provider-buildkite/shim"

	"github.com/grapl-security/pulumi-buildkite/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tfshim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "buildkite"
	// modules:
	mainMod = "index" // the buildkite module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c tfshim.ResourceConfig) error {
	return nil
}

// boolRef returns a reference to the bool argument.
func boolRef(b bool) *bool {
	return &b
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(shim.NewProvider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "buildkite",
		Description: "A Pulumi package for creating and managing Buildkite CI/CD platform resources.",
		// Keywords describing the provider in the Pulumi Registry.
		Keywords: []string{"pulumi", "buildkite", "category/infrastructure"},
		License:  "Apache-2.0",
		Homepage: "https://pulumi.io",
		// The organization of the underlying Terraform provider we're
		// using, because it is not part of the `terraform-providers`
		// organization (this is required for proper documentation
		// extraction).
		GitHubOrg: "buildkite",
		// The logo for this provider that will be shown in the Pulumi
		// Registry.
		LogoURL: "https://raw.githubusercontent.com/grapl-security/pulumi-buildkite/main/assets/buildkite-logo.svg",
		// The repository for *this* code.
		Repository:  "https://github.com/grapl-security/pulumi-buildkite",
		Publisher:   "Grapl Security",
		DisplayName: "Buildkite",
		// Binaries for the plugin will be stored as Github Releases
		// (recommended by Pulumi).
		// NOTE: the added 'v' in front of `${VERSION}` is a temporary
		// workaround for (what I think is) a `pulumi plugin install` issue.
		PluginDownloadURL: "https://github.com/grapl-security/pulumi-buildkite/releases/download/v${VERSION}",
		Config: map[string]*tfbridge.SchemaInfo{
			"api_token": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"BUILDKITE_API_TOKEN"},
				},
				Secret: boolRef(true),
			},
			"organization": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"BUILDKITE_ORGANIZATION"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
		// Each resource from the underlying Terraform provider should
		// be reflected here.
		Resources: map[string]*tfbridge.ResourceInfo{
			"buildkite_agent_token":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AgentToken")},
			"buildkite_pipeline":          {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Pipeline")},
			"buildkite_pipeline_schedule": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "PipelineSchedule")},
			"buildkite_team":              {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Team")},
			"buildkite_team_member":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "TeamMember")},
		},
		// Each data source from the underlying Terraform provider
		// should be reflected here.
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"buildkite_meta": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getMeta")},
			"buildkite_pipeline": {Tok: tfbridge.MakeDataSource(
				mainPkg, mainMod, "getPipeline",
			)},
			"buildkite_team": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getTeam")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			PackageName: "@grapl/pulumi-buildkite",
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/grapl-security/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
