//go:build go || all
// +build go all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getGoBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := GetBaseOptions()
	baseGo := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"github.com/grapl-security/pulumi-buildkite/sdk",
		},
	})

	return baseGo
}

func TestBuildkitePipelineGo(t *testing.T) {
	test := getGoBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(GetCwd(t), "buildkite-pipeline", "go"),
		})

	integration.ProgramTest(t, &test)
}
