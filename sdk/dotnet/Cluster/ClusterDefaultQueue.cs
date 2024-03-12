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
    /// This resource allows you to manage a default queue for a Buildkite Cluster.
    /// Find out more information in our [documentation](https://buildkite.com/docs/clusters/overview).
    ///
    /// ## Example Usage
    ///
    /// <!--Start PulumiCodeChooser -->
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Buildkite = Pulumiverse.Buildkite;
    ///
    /// return await Deployment.RunAsync(() =>
    /// {
    ///     // create a cluster
    ///     var primaryCluster = new Buildkite.Cluster.Cluster("primaryCluster", new()
    ///     {
    ///         Description = "Runs the monolith build and deploy",
    ///         Emoji = "🚀",
    ///         Color = "#bada55",
    ///     });
    ///
    ///     var @default = new Buildkite.Cluster.ClusterQueue("default", new()
    ///     {
    ///         ClusterId = primaryCluster.Id,
    ///         Key = "default",
    ///     });
    ///
    ///     var primaryClusterDefaultQueue = new Buildkite.Cluster.ClusterDefaultQueue("primaryClusterDefaultQueue", new()
    ///     {
    ///         ClusterId = primaryCluster.Id,
    ///         QueueId = @default.Id,
    ///     });
    ///
    /// });
    /// ```
    /// <!--End PulumiCodeChooser -->
    ///
    /// ## Import
    ///
    /// import a clusters default queue resource using the GraphQL ID of the cluster itself
    ///
    /// #
    ///
    /// you can use this query to find the ID:
    ///
    /// query getClusters {
    ///
    ///   organization(slug: "ORGANIZATION"){
    ///
    ///     clusters(first: 5, order:NAME) {
    ///
    ///       edges{
    ///
    ///         node {
    ///
    ///           id
    ///
    ///           name
    ///
    ///         }
    ///
    ///       }
    ///
    ///     }
    ///
    ///   }
    ///
    /// }
    ///
    /// ```sh
    /// $ pulumi import buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue primary Q2x1c3Rlci0tLTI3ZmFmZjA4LTA3OWEtNDk5ZC1hMmIwLTIzNmY3NWFkMWZjYg==
    /// ```
    /// </summary>
    [BuildkiteResourceType("buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue")]
    public partial class ClusterDefaultQueue : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The GraphQL ID of the cluster to which to add a default queue.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// The GraphQL ID of the cluster queue to set as default on the cluster.
        /// </summary>
        [Output("queueId")]
        public Output<string> QueueId { get; private set; } = null!;

        /// <summary>
        /// The UUID of the cluster.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterDefaultQueue resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterDefaultQueue(string name, ClusterDefaultQueueArgs args, CustomResourceOptions? options = null)
            : base("buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue", name, args ?? new ClusterDefaultQueueArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterDefaultQueue(string name, Input<string> id, ClusterDefaultQueueState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:Cluster/clusterDefaultQueue:ClusterDefaultQueue", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ClusterDefaultQueue resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterDefaultQueue Get(string name, Input<string> id, ClusterDefaultQueueState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterDefaultQueue(name, id, state, options);
        }
    }

    public sealed class ClusterDefaultQueueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The GraphQL ID of the cluster to which to add a default queue.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// The GraphQL ID of the cluster queue to set as default on the cluster.
        /// </summary>
        [Input("queueId", required: true)]
        public Input<string> QueueId { get; set; } = null!;

        public ClusterDefaultQueueArgs()
        {
        }
        public static new ClusterDefaultQueueArgs Empty => new ClusterDefaultQueueArgs();
    }

    public sealed class ClusterDefaultQueueState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The GraphQL ID of the cluster to which to add a default queue.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// The GraphQL ID of the cluster queue to set as default on the cluster.
        /// </summary>
        [Input("queueId")]
        public Input<string>? QueueId { get; set; }

        /// <summary>
        /// The UUID of the cluster.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public ClusterDefaultQueueState()
        {
        }
        public static new ClusterDefaultQueueState Empty => new ClusterDefaultQueueState();
    }
}
