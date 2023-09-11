// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organization

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-buildkite/sdk/v2/go/buildkite/internal"
)

// ## # Resource: organization
//
// This resource allows you to manage the settings for an organization.
//
// You must be an organization administrator to manage organization settings.
//
// Note: The "Allowed API IP Addresses" feature must be enabled on your organization in order to manage the `allowedApiIpAddresses` attribute.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-buildkite/sdk/v2/go/buildkite/Organization"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Organization.NewOrganization(ctx, "testSettings", &Organization.OrganizationArgs{
//				AllowedApiIpAddresses: pulumi.StringArray{
//					pulumi.String("1.1.1.1/32"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Organization settings can be imported by passing the organization slug to the import command, along with the identifier of the resource.
//
// ```sh
//
//	$ pulumi import buildkite:Organization/organization:Organization test_settings test_org
//
// ```
//
//	Your organization's slug can be found in your organisation's [settings](https://buildkite.com/organizations/~/settings) page.
type Organization struct {
	pulumi.CustomResourceState

	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses pulumi.StringArrayOutput `pulumi:"allowedApiIpAddresses"`
	Uuid                  pulumi.StringOutput      `pulumi:"uuid"`
}

// NewOrganization registers a new resource with the given unique name, arguments, and options.
func NewOrganization(ctx *pulumi.Context,
	name string, args *OrganizationArgs, opts ...pulumi.ResourceOption) (*Organization, error) {
	if args == nil {
		args = &OrganizationArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Organization
	err := ctx.RegisterResource("buildkite:Organization/organization:Organization", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganization gets an existing Organization resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganization(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationState, opts ...pulumi.ResourceOption) (*Organization, error) {
	var resource Organization
	err := ctx.ReadResource("buildkite:Organization/organization:Organization", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Organization resources.
type organizationState struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses []string `pulumi:"allowedApiIpAddresses"`
	Uuid                  *string  `pulumi:"uuid"`
}

type OrganizationState struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses pulumi.StringArrayInput
	Uuid                  pulumi.StringPtrInput
}

func (OrganizationState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationState)(nil)).Elem()
}

type organizationArgs struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses []string `pulumi:"allowedApiIpAddresses"`
}

// The set of arguments for constructing a Organization resource.
type OrganizationArgs struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses pulumi.StringArrayInput
}

func (OrganizationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationArgs)(nil)).Elem()
}

type OrganizationInput interface {
	pulumi.Input

	ToOrganizationOutput() OrganizationOutput
	ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput
}

func (*Organization) ElementType() reflect.Type {
	return reflect.TypeOf((**Organization)(nil)).Elem()
}

func (i *Organization) ToOrganizationOutput() OrganizationOutput {
	return i.ToOrganizationOutputWithContext(context.Background())
}

func (i *Organization) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationOutput)
}

// OrganizationArrayInput is an input type that accepts OrganizationArray and OrganizationArrayOutput values.
// You can construct a concrete instance of `OrganizationArrayInput` via:
//
//	OrganizationArray{ OrganizationArgs{...} }
type OrganizationArrayInput interface {
	pulumi.Input

	ToOrganizationArrayOutput() OrganizationArrayOutput
	ToOrganizationArrayOutputWithContext(context.Context) OrganizationArrayOutput
}

type OrganizationArray []OrganizationInput

func (OrganizationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Organization)(nil)).Elem()
}

func (i OrganizationArray) ToOrganizationArrayOutput() OrganizationArrayOutput {
	return i.ToOrganizationArrayOutputWithContext(context.Background())
}

func (i OrganizationArray) ToOrganizationArrayOutputWithContext(ctx context.Context) OrganizationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationArrayOutput)
}

// OrganizationMapInput is an input type that accepts OrganizationMap and OrganizationMapOutput values.
// You can construct a concrete instance of `OrganizationMapInput` via:
//
//	OrganizationMap{ "key": OrganizationArgs{...} }
type OrganizationMapInput interface {
	pulumi.Input

	ToOrganizationMapOutput() OrganizationMapOutput
	ToOrganizationMapOutputWithContext(context.Context) OrganizationMapOutput
}

type OrganizationMap map[string]OrganizationInput

func (OrganizationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Organization)(nil)).Elem()
}

func (i OrganizationMap) ToOrganizationMapOutput() OrganizationMapOutput {
	return i.ToOrganizationMapOutputWithContext(context.Background())
}

func (i OrganizationMap) ToOrganizationMapOutputWithContext(ctx context.Context) OrganizationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationMapOutput)
}

type OrganizationOutput struct{ *pulumi.OutputState }

func (OrganizationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Organization)(nil)).Elem()
}

func (o OrganizationOutput) ToOrganizationOutput() OrganizationOutput {
	return o
}

func (o OrganizationOutput) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return o
}

// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
func (o OrganizationOutput) AllowedApiIpAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringArrayOutput { return v.AllowedApiIpAddresses }).(pulumi.StringArrayOutput)
}

func (o OrganizationOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

type OrganizationArrayOutput struct{ *pulumi.OutputState }

func (OrganizationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Organization)(nil)).Elem()
}

func (o OrganizationArrayOutput) ToOrganizationArrayOutput() OrganizationArrayOutput {
	return o
}

func (o OrganizationArrayOutput) ToOrganizationArrayOutputWithContext(ctx context.Context) OrganizationArrayOutput {
	return o
}

func (o OrganizationArrayOutput) Index(i pulumi.IntInput) OrganizationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Organization {
		return vs[0].([]*Organization)[vs[1].(int)]
	}).(OrganizationOutput)
}

type OrganizationMapOutput struct{ *pulumi.OutputState }

func (OrganizationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Organization)(nil)).Elem()
}

func (o OrganizationMapOutput) ToOrganizationMapOutput() OrganizationMapOutput {
	return o
}

func (o OrganizationMapOutput) ToOrganizationMapOutputWithContext(ctx context.Context) OrganizationMapOutput {
	return o
}

func (o OrganizationMapOutput) MapIndex(k pulumi.StringInput) OrganizationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Organization {
		return vs[0].(map[string]*Organization)[vs[1].(string)]
	}).(OrganizationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationInput)(nil)).Elem(), &Organization{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationArrayInput)(nil)).Elem(), OrganizationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationMapInput)(nil)).Elem(), OrganizationMap{})
	pulumi.RegisterOutputType(OrganizationOutput{})
	pulumi.RegisterOutputType(OrganizationArrayOutput{})
	pulumi.RegisterOutputType(OrganizationMapOutput{})
}