module github.com/grapl-security/pulumi-buildkite/provider

go 1.16

replace (
	github.com/buildkite/terraform-provider-buildkite/shim => ./shim
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	// v0.16.0 removed the experimental tfinstall command
	// https://github.com/hashicorp/terraform-exec/blob/main/CHANGELOG.md#0160-january-31-2022
	github.com/hashicorp/terraform-exec => github.com/hashicorp/terraform-exec v0.15.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220523144019-a9dc436975cc
)

require (
	github.com/buildkite/terraform-provider-buildkite/shim v0.0.0-00010101000000-000000000000
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.26.0
	github.com/pulumi/pulumi/sdk/v3 v3.36.0
)

require github.com/hashicorp/terraform-plugin-sdk v1.17.2 // indirect
