package shim

import (
	"github.com/buildkite/terraform-provider-buildkite/buildkite"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

func NewProvider() *schema.Provider {
	return buildkite.Provider()
}
