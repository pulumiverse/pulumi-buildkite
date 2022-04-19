//go:generate go run ./generate.go

package main

import (
	buildkite "github.com/grapl-security/pulumi-buildkite/provider"
	"github.com/grapl-security/pulumi-buildkite/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
)

func main() {
	// Modify the path to point to the new provider
	tfbridge.Main("buildkite", version.Version, buildkite.Provider(), pulumiSchema)
}
