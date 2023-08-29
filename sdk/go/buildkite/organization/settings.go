// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organization

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-buildkite/sdk/v2/go/buildkite/internal"
)

// ## # Resource: organizationSettings
//
// **Note**: This resource has been deprecated. In a future minor release, we will remove this resource in favour of the newer `Organization.Organization` resource that aligns with the datasource of the same name.
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
//			_, err := Organization.NewSettings(ctx, "testSettings", &Organization.SettingsArgs{
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
//	$ pulumi import buildkite:Organization/settings:Settings test_settings test_org
//
// ```
//
//	Your organization's slug can be found in your organisation's [settings](https://buildkite.com/organizations/~/settings) page.
type Settings struct {
	pulumi.CustomResourceState

	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses pulumi.StringArrayOutput `pulumi:"allowedApiIpAddresses"`
	Uuid                  pulumi.StringOutput      `pulumi:"uuid"`
}

// NewSettings registers a new resource with the given unique name, arguments, and options.
func NewSettings(ctx *pulumi.Context,
	name string, args *SettingsArgs, opts ...pulumi.ResourceOption) (*Settings, error) {
	if args == nil {
		args = &SettingsArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Settings
	err := ctx.RegisterResource("buildkite:Organization/settings:Settings", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSettings gets an existing Settings resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSettings(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SettingsState, opts ...pulumi.ResourceOption) (*Settings, error) {
	var resource Settings
	err := ctx.ReadResource("buildkite:Organization/settings:Settings", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Settings resources.
type settingsState struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses []string `pulumi:"allowedApiIpAddresses"`
	Uuid                  *string  `pulumi:"uuid"`
}

type SettingsState struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses pulumi.StringArrayInput
	Uuid                  pulumi.StringPtrInput
}

func (SettingsState) ElementType() reflect.Type {
	return reflect.TypeOf((*settingsState)(nil)).Elem()
}

type settingsArgs struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses []string `pulumi:"allowedApiIpAddresses"`
}

// The set of arguments for constructing a Settings resource.
type SettingsArgs struct {
	// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
	AllowedApiIpAddresses pulumi.StringArrayInput
}

func (SettingsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*settingsArgs)(nil)).Elem()
}

type SettingsInput interface {
	pulumi.Input

	ToSettingsOutput() SettingsOutput
	ToSettingsOutputWithContext(ctx context.Context) SettingsOutput
}

func (*Settings) ElementType() reflect.Type {
	return reflect.TypeOf((**Settings)(nil)).Elem()
}

func (i *Settings) ToSettingsOutput() SettingsOutput {
	return i.ToSettingsOutputWithContext(context.Background())
}

func (i *Settings) ToSettingsOutputWithContext(ctx context.Context) SettingsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingsOutput)
}

// SettingsArrayInput is an input type that accepts SettingsArray and SettingsArrayOutput values.
// You can construct a concrete instance of `SettingsArrayInput` via:
//
//	SettingsArray{ SettingsArgs{...} }
type SettingsArrayInput interface {
	pulumi.Input

	ToSettingsArrayOutput() SettingsArrayOutput
	ToSettingsArrayOutputWithContext(context.Context) SettingsArrayOutput
}

type SettingsArray []SettingsInput

func (SettingsArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Settings)(nil)).Elem()
}

func (i SettingsArray) ToSettingsArrayOutput() SettingsArrayOutput {
	return i.ToSettingsArrayOutputWithContext(context.Background())
}

func (i SettingsArray) ToSettingsArrayOutputWithContext(ctx context.Context) SettingsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingsArrayOutput)
}

// SettingsMapInput is an input type that accepts SettingsMap and SettingsMapOutput values.
// You can construct a concrete instance of `SettingsMapInput` via:
//
//	SettingsMap{ "key": SettingsArgs{...} }
type SettingsMapInput interface {
	pulumi.Input

	ToSettingsMapOutput() SettingsMapOutput
	ToSettingsMapOutputWithContext(context.Context) SettingsMapOutput
}

type SettingsMap map[string]SettingsInput

func (SettingsMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Settings)(nil)).Elem()
}

func (i SettingsMap) ToSettingsMapOutput() SettingsMapOutput {
	return i.ToSettingsMapOutputWithContext(context.Background())
}

func (i SettingsMap) ToSettingsMapOutputWithContext(ctx context.Context) SettingsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingsMapOutput)
}

type SettingsOutput struct{ *pulumi.OutputState }

func (SettingsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Settings)(nil)).Elem()
}

func (o SettingsOutput) ToSettingsOutput() SettingsOutput {
	return o
}

func (o SettingsOutput) ToSettingsOutputWithContext(ctx context.Context) SettingsOutput {
	return o
}

// A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
func (o SettingsOutput) AllowedApiIpAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Settings) pulumi.StringArrayOutput { return v.AllowedApiIpAddresses }).(pulumi.StringArrayOutput)
}

func (o SettingsOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *Settings) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

type SettingsArrayOutput struct{ *pulumi.OutputState }

func (SettingsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Settings)(nil)).Elem()
}

func (o SettingsArrayOutput) ToSettingsArrayOutput() SettingsArrayOutput {
	return o
}

func (o SettingsArrayOutput) ToSettingsArrayOutputWithContext(ctx context.Context) SettingsArrayOutput {
	return o
}

func (o SettingsArrayOutput) Index(i pulumi.IntInput) SettingsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Settings {
		return vs[0].([]*Settings)[vs[1].(int)]
	}).(SettingsOutput)
}

type SettingsMapOutput struct{ *pulumi.OutputState }

func (SettingsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Settings)(nil)).Elem()
}

func (o SettingsMapOutput) ToSettingsMapOutput() SettingsMapOutput {
	return o
}

func (o SettingsMapOutput) ToSettingsMapOutputWithContext(ctx context.Context) SettingsMapOutput {
	return o
}

func (o SettingsMapOutput) MapIndex(k pulumi.StringInput) SettingsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Settings {
		return vs[0].(map[string]*Settings)[vs[1].(string)]
	}).(SettingsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SettingsInput)(nil)).Elem(), &Settings{})
	pulumi.RegisterInputType(reflect.TypeOf((*SettingsArrayInput)(nil)).Elem(), SettingsArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SettingsMapInput)(nil)).Elem(), SettingsMap{})
	pulumi.RegisterOutputType(SettingsOutput{})
	pulumi.RegisterOutputType(SettingsArrayOutput{})
	pulumi.RegisterOutputType(SettingsMapOutput{})
}
