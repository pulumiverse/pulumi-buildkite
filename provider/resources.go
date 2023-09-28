// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package buildkite

import (
	"context"
	_ "embed"
	"fmt"
	"path/filepath"

	"github.com/buildkite/terraform-provider-buildkite/buildkite"
	pfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumiverse/pulumi-buildkite/provider/pkg/version"
)

const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "buildkite"
	// modules:
	mainMod         = "index" //nolint:deadcode,unused,varcheck
	pipelineMod     = "Pipeline"
	testMod         = "TestSuite"
	teamMod         = "Team"
	organizationMod = "Organization"
	agentMod        = "Agent"
	clusterMod      = "Cluster"
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(_ resource.PropertyMap, _ shim.ResourceConfig) error {
	return nil
}

//go:embed cmd/pulumi-resource-buildkite/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := pfbridge.MuxShimWithPF(context.Background(),
		pfbridge.ShimProvider(buildkite.New(version.Version)),
		buildkite.New(version.Version),
	)

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:                    p,
		Name:                 "buildkite",
		DisplayName:          "Buildkite",
		Description:          "A Pulumi package for creating and managing Buildkite resources.",
		Publisher:            "Pulumiverse",
		Keywords:             []string{"pulumi", "buildkite"},
		License:              "Apache-2.0",
		Homepage:             "https://github.com/pulumiverse/pulumi-buildkite",
		Repository:           "https://github.com/pulumiverse/pulumi-buildkite",
		LogoURL:              "https://raw.githubusercontent.com/pulumiverse/pulumi-buildkite/main/assets/buildkite-logo.png",
		GitHubOrg:            "buildkite",
		PluginDownloadURL:    "github://api.github.com/pulumiverse/pulumi-buildkite",
		MetadataInfo:         tfbridge.NewProviderMetadata(metadata),
		Version:              version.Version,
		Config:               map[string]*tfbridge.SchemaInfo{},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			// Pipeline
			"buildkite_pipeline":          {Tok: tfbridge.MakeResource(mainPkg, pipelineMod, "Pipeline")},
			"buildkite_pipeline_schedule": {Tok: tfbridge.MakeResource(mainPkg, pipelineMod, "Schedule")},
			"buildkite_pipeline_team":     {Tok: tfbridge.MakeResource(mainPkg, pipelineMod, "Team")},
			"buildkite_pipeline_template": {Tok: tfbridge.MakeResource(mainPkg, pipelineMod, "Template")},
			// Team
			"buildkite_team":        {Tok: tfbridge.MakeResource(mainPkg, teamMod, "Team")},
			"buildkite_team_member": {Tok: tfbridge.MakeResource(mainPkg, teamMod, "Member")},
			// Test
			"buildkite_test_suite":      {Tok: tfbridge.MakeResource(mainPkg, testMod, "TestSuite")},
			"buildkite_test_suite_team": {Tok: tfbridge.MakeResource(mainPkg, testMod, "Team")},
			// Organization
			"buildkite_organization":        {Tok: tfbridge.MakeResource(mainPkg, organizationMod, "Organization")},
			"buildkite_organization_banner": {Tok: tfbridge.MakeResource(mainPkg, organizationMod, "Banner")},
			// Agent
			"buildkite_agent_token": {Tok: tfbridge.MakeResource(mainPkg, agentMod, "AgentToken")},
			// Cluster
			"buildkite_cluster":               {Tok: tfbridge.MakeResource(mainPkg, clusterMod, "Cluster")},
			"buildkite_cluster_agent_token":   {Tok: tfbridge.MakeResource(mainPkg, clusterMod, "ClusterAgentToken")},
			"buildkite_cluster_queue":         {Tok: tfbridge.MakeResource(mainPkg, clusterMod, "ClusterQueue")},
			"buildkite_cluster_default_queue": {Tok: tfbridge.MakeResource(mainPkg, clusterMod, "ClusterDefaultQueue")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Pipeline
			"buildkite_pipeline":              {Tok: tfbridge.MakeDataSource(mainPkg, pipelineMod, "getPipeline")},
			"buildkite_pipeline_template":     {Tok: tfbridge.MakeDataSource(mainPkg, pipelineMod, "getTemplate")},
			"buildkite_signed_pipeline_steps": {Tok: tfbridge.MakeDataSource(mainPkg, pipelineMod, "getSignedSteps")},
			// Team
			"buildkite_team": {Tok: tfbridge.MakeDataSource(mainPkg, teamMod, "getTeam")},
			// Organization
			"buildkite_organization": {Tok: tfbridge.MakeDataSource(mainPkg, organizationMod, "getOrganization")},
			// Cluster
			"buildkite_cluster": {Tok: tfbridge.MakeDataSource(mainPkg, clusterMod, "getCluster")},
			// Anything Else
			"buildkite_meta": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getMeta")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@pulumiverse/buildkite",
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "pulumiverse_buildkite",
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumiverse/pulumi-%[1]s/sdk/", mainPkg),
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
			RootNamespace: "Pulumiverse",
			Namespaces: map[string]string{
				mainPkg: "Buildkite",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
