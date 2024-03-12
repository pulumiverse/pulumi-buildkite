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
    'GetTemplateResult',
    'AwaitableGetTemplateResult',
    'get_template',
    'get_template_output',
]

@pulumi.output_type
class GetTemplateResult:
    """
    A collection of values returned by getTemplate.
    """
    def __init__(__self__, available=None, configuration=None, description=None, id=None, name=None, uuid=None):
        if available and not isinstance(available, bool):
            raise TypeError("Expected argument 'available' to be a bool")
        pulumi.set(__self__, "available", available)
        if configuration and not isinstance(configuration, str):
            raise TypeError("Expected argument 'configuration' to be a str")
        pulumi.set(__self__, "configuration", configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def available(self) -> bool:
        """
        If the pipeline template is available for assignment by non admin users.
        """
        return pulumi.get(self, "available")

    @property
    @pulumi.getter
    def configuration(self) -> str:
        """
        The YAML step configuration for the pipeline template.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description for the pipeline template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The GraphQL ID of the pipeline template.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the pipeline template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        The UUID of the pipeline template.
        """
        return pulumi.get(self, "uuid")


class AwaitableGetTemplateResult(GetTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTemplateResult(
            available=self.available,
            configuration=self.configuration,
            description=self.description,
            id=self.id,
            name=self.name,
            uuid=self.uuid)


def get_template(id: Optional[str] = None,
                 name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTemplateResult:
    """
    Use this data source to retrieve a pipeline template by its ID or name.

    More information on pipeline templates can be found in the [documentation](https://buildkite.com/docs/pipelines/templates).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_buildkite as buildkite
    import pulumiverse_buildkite as buildkite

    repository = "git@github.com:my-org/my-repo.git"
    dev_template = buildkite.Pipeline.get_template(id=buildkite_pipeline_template["template_dev"]["id"])
    frontend_template = buildkite.Pipeline.get_template(name="Frontend app template")
    apiv2_dev = buildkite.pipeline.Pipeline("apiv2Dev",
        repository=repository,
        pipeline_template_id=dev_template.id)
    frontend = buildkite.pipeline.Pipeline("frontend",
        repository=repository,
        pipeline_template_id=frontend_template.id)
    ```
    <!--End PulumiCodeChooser -->


    :param str id: The GraphQL ID of the pipeline template.
    :param str name: The name of the pipeline template.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('buildkite:Pipeline/getTemplate:getTemplate', __args__, opts=opts, typ=GetTemplateResult).value

    return AwaitableGetTemplateResult(
        available=pulumi.get(__ret__, 'available'),
        configuration=pulumi.get(__ret__, 'configuration'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        uuid=pulumi.get(__ret__, 'uuid'))


@_utilities.lift_output_func(get_template)
def get_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTemplateResult]:
    """
    Use this data source to retrieve a pipeline template by its ID or name.

    More information on pipeline templates can be found in the [documentation](https://buildkite.com/docs/pipelines/templates).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_buildkite as buildkite
    import pulumiverse_buildkite as buildkite

    repository = "git@github.com:my-org/my-repo.git"
    dev_template = buildkite.Pipeline.get_template(id=buildkite_pipeline_template["template_dev"]["id"])
    frontend_template = buildkite.Pipeline.get_template(name="Frontend app template")
    apiv2_dev = buildkite.pipeline.Pipeline("apiv2Dev",
        repository=repository,
        pipeline_template_id=dev_template.id)
    frontend = buildkite.pipeline.Pipeline("frontend",
        repository=repository,
        pipeline_template_id=frontend_template.id)
    ```
    <!--End PulumiCodeChooser -->


    :param str id: The GraphQL ID of the pipeline template.
    :param str name: The name of the pipeline template.
    """
    ...
