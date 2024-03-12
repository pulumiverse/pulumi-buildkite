# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPipelineResult',
    'AwaitableGetPipelineResult',
    'get_pipeline',
    'get_pipeline_output',
]

@pulumi.output_type
class GetPipelineResult:
    """
    A collection of values returned by getPipeline.
    """
    def __init__(__self__, default_branch=None, description=None, id=None, name=None, repository=None, slug=None, uuid=None, webhook_url=None):
        if default_branch and not isinstance(default_branch, str):
            raise TypeError("Expected argument 'default_branch' to be a str")
        pulumi.set(__self__, "default_branch", default_branch)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if repository and not isinstance(repository, str):
            raise TypeError("Expected argument 'repository' to be a str")
        pulumi.set(__self__, "repository", repository)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if webhook_url and not isinstance(webhook_url, str):
            raise TypeError("Expected argument 'webhook_url' to be a str")
        pulumi.set(__self__, "webhook_url", webhook_url)

    @property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> str:
        """
        The default branch to prefill when new builds are created or triggered.
        """
        return pulumi.get(self, "default_branch")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The GraphQL ID of the pipeline.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the pipeline.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def repository(self) -> str:
        """
        The git URL of the repository.
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter
    def slug(self) -> str:
        """
        The slug of the pipeline.
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        The UUID of the pipeline.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="webhookUrl")
    def webhook_url(self) -> str:
        """
        The Buildkite webhook URL that triggers builds on this pipeline.
        """
        return pulumi.get(self, "webhook_url")


class AwaitableGetPipelineResult(GetPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineResult(
            default_branch=self.default_branch,
            description=self.description,
            id=self.id,
            name=self.name,
            repository=self.repository,
            slug=self.slug,
            uuid=self.uuid,
            webhook_url=self.webhook_url)


def get_pipeline(slug: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineResult:
    """
    Use this data source to look up properties on a specific pipeline. This is particularly useful for looking up the webhook URL for each pipeline.

    More info in the Buildkite [documentation](https://buildkite.com/docs/pipelines).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_buildkite as buildkite

    pipeline = buildkite.Pipeline.get_pipeline(slug="buildkite")
    ```
    <!--End PulumiCodeChooser -->


    :param str slug: The slug of the pipeline.
    """
    __args__ = dict()
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('buildkite:Pipeline/getPipeline:getPipeline', __args__, opts=opts, typ=GetPipelineResult).value

    return AwaitableGetPipelineResult(
        default_branch=pulumi.get(__ret__, 'default_branch'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        repository=pulumi.get(__ret__, 'repository'),
        slug=pulumi.get(__ret__, 'slug'),
        uuid=pulumi.get(__ret__, 'uuid'),
        webhook_url=pulumi.get(__ret__, 'webhook_url'))


@_utilities.lift_output_func(get_pipeline)
def get_pipeline_output(slug: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineResult]:
    """
    Use this data source to look up properties on a specific pipeline. This is particularly useful for looking up the webhook URL for each pipeline.

    More info in the Buildkite [documentation](https://buildkite.com/docs/pipelines).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_buildkite as buildkite

    pipeline = buildkite.Pipeline.get_pipeline(slug="buildkite")
    ```
    <!--End PulumiCodeChooser -->


    :param str slug: The slug of the pipeline.
    """
    ...
