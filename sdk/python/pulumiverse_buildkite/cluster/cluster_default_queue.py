# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ClusterDefaultQueueArgs', 'ClusterDefaultQueue']

@pulumi.input_type
class ClusterDefaultQueueArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 queue_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ClusterDefaultQueue resource.
        :param pulumi.Input[str] cluster_id: The GraphQL ID of the cluster to which to add a default queue.
        :param pulumi.Input[str] queue_id: The GraphQL ID of the cluster queue to set as default on the cluster.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "queue_id", queue_id)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The GraphQL ID of the cluster to which to add a default queue.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Input[str]:
        """
        The GraphQL ID of the cluster queue to set as default on the cluster.
        """
        return pulumi.get(self, "queue_id")

    @queue_id.setter
    def queue_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "queue_id", value)


@pulumi.input_type
class _ClusterDefaultQueueState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ClusterDefaultQueue resources.
        :param pulumi.Input[str] cluster_id: The GraphQL ID of the cluster to which to add a default queue.
        :param pulumi.Input[str] queue_id: The GraphQL ID of the cluster queue to set as default on the cluster.
        :param pulumi.Input[str] uuid: The UUID of the cluster.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if queue_id is not None:
            pulumi.set(__self__, "queue_id", queue_id)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GraphQL ID of the cluster to which to add a default queue.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GraphQL ID of the cluster queue to set as default on the cluster.
        """
        return pulumi.get(self, "queue_id")

    @queue_id.setter
    def queue_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_id", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the cluster.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


class ClusterDefaultQueue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to manage a default queue for a Buildkite Cluster.
        Find out more information in our [documentation](https://buildkite.com/docs/clusters/overview).

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        # create a cluster
        primary_cluster = buildkite.cluster.Cluster("primaryCluster",
            description="Runs the monolith build and deploy",
            emoji="🚀",
            color="#bada55")
        default = buildkite.cluster.ClusterQueue("default",
            cluster_id=primary_cluster.id,
            key="default")
        primary_cluster_default_queue = buildkite.cluster.ClusterDefaultQueue("primaryClusterDefaultQueue",
            cluster_id=primary_cluster.id,
            queue_id=default.id)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        import a clusters default queue resource using the GraphQL ID of the cluster itself

        #

        you can use this query to find the ID:

        query getClusters {

          organization(slug: "ORGANIZATION"){

            clusters(first: 5, order:NAME) {

              edges{

                node {

                  id

                  name

                }

              }

            }

          }

        }

        ```sh
        $ pulumi import buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue primary Q2x1c3Rlci0tLTI3ZmFmZjA4LTA3OWEtNDk5ZC1hMmIwLTIzNmY3NWFkMWZjYg==
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The GraphQL ID of the cluster to which to add a default queue.
        :param pulumi.Input[str] queue_id: The GraphQL ID of the cluster queue to set as default on the cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterDefaultQueueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to manage a default queue for a Buildkite Cluster.
        Find out more information in our [documentation](https://buildkite.com/docs/clusters/overview).

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        # create a cluster
        primary_cluster = buildkite.cluster.Cluster("primaryCluster",
            description="Runs the monolith build and deploy",
            emoji="🚀",
            color="#bada55")
        default = buildkite.cluster.ClusterQueue("default",
            cluster_id=primary_cluster.id,
            key="default")
        primary_cluster_default_queue = buildkite.cluster.ClusterDefaultQueue("primaryClusterDefaultQueue",
            cluster_id=primary_cluster.id,
            queue_id=default.id)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        import a clusters default queue resource using the GraphQL ID of the cluster itself

        #

        you can use this query to find the ID:

        query getClusters {

          organization(slug: "ORGANIZATION"){

            clusters(first: 5, order:NAME) {

              edges{

                node {

                  id

                  name

                }

              }

            }

          }

        }

        ```sh
        $ pulumi import buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue primary Q2x1c3Rlci0tLTI3ZmFmZjA4LTA3OWEtNDk5ZC1hMmIwLTIzNmY3NWFkMWZjYg==
        ```

        :param str resource_name: The name of the resource.
        :param ClusterDefaultQueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterDefaultQueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterDefaultQueueArgs.__new__(ClusterDefaultQueueArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if queue_id is None and not opts.urn:
                raise TypeError("Missing required property 'queue_id'")
            __props__.__dict__["queue_id"] = queue_id
            __props__.__dict__["uuid"] = None
        super(ClusterDefaultQueue, __self__).__init__(
            'buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            queue_id: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None) -> 'ClusterDefaultQueue':
        """
        Get an existing ClusterDefaultQueue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The GraphQL ID of the cluster to which to add a default queue.
        :param pulumi.Input[str] queue_id: The GraphQL ID of the cluster queue to set as default on the cluster.
        :param pulumi.Input[str] uuid: The UUID of the cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterDefaultQueueState.__new__(_ClusterDefaultQueueState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["queue_id"] = queue_id
        __props__.__dict__["uuid"] = uuid
        return ClusterDefaultQueue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The GraphQL ID of the cluster to which to add a default queue.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Output[str]:
        """
        The GraphQL ID of the cluster queue to set as default on the cluster.
        """
        return pulumi.get(self, "queue_id")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        The UUID of the cluster.
        """
        return pulumi.get(self, "uuid")

