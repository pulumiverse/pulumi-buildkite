# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TestSuiteArgs', 'TestSuite']

@pulumi.input_type
class TestSuiteArgs:
    def __init__(__self__, *,
                 default_branch: pulumi.Input[str],
                 team_owner_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TestSuite resource.
        :param pulumi.Input[str] default_branch: The default branch for the repository this test suite is for.
        :param pulumi.Input[str] team_owner_id: The GraphQL ID of the team to mark as the owner/admin of the test suite.
        :param pulumi.Input[str] name: The name to give the test suite.
        """
        pulumi.set(__self__, "default_branch", default_branch)
        pulumi.set(__self__, "team_owner_id", team_owner_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> pulumi.Input[str]:
        """
        The default branch for the repository this test suite is for.
        """
        return pulumi.get(self, "default_branch")

    @default_branch.setter
    def default_branch(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_branch", value)

    @property
    @pulumi.getter(name="teamOwnerId")
    def team_owner_id(self) -> pulumi.Input[str]:
        """
        The GraphQL ID of the team to mark as the owner/admin of the test suite.
        """
        return pulumi.get(self, "team_owner_id")

    @team_owner_id.setter
    def team_owner_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_owner_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name to give the test suite.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TestSuiteState:
    def __init__(__self__, *,
                 api_token: Optional[pulumi.Input[str]] = None,
                 default_branch: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 team_owner_id: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TestSuite resources.
        :param pulumi.Input[str] api_token: The API token to use to send test run data to the API.
        :param pulumi.Input[str] default_branch: The default branch for the repository this test suite is for.
        :param pulumi.Input[str] name: The name to give the test suite.
        :param pulumi.Input[str] slug: The generated slug of the test suite.
        :param pulumi.Input[str] team_owner_id: The GraphQL ID of the team to mark as the owner/admin of the test suite.
        :param pulumi.Input[str] uuid: The UUID of the test suite.
        """
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if default_branch is not None:
            pulumi.set(__self__, "default_branch", default_branch)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if team_owner_id is not None:
            pulumi.set(__self__, "team_owner_id", team_owner_id)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        The API token to use to send test run data to the API.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[pulumi.Input[str]]:
        """
        The default branch for the repository this test suite is for.
        """
        return pulumi.get(self, "default_branch")

    @default_branch.setter
    def default_branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_branch", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name to give the test suite.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        """
        The generated slug of the test suite.
        """
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter(name="teamOwnerId")
    def team_owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GraphQL ID of the team to mark as the owner/admin of the test suite.
        """
        return pulumi.get(self, "team_owner_id")

    @team_owner_id.setter
    def team_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_owner_id", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the test suite.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


class TestSuite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_branch: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A test suite is a collection of tests. A run is to a suite what a build is to a Pipeline.Use this resource to manage [Test Suites](https://buildkite.com/docs/test-analytics) on Buildkite.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        # create a test suite for the main repository
        main = buildkite.test_suite.TestSuite("main",
            default_branch="main",
            team_owner_id="VGVhbvDf4eRef20tMzIxMGEfYTctNzEF5g00M8f5s6E2YjYtODNlOGNlZgD6HcBi")
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_branch: The default branch for the repository this test suite is for.
        :param pulumi.Input[str] name: The name to give the test suite.
        :param pulumi.Input[str] team_owner_id: The GraphQL ID of the team to mark as the owner/admin of the test suite.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TestSuiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A test suite is a collection of tests. A run is to a suite what a build is to a Pipeline.Use this resource to manage [Test Suites](https://buildkite.com/docs/test-analytics) on Buildkite.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        # create a test suite for the main repository
        main = buildkite.test_suite.TestSuite("main",
            default_branch="main",
            team_owner_id="VGVhbvDf4eRef20tMzIxMGEfYTctNzEF5g00M8f5s6E2YjYtODNlOGNlZgD6HcBi")
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param TestSuiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TestSuiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_branch: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TestSuiteArgs.__new__(TestSuiteArgs)

            if default_branch is None and not opts.urn:
                raise TypeError("Missing required property 'default_branch'")
            __props__.__dict__["default_branch"] = default_branch
            __props__.__dict__["name"] = name
            if team_owner_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_owner_id'")
            __props__.__dict__["team_owner_id"] = team_owner_id
            __props__.__dict__["api_token"] = None
            __props__.__dict__["slug"] = None
            __props__.__dict__["uuid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TestSuite, __self__).__init__(
            'buildkite:TestSuite/testSuite:TestSuite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_token: Optional[pulumi.Input[str]] = None,
            default_branch: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            team_owner_id: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None) -> 'TestSuite':
        """
        Get an existing TestSuite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_token: The API token to use to send test run data to the API.
        :param pulumi.Input[str] default_branch: The default branch for the repository this test suite is for.
        :param pulumi.Input[str] name: The name to give the test suite.
        :param pulumi.Input[str] slug: The generated slug of the test suite.
        :param pulumi.Input[str] team_owner_id: The GraphQL ID of the team to mark as the owner/admin of the test suite.
        :param pulumi.Input[str] uuid: The UUID of the test suite.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TestSuiteState.__new__(_TestSuiteState)

        __props__.__dict__["api_token"] = api_token
        __props__.__dict__["default_branch"] = default_branch
        __props__.__dict__["name"] = name
        __props__.__dict__["slug"] = slug
        __props__.__dict__["team_owner_id"] = team_owner_id
        __props__.__dict__["uuid"] = uuid
        return TestSuite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> pulumi.Output[str]:
        """
        The API token to use to send test run data to the API.
        """
        return pulumi.get(self, "api_token")

    @property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> pulumi.Output[str]:
        """
        The default branch for the repository this test suite is for.
        """
        return pulumi.get(self, "default_branch")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name to give the test suite.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        """
        The generated slug of the test suite.
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter(name="teamOwnerId")
    def team_owner_id(self) -> pulumi.Output[str]:
        """
        The GraphQL ID of the team to mark as the owner/admin of the test suite.
        """
        return pulumi.get(self, "team_owner_id")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        The UUID of the test suite.
        """
        return pulumi.get(self, "uuid")

