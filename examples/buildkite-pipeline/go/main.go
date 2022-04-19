package main

import (
	"fmt"
	buildkite "github.com/grapl-security/pulumi-buildkite/sdk/go/buildkite"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		_, err := buildkite.NewPipeline(ctx, "buildkite-pipeline-go", &buildkite.PipelineArgs{
			Name:          pulumi.String("testing-pipeline-go"),
			Repository:    pulumi.String("https://github.com/grapl-security/pulumi-buildkite"),
			Description:   pulumi.String(":pulumi::buildkite::go: A pipeline created to test the pulumi-buildkite provider"),
			DefaultBranch: pulumi.String("main"),
			Steps: pulumi.String(`
        steps:
          - label: "Hello World"
            command: echo 'Hello World'
`),
		})
		if err != nil {
			return fmt.Errorf("error creating pipeline: %v", err)
		}

		return nil
	})
}
