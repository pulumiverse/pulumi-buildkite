module github.com/grapl-security/pulumi-buildkite/sdk

go 1.16

require (
	github.com/blang/semver v3.5.1+incompatible
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi/sdk/v3 v3.40.1
)

require github.com/mattn/go-isatty v0.0.14 // indirect

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220725190814-23001ad6ec03
