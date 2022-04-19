// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// API token with GraphQL access and `write_pipelines, read_pipelines` scopes
func GetApiToken(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "buildkite:apiToken")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "BUILDKITE_API_TOKEN").(string)
}

// The Buildkite organization ID
func GetOrganization(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "buildkite:organization")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "BUILDKITE_ORGANIZATION").(string)
}
