module github.com/buildkite/terraform-provider-buildkite/shim

go 1.16

require (
	github.com/buildkite/terraform-provider-buildkite v0.11.0
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.16.0
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220505215311-795430389fa7
