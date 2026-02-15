package shim

import (
	p "github.com/buildkite/terraform-provider-buildkite/buildkite"
	"github.com/hashicorp/terraform-plugin-framework/provider"

	"github.com/pulumiverse/pulumi-buildkite/provider/pkg/version"
)

func NewProvider() provider.Provider {
	return p.New(version.Version)
}
