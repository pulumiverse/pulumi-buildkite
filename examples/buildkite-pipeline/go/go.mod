module buildkite-pipeline-go

go 1.16

replace github.com/grapl-security/pulumi-buildkite/sdk => ../../../sdk

require (
	github.com/grapl-security/pulumi-buildkite/sdk v0.1.0
	github.com/pulumi/pulumi/sdk/v3 v3.33.1
)
