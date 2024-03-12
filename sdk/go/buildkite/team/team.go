// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package team

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-buildkite/sdk/v3/go/buildkite/internal"
)

// A Team is a group of users that can be given permissions for using Pipelines.This feature is only available to Business and Enterprise customers.  You can find out more about Teams in the Buildkite [documentation](https://buildkite.com/docs/team-management/permissions).
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-buildkite/sdk/v3/go/buildkite/Team"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Team.NewTeam(ctx, "everyone", &Team.TeamArgs{
//				DefaultMemberRole: pulumi.String("MEMBER"),
//				DefaultTeam:       pulumi.Bool(false),
//				Privacy:           pulumi.String("VISIBLE"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// import a team resource using the GraphQL ID
//
// #
//
// you can use this query to find the ID:
//
// query getTeamId {
//
//	organization(slug: "ORGANIZATION_SLUG") {
//
//	  teams(first: 1, search: "TEAM_SEARCH_TERM") {
//
//	    edges {
//
//	      node {
//
//	        id
//
//	        name
//
//	      }
//
//	    }
//
//	  }
//
//	}
//
// }
//
// ```sh
// $ pulumi import buildkite:Team/team:Team everyone UGlwZWxpbmUtLS00MzVjYWQ1OC1lODFkLTQ1YWYtODYzNy1iMWNmODA3MDIzOGQ=
// ```
type Team struct {
	pulumi.CustomResourceState

	// The default role for new members of the team. This can be either `MEMBER` or `MAINTAINER`.
	DefaultMemberRole pulumi.StringOutput `pulumi:"defaultMemberRole"`
	// Whether this is the default team for the organization.
	DefaultTeam pulumi.BoolOutput `pulumi:"defaultTeam"`
	// A description for the team. This is displayed in the Buildkite UI.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Whether members of the team can create Pipelines.
	MembersCanCreatePipelines pulumi.BoolOutput `pulumi:"membersCanCreatePipelines"`
	// The name of the team.
	Name pulumi.StringOutput `pulumi:"name"`
	// The privacy setting for the team. This can be either `VISIBLE` or `SECRET`.
	Privacy pulumi.StringOutput `pulumi:"privacy"`
	// The generated slug for the team.
	Slug pulumi.StringOutput `pulumi:"slug"`
	// The UUID of the team.
	Uuid pulumi.StringOutput `pulumi:"uuid"`
}

// NewTeam registers a new resource with the given unique name, arguments, and options.
func NewTeam(ctx *pulumi.Context,
	name string, args *TeamArgs, opts ...pulumi.ResourceOption) (*Team, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DefaultMemberRole == nil {
		return nil, errors.New("invalid value for required argument 'DefaultMemberRole'")
	}
	if args.DefaultTeam == nil {
		return nil, errors.New("invalid value for required argument 'DefaultTeam'")
	}
	if args.Privacy == nil {
		return nil, errors.New("invalid value for required argument 'Privacy'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Team
	err := ctx.RegisterResource("buildkite:Team/team:Team", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTeam gets an existing Team resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeam(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TeamState, opts ...pulumi.ResourceOption) (*Team, error) {
	var resource Team
	err := ctx.ReadResource("buildkite:Team/team:Team", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Team resources.
type teamState struct {
	// The default role for new members of the team. This can be either `MEMBER` or `MAINTAINER`.
	DefaultMemberRole *string `pulumi:"defaultMemberRole"`
	// Whether this is the default team for the organization.
	DefaultTeam *bool `pulumi:"defaultTeam"`
	// A description for the team. This is displayed in the Buildkite UI.
	Description *string `pulumi:"description"`
	// Whether members of the team can create Pipelines.
	MembersCanCreatePipelines *bool `pulumi:"membersCanCreatePipelines"`
	// The name of the team.
	Name *string `pulumi:"name"`
	// The privacy setting for the team. This can be either `VISIBLE` or `SECRET`.
	Privacy *string `pulumi:"privacy"`
	// The generated slug for the team.
	Slug *string `pulumi:"slug"`
	// The UUID of the team.
	Uuid *string `pulumi:"uuid"`
}

type TeamState struct {
	// The default role for new members of the team. This can be either `MEMBER` or `MAINTAINER`.
	DefaultMemberRole pulumi.StringPtrInput
	// Whether this is the default team for the organization.
	DefaultTeam pulumi.BoolPtrInput
	// A description for the team. This is displayed in the Buildkite UI.
	Description pulumi.StringPtrInput
	// Whether members of the team can create Pipelines.
	MembersCanCreatePipelines pulumi.BoolPtrInput
	// The name of the team.
	Name pulumi.StringPtrInput
	// The privacy setting for the team. This can be either `VISIBLE` or `SECRET`.
	Privacy pulumi.StringPtrInput
	// The generated slug for the team.
	Slug pulumi.StringPtrInput
	// The UUID of the team.
	Uuid pulumi.StringPtrInput
}

func (TeamState) ElementType() reflect.Type {
	return reflect.TypeOf((*teamState)(nil)).Elem()
}

type teamArgs struct {
	// The default role for new members of the team. This can be either `MEMBER` or `MAINTAINER`.
	DefaultMemberRole string `pulumi:"defaultMemberRole"`
	// Whether this is the default team for the organization.
	DefaultTeam bool `pulumi:"defaultTeam"`
	// A description for the team. This is displayed in the Buildkite UI.
	Description *string `pulumi:"description"`
	// Whether members of the team can create Pipelines.
	MembersCanCreatePipelines *bool `pulumi:"membersCanCreatePipelines"`
	// The name of the team.
	Name *string `pulumi:"name"`
	// The privacy setting for the team. This can be either `VISIBLE` or `SECRET`.
	Privacy string `pulumi:"privacy"`
}

// The set of arguments for constructing a Team resource.
type TeamArgs struct {
	// The default role for new members of the team. This can be either `MEMBER` or `MAINTAINER`.
	DefaultMemberRole pulumi.StringInput
	// Whether this is the default team for the organization.
	DefaultTeam pulumi.BoolInput
	// A description for the team. This is displayed in the Buildkite UI.
	Description pulumi.StringPtrInput
	// Whether members of the team can create Pipelines.
	MembersCanCreatePipelines pulumi.BoolPtrInput
	// The name of the team.
	Name pulumi.StringPtrInput
	// The privacy setting for the team. This can be either `VISIBLE` or `SECRET`.
	Privacy pulumi.StringInput
}

func (TeamArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*teamArgs)(nil)).Elem()
}

type TeamInput interface {
	pulumi.Input

	ToTeamOutput() TeamOutput
	ToTeamOutputWithContext(ctx context.Context) TeamOutput
}

func (*Team) ElementType() reflect.Type {
	return reflect.TypeOf((**Team)(nil)).Elem()
}

func (i *Team) ToTeamOutput() TeamOutput {
	return i.ToTeamOutputWithContext(context.Background())
}

func (i *Team) ToTeamOutputWithContext(ctx context.Context) TeamOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamOutput)
}

// TeamArrayInput is an input type that accepts TeamArray and TeamArrayOutput values.
// You can construct a concrete instance of `TeamArrayInput` via:
//
//	TeamArray{ TeamArgs{...} }
type TeamArrayInput interface {
	pulumi.Input

	ToTeamArrayOutput() TeamArrayOutput
	ToTeamArrayOutputWithContext(context.Context) TeamArrayOutput
}

type TeamArray []TeamInput

func (TeamArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Team)(nil)).Elem()
}

func (i TeamArray) ToTeamArrayOutput() TeamArrayOutput {
	return i.ToTeamArrayOutputWithContext(context.Background())
}

func (i TeamArray) ToTeamArrayOutputWithContext(ctx context.Context) TeamArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamArrayOutput)
}

// TeamMapInput is an input type that accepts TeamMap and TeamMapOutput values.
// You can construct a concrete instance of `TeamMapInput` via:
//
//	TeamMap{ "key": TeamArgs{...} }
type TeamMapInput interface {
	pulumi.Input

	ToTeamMapOutput() TeamMapOutput
	ToTeamMapOutputWithContext(context.Context) TeamMapOutput
}

type TeamMap map[string]TeamInput

func (TeamMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Team)(nil)).Elem()
}

func (i TeamMap) ToTeamMapOutput() TeamMapOutput {
	return i.ToTeamMapOutputWithContext(context.Background())
}

func (i TeamMap) ToTeamMapOutputWithContext(ctx context.Context) TeamMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamMapOutput)
}

type TeamOutput struct{ *pulumi.OutputState }

func (TeamOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Team)(nil)).Elem()
}

func (o TeamOutput) ToTeamOutput() TeamOutput {
	return o
}

func (o TeamOutput) ToTeamOutputWithContext(ctx context.Context) TeamOutput {
	return o
}

// The default role for new members of the team. This can be either `MEMBER` or `MAINTAINER`.
func (o TeamOutput) DefaultMemberRole() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.DefaultMemberRole }).(pulumi.StringOutput)
}

// Whether this is the default team for the organization.
func (o TeamOutput) DefaultTeam() pulumi.BoolOutput {
	return o.ApplyT(func(v *Team) pulumi.BoolOutput { return v.DefaultTeam }).(pulumi.BoolOutput)
}

// A description for the team. This is displayed in the Buildkite UI.
func (o TeamOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Team) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Whether members of the team can create Pipelines.
func (o TeamOutput) MembersCanCreatePipelines() pulumi.BoolOutput {
	return o.ApplyT(func(v *Team) pulumi.BoolOutput { return v.MembersCanCreatePipelines }).(pulumi.BoolOutput)
}

// The name of the team.
func (o TeamOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The privacy setting for the team. This can be either `VISIBLE` or `SECRET`.
func (o TeamOutput) Privacy() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Privacy }).(pulumi.StringOutput)
}

// The generated slug for the team.
func (o TeamOutput) Slug() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Slug }).(pulumi.StringOutput)
}

// The UUID of the team.
func (o TeamOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *Team) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

type TeamArrayOutput struct{ *pulumi.OutputState }

func (TeamArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Team)(nil)).Elem()
}

func (o TeamArrayOutput) ToTeamArrayOutput() TeamArrayOutput {
	return o
}

func (o TeamArrayOutput) ToTeamArrayOutputWithContext(ctx context.Context) TeamArrayOutput {
	return o
}

func (o TeamArrayOutput) Index(i pulumi.IntInput) TeamOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Team {
		return vs[0].([]*Team)[vs[1].(int)]
	}).(TeamOutput)
}

type TeamMapOutput struct{ *pulumi.OutputState }

func (TeamMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Team)(nil)).Elem()
}

func (o TeamMapOutput) ToTeamMapOutput() TeamMapOutput {
	return o
}

func (o TeamMapOutput) ToTeamMapOutputWithContext(ctx context.Context) TeamMapOutput {
	return o
}

func (o TeamMapOutput) MapIndex(k pulumi.StringInput) TeamOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Team {
		return vs[0].(map[string]*Team)[vs[1].(string)]
	}).(TeamOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TeamInput)(nil)).Elem(), &Team{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamArrayInput)(nil)).Elem(), TeamArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamMapInput)(nil)).Elem(), TeamMap{})
	pulumi.RegisterOutputType(TeamOutput{})
	pulumi.RegisterOutputType(TeamArrayOutput{})
	pulumi.RegisterOutputType(TeamMapOutput{})
}
