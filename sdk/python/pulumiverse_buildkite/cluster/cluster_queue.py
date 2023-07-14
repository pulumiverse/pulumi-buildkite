# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ClusterQueueArgs', 'ClusterQueue']

@pulumi.input_type
class ClusterQueueArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 key: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ClusterQueue resource.
        :param pulumi.Input[str] cluster_id: The ID of the cluster that this cluster queue belongs to.
        :param pulumi.Input[str] key: The key of the cluster queue.
        :param pulumi.Input[str] description: The description of the cluster queue.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "key", key)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the cluster that this cluster queue belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key of the cluster queue.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the cluster queue.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ClusterQueueState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_uuid: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ClusterQueue resources.
        :param pulumi.Input[str] cluster_id: The ID of the cluster that this cluster queue belongs to.
        :param pulumi.Input[str] cluster_uuid: The UUID of the cluster that this cluster queue belongs to.
        :param pulumi.Input[str] description: The description of the cluster queue.
        :param pulumi.Input[str] key: The key of the cluster queue.
        :param pulumi.Input[str] uuid: The UUID of the created cluster queue.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_uuid is not None:
            pulumi.set(__self__, "cluster_uuid", cluster_uuid)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the cluster that this cluster queue belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the cluster that this cluster queue belongs to.
        """
        return pulumi.get(self, "cluster_uuid")

    @cluster_uuid.setter
    def cluster_uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_uuid", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the cluster queue.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key of the cluster queue.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the created cluster queue.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


class ClusterQueue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Resource: cluster_queue

        This resource allows you to create and manage cluster queues.

        Buildkite Documentation: https://buildkite.com/docs/clusters/manage-clusters#set-up-clusters-create-a-queue

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        queue1 = buildkite.cluster.ClusterQueue("queue1",
            cluster_id="Q2x1c3Rlci0tLTMzMDc0ZDhiLTM4MjctNDRkNC05YTQ3LTkwN2E2NWZjODViNg==",
            description="Prod deployment cluster queue",
            key="prod-deploy")
        ```

        ## Import

        Cluster queues can be imported using its `GraphQL ID`, along with its respective cluster `UUID`, separated by a comma. e.g.

        ```sh
         $ pulumi import buildkite:Cluster/clusterQueue:ClusterQueue test Q2x1c3RlclF1ZXVlLS0tYjJiOGRhNTEtOWY5My00Y2MyLTkyMjktMGRiNzg3ZDQzOTAz,35498aaf-ad05-4fa5-9a07-91bf6cacd2bd
        ```

         To find the cluster's `UUID` to utilize, you can use the below GraphQL query below. Alternatively, you can use this [pre-saved query](https://buildkite.com/user/graphql/console/3adf0389-02bd-45ef-adcd-4e8e5ae57f25), where you will need fo fill in the organization slug (ORGANIZATION_SLUG) for obtaining the relevant cluster name/`UUID` that the cluster queue is in. graphql query getClusters {

         organization(slug"ORGANIZATION_SLUG") {

         clusters(first50) {

         edges{

         node{

         name

         uuid

         }

         }

         }

         } } After the cluster `UUID` has been found, you can use the below GraphQL query to find the cluster queue's `GraphQL ID`. Alternatively, this [pre-saved query](https://buildkite.com/user/graphql/console/1d913905-900e-40e7-8f46-651543487b5a) can be used, specifying the organization slug (ORGANIZATION_SLUG) and the cluster `UUID` from above (CLUSTER_UUID). graphql query getClusterQueues {

         organization(slug"ORGANIZATION_SLUG") {

         cluster(id"CLUSTER_UUID") {

         queues(first50) {

         edges {

         node {

         id

         key

         }

         }

         }

         }

         } }

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the cluster that this cluster queue belongs to.
        :param pulumi.Input[str] description: The description of the cluster queue.
        :param pulumi.Input[str] key: The key of the cluster queue.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterQueueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Resource: cluster_queue

        This resource allows you to create and manage cluster queues.

        Buildkite Documentation: https://buildkite.com/docs/clusters/manage-clusters#set-up-clusters-create-a-queue

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_buildkite as buildkite

        queue1 = buildkite.cluster.ClusterQueue("queue1",
            cluster_id="Q2x1c3Rlci0tLTMzMDc0ZDhiLTM4MjctNDRkNC05YTQ3LTkwN2E2NWZjODViNg==",
            description="Prod deployment cluster queue",
            key="prod-deploy")
        ```

        ## Import

        Cluster queues can be imported using its `GraphQL ID`, along with its respective cluster `UUID`, separated by a comma. e.g.

        ```sh
         $ pulumi import buildkite:Cluster/clusterQueue:ClusterQueue test Q2x1c3RlclF1ZXVlLS0tYjJiOGRhNTEtOWY5My00Y2MyLTkyMjktMGRiNzg3ZDQzOTAz,35498aaf-ad05-4fa5-9a07-91bf6cacd2bd
        ```

         To find the cluster's `UUID` to utilize, you can use the below GraphQL query below. Alternatively, you can use this [pre-saved query](https://buildkite.com/user/graphql/console/3adf0389-02bd-45ef-adcd-4e8e5ae57f25), where you will need fo fill in the organization slug (ORGANIZATION_SLUG) for obtaining the relevant cluster name/`UUID` that the cluster queue is in. graphql query getClusters {

         organization(slug"ORGANIZATION_SLUG") {

         clusters(first50) {

         edges{

         node{

         name

         uuid

         }

         }

         }

         } } After the cluster `UUID` has been found, you can use the below GraphQL query to find the cluster queue's `GraphQL ID`. Alternatively, this [pre-saved query](https://buildkite.com/user/graphql/console/1d913905-900e-40e7-8f46-651543487b5a) can be used, specifying the organization slug (ORGANIZATION_SLUG) and the cluster `UUID` from above (CLUSTER_UUID). graphql query getClusterQueues {

         organization(slug"ORGANIZATION_SLUG") {

         cluster(id"CLUSTER_UUID") {

         queues(first50) {

         edges {

         node {

         id

         key

         }

         }

         }

         }

         } }

        :param str resource_name: The name of the resource.
        :param ClusterQueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterQueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterQueueArgs.__new__(ClusterQueueArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["description"] = description
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["cluster_uuid"] = None
            __props__.__dict__["uuid"] = None
        super(ClusterQueue, __self__).__init__(
            'buildkite:Cluster/clusterQueue:ClusterQueue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cluster_uuid: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None) -> 'ClusterQueue':
        """
        Get an existing ClusterQueue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the cluster that this cluster queue belongs to.
        :param pulumi.Input[str] cluster_uuid: The UUID of the cluster that this cluster queue belongs to.
        :param pulumi.Input[str] description: The description of the cluster queue.
        :param pulumi.Input[str] key: The key of the cluster queue.
        :param pulumi.Input[str] uuid: The UUID of the created cluster queue.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterQueueState.__new__(_ClusterQueueState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cluster_uuid"] = cluster_uuid
        __props__.__dict__["description"] = description
        __props__.__dict__["key"] = key
        __props__.__dict__["uuid"] = uuid
        return ClusterQueue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the cluster that this cluster queue belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> pulumi.Output[str]:
        """
        The UUID of the cluster that this cluster queue belongs to.
        """
        return pulumi.get(self, "cluster_uuid")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the cluster queue.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The key of the cluster queue.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        The UUID of the created cluster queue.
        """
        return pulumi.get(self, "uuid")
