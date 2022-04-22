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
	}
}
