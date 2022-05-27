package examples

import (
	"os"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func GetCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

func GetBaseOptions() integration.ProgramTestOptions {
	return integration.ProgramTestOptions{
		Verbose: true,
		// After v0.9.0 of the Terraform Buildkite provider, we have a
		// `tags` list on Pipelines. If you don't set tags at
		// creation, a refresh will trigger a change by adding an
		// empty list. I think there's a way we can modify this in the
		// Pulumi mapping, but for now, we'll just skip any refreshes
		// to avoid a failure. (Even if you add an empty tags list,
		// the refresh will still change!)
		SkipRefresh: true,
	}
}
