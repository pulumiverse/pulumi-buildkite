module github.com/buildkite/terraform-provider-buildkite/shim

go 1.16

require (
	github.com/buildkite/terraform-provider-buildkite v0.8.0
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.10.1
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20211230170131-3a7c83bfab87
