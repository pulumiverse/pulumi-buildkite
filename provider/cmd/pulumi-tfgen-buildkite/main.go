package main

import (
	buildkite "github.com/grapl-security/pulumi-buildkite/provider"
	"github.com/grapl-security/pulumi-buildkite/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen"
)

func main() {
	// Modify the path to point to the new provider
	tfgen.Main("buildkite", version.Version, buildkite.Provider())
}
