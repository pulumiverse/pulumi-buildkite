// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite.Cluster
{
    /// <summary>
    /// ## # Resource: cluster_queue
    /// 
    /// This resource allows you to create and manage cluster queues.
    /// 
    /// Buildkite Documentation: https://buildkite.com/docs/clusters/manage-clusters#set-up-clusters-create-a-queue
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Buildkite = Pulumiverse.Buildkite;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var queue1 = new Buildkite.Cluster.ClusterQueue("queue1", new()
    ///     {
    ///         ClusterId = "Q2x1c3Rlci0tLTMzMDc0ZDhiLTM4MjctNDRkNC05YTQ3LTkwN2E2NWZjODViNg==",
    ///         Description = "Prod deployment cluster queue",
    ///         Key = "prod-deploy",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Cluster queues can be imported using its `GraphQL ID`, along with its respective cluster `UUID`, separated by a comma. e.g.
    /// 
    /// ```sh
    ///  $ pulumi import buildkite:Cluster/clusterQueue:ClusterQueue test Q2x1c3RlclF1ZXVlLS0tYjJiOGRhNTEtOWY5My00Y2MyLTkyMjktMGRiNzg3ZDQzOTAz,35498aaf-ad05-4fa5-9a07-91bf6cacd2bd
    /// ```
    /// 
    ///  To find the cluster's `UUID` to utilize, you can use the below GraphQL query below. Alternatively, you can use this [pre-saved query](https://buildkite.com/user/graphql/console/3adf0389-02bd-45ef-adcd-4e8e5ae57f25), where you will need fo fill in the organization slug (ORGANIZATION_SLUG) for obtaining the relevant cluster name/`UUID` that the cluster queue is in. graphql query getClusters {
    /// 
    ///  organization(slug"ORGANIZATION_SLUG") {
    /// 
    ///  clusters(first50) {
    /// 
    ///  edges{
    /// 
    ///  node{
    /// 
    ///  name
    /// 
    ///  uuid
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  } } After the cluster `UUID` has been found, you can use the below GraphQL query to find the cluster queue's `GraphQL ID`. Alternatively, this [pre-saved query](https://buildkite.com/user/graphql/console/1d913905-900e-40e7-8f46-651543487b5a) can be used, specifying the organization slug (ORGANIZATION_SLUG) and the cluster `UUID` from above (CLUSTER_UUID). graphql query getClusterQueues {
    /// 
    ///  organization(slug"ORGANIZATION_SLUG") {
    /// 
    ///  cluster(id"CLUSTER_UUID") {
    /// 
    ///  queues(first50) {
    /// 
    ///  edges {
    /// 
    ///  node {
    /// 
    ///  id
    /// 
    ///  key
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  } }
    /// </summary>
    [BuildkiteResourceType("buildkite:Cluster/clusterQueue:ClusterQueue")]
    public partial class ClusterQueue : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the cluster that this cluster queue belongs to.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// The UUID of the cluster that this cluster queue belongs to.
        /// </summary>
        [Output("clusterUuid")]
        public Output<string> ClusterUuid { get; private set; } = null!;

        /// <summary>
        /// The description of the cluster queue.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The key of the cluster queue.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The UUID of the created cluster queue.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterQueue resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterQueue(string name, ClusterQueueArgs args, CustomResourceOptions? options = null)
            : base("buildkite:Cluster/clusterQueue:ClusterQueue", name, args ?? new ClusterQueueArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterQueue(string name, Input<string> id, ClusterQueueState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:Cluster/clusterQueue:ClusterQueue", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse/pulumi-buildkite",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ClusterQueue resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterQueue Get(string name, Input<string> id, ClusterQueueState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterQueue(name, id, state, options);
        }
    }

    public sealed class ClusterQueueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the cluster that this cluster queue belongs to.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// The description of the cluster queue.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The key of the cluster queue.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        public ClusterQueueArgs()
        {
        }
        public static new ClusterQueueArgs Empty => new ClusterQueueArgs();
    }

    public sealed class ClusterQueueState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the cluster that this cluster queue belongs to.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// The UUID of the cluster that this cluster queue belongs to.
        /// </summary>
        [Input("clusterUuid")]
        public Input<string>? ClusterUuid { get; set; }

        /// <summary>
        /// The description of the cluster queue.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The key of the cluster queue.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The UUID of the created cluster queue.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public ClusterQueueState()
        {
        }
        public static new ClusterQueueState Empty => new ClusterQueueState();
    }
}