//go:build nodejs || all
// +build nodejs all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getNodeJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := GetBaseOptions()
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@grapl/pulumi-buildkite",
		},
	})

	return baseJS
}

func TestBuildkitePipelineNodeJS(t *testing.T) {
	test := getNodeJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(GetCwd(t), "buildkite-pipeline", "nodejs"),
		})
	integration.ProgramTest(t, &test)
}
