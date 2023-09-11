# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TeamArgs', 'Team']

@pulumi.input_type
class TeamArgs:
    def __init__(__self__, *,
                 access_level: pulumi.Input[str],
                 team_id: pulumi.Input[str],
                 test_suite_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Team resource.
        :param pulumi.Input[str] access_level: The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        :param pulumi.Input[str] team_id: The GraphQL ID of the team.
        :param pulumi.Input[str] test_suite_id: The GraphQL ID of the test suite.
        """
        pulumi.set(__self__, "access_level", access_level)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "test_suite_id", test_suite_id)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Input[str]:
        """
        The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        """
        return pulumi.get(self, "access_level")

    @access_level.setter
    def access_level(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_level", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        The GraphQL ID of the team.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="testSuiteId")
    def test_suite_id(self) -> pulumi.Input[str]:
        """
        The GraphQL ID of the test suite.
        """
        return pulumi.get(self, "test_suite_id")

    @test_suite_id.setter
    def test_suite_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "test_suite_id", value)


@pulumi.input_type
class _TeamState:
    def __init__(__self__, *,
                 access_level: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 test_suite_id: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Team resources.
        :param pulumi.Input[str] access_level: The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        :param pulumi.Input[str] team_id: The GraphQL ID of the team.
        :param pulumi.Input[str] test_suite_id: The GraphQL ID of the test suite.
        :param pulumi.Input[str] uuid: This is the UUID of the test suite team.
        """
        if access_level is not None:
            pulumi.set(__self__, "access_level", access_level)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if test_suite_id is not None:
            pulumi.set(__self__, "test_suite_id", test_suite_id)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[str]]:
        """
        The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        """
        return pulumi.get(self, "access_level")

    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_level", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GraphQL ID of the team.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="testSuiteId")
    def test_suite_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GraphQL ID of the test suite.
        """
        return pulumi.get(self, "test_suite_id")

    @test_suite_id.setter
    def test_suite_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "test_suite_id", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        This is the UUID of the test suite team.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


class Team(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_level: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 test_suite_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Resource: test_suite_team

        This resources allows you to create, manage and import team access to Test Suites.

        Buildkite documentation: https://buildkite.com/docs/test-analytics

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        owners = buildkite.team.Team("owners",
            default_team=False,
            privacy="VISIBLE",
            default_member_role="MAINTAINER")
        viewers = buildkite.team.Team("viewers",
            default_team=False,
            privacy="VISIBLE",
            default_member_role="MAINTAINER")
        rspec_suite = buildkite.test_suite.TestSuite("rspecSuite",
            default_branch="main",
            team_owner_id=owners.id)
        viewers_rspec = buildkite.test_suite.Team("viewersRspec",
            test_suite_id=rspec_suite.id,
            team_id=viewers.id,
            access_level="READ_ONLY")
        ```

        ## Import

        Test suite teams can be imported using the `GraphQL ID` (not UUID), e.g.

        ```sh
         $ pulumi import buildkite:TestSuite/team:Team viewers VGVhbvDf4eRef20tMzIxMGEfYTctNzEF5g00M8f5s6E2YjYtODNlOGNlZgD6HcBi
        ```

         To find the ID to use, you can use the GraphQL query below. Alternatively, you could use this [pre-saved query](https://buildkite.com/user/graphql/console/e8480014-37a8-4150-a011-6d35f33b4dfd), where you will need fo fill in the organization slug and suite search term (SUITE_SEARCH_TERM) for the particular test suite required. graphql query getTeamSuiteIds {

         organization(slug"ORGANIZATION_SLUG") {

         suites(first1, search:"SUITE_SEARCH_TERM") {

         edges {

         node {

         id

         name

         teams(first10){

         edges {

         node {

         id

         accessLevel

         team{

         name

         }

         }

         }

         }

         }

         }

         }

         } }

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        :param pulumi.Input[str] team_id: The GraphQL ID of the team.
        :param pulumi.Input[str] test_suite_id: The GraphQL ID of the test suite.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Resource: test_suite_team

        This resources allows you to create, manage and import team access to Test Suites.

        Buildkite documentation: https://buildkite.com/docs/test-analytics

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        owners = buildkite.team.Team("owners",
            default_team=False,
            privacy="VISIBLE",
            default_member_role="MAINTAINER")
        viewers = buildkite.team.Team("viewers",
            default_team=False,
            privacy="VISIBLE",
            default_member_role="MAINTAINER")
        rspec_suite = buildkite.test_suite.TestSuite("rspecSuite",
            default_branch="main",
            team_owner_id=owners.id)
        viewers_rspec = buildkite.test_suite.Team("viewersRspec",
            test_suite_id=rspec_suite.id,
            team_id=viewers.id,
            access_level="READ_ONLY")
        ```

        ## Import

        Test suite teams can be imported using the `GraphQL ID` (not UUID), e.g.

        ```sh
         $ pulumi import buildkite:TestSuite/team:Team viewers VGVhbvDf4eRef20tMzIxMGEfYTctNzEF5g00M8f5s6E2YjYtODNlOGNlZgD6HcBi
        ```

         To find the ID to use, you can use the GraphQL query below. Alternatively, you could use this [pre-saved query](https://buildkite.com/user/graphql/console/e8480014-37a8-4150-a011-6d35f33b4dfd), where you will need fo fill in the organization slug and suite search term (SUITE_SEARCH_TERM) for the particular test suite required. graphql query getTeamSuiteIds {

         organization(slug"ORGANIZATION_SLUG") {

         suites(first1, search:"SUITE_SEARCH_TERM") {

         edges {

         node {

         id

         name

         teams(first10){

         edges {

         node {

         id

         accessLevel

         team{

         name

         }

         }

         }

         }

         }

         }

         }

         } }

        :param str resource_name: The name of the resource.
        :param TeamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_level: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 test_suite_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamArgs.__new__(TeamArgs)

            if access_level is None and not opts.urn:
                raise TypeError("Missing required property 'access_level'")
            __props__.__dict__["access_level"] = access_level
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            if test_suite_id is None and not opts.urn:
                raise TypeError("Missing required property 'test_suite_id'")
            __props__.__dict__["test_suite_id"] = test_suite_id
            __props__.__dict__["uuid"] = None
        super(Team, __self__).__init__(
            'buildkite:TestSuite/team:Team',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_level: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            test_suite_id: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None) -> 'Team':
        """
        Get an existing Team resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        :param pulumi.Input[str] team_id: The GraphQL ID of the team.
        :param pulumi.Input[str] test_suite_id: The GraphQL ID of the test suite.
        :param pulumi.Input[str] uuid: This is the UUID of the test suite team.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamState.__new__(_TeamState)

        __props__.__dict__["access_level"] = access_level
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["test_suite_id"] = test_suite_id
        __props__.__dict__["uuid"] = uuid
        return Team(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Output[str]:
        """
        The access level the team has on the test suite. Either READ_ONLY or MANAGE_AND_READ.
        """
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The GraphQL ID of the team.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="testSuiteId")
    def test_suite_id(self) -> pulumi.Output[str]:
        """
        The GraphQL ID of the test suite.
        """
        return pulumi.get(self, "test_suite_id")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        This is the UUID of the test suite team.
        """
        return pulumi.get(self, "uuid")
