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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, color=None, description=None, emoji=None, id=None, name=None, uuid=None):
        if color and not isinstance(color, str):
            raise TypeError("Expected argument 'color' to be a str")
        pulumi.set(__self__, "color", color)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if emoji and not isinstance(emoji, str):
            raise TypeError("Expected argument 'emoji' to be a str")
        pulumi.set(__self__, "emoji", emoji)
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
    def color(self) -> str:
        """
        The color given the cluster.
        """
        return pulumi.get(self, "color")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the cluster.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def emoji(self) -> str:
        """
        The emoji given the cluster.
        """
        return pulumi.get(self, "emoji")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The GraphQL ID of the cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        The UUID of the cluster.
        """
        return pulumi.get(self, "uuid")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            color=self.color,
            description=self.description,
            emoji=self.emoji,
            id=self.id,
            name=self.name,
            uuid=self.uuid)


def get_cluster(name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Use this data source to access information about an existing resource.

    :param str name: The name of the cluster to lookup.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('buildkite:Cluster/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        color=pulumi.get(__ret__, 'color'),
        description=pulumi.get(__ret__, 'description'),
        emoji=pulumi.get(__ret__, 'emoji'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        uuid=pulumi.get(__ret__, 'uuid'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Use this data source to access information about an existing resource.

    :param str name: The name of the cluster to lookup.
    """
    ...
