package main

import (
	buildkite "github.com/grapl-security/pulumi-buildkite/sdk/go/buildkite"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This minimal program is solely designed to exercise the plugin
// binary installation. We must use *something* from the Buildkite
// SDK, so we'll just try to lookup a non-existent pipeline; we don't care
// about the result, either.
//
// We'll also just be previewing this stack, as that is sufficient to
// trigger the plugin download. Note that we don't even need to
// provide Buildkite credentials for this to work (given this program,
// at least).
func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		buildkite.LookupPipeline(ctx, &buildkite.LookupPipelineArgs{
			Slug: "sluggy-mc-slugface",
		})

		return nil
	})
}
