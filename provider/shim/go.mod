module github.com/buildkite/terraform-provider-buildkite/shim

go 1.16

require (
	github.com/buildkite/terraform-provider-buildkite v0.11.0
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.16.0
)

replace (
	// v0.16.0 removed the experimental tfinstall command
	// https://github.com/hashicorp/terraform-exec/blob/main/CHANGELOG.md#0160-january-31-2022
	github.com/hashicorp/terraform-exec => github.com/hashicorp/terraform-exec v0.15.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220523144019-a9dc436975cc
)
