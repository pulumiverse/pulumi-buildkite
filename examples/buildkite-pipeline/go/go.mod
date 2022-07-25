module buildkite-pipeline-go

go 1.16

replace github.com/grapl-security/pulumi-buildkite/sdk => ../../../sdk

require (
	github.com/grapl-security/pulumi-buildkite/sdk v0.2.1
	github.com/pulumi/pulumi/sdk/v3 v3.36.0
)
