module buildkite-pipeline-go

go 1.16

replace github.com/grapl-security/pulumi-buildkite/sdk => ../../../sdk

require (
	github.com/grapl-security/pulumi-buildkite/sdk v0.0.0-00010101000000-000000000000
	github.com/pulumi/pulumi/sdk/v3 v3.30.0
)
