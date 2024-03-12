// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite.Pipeline
{
    /// <summary>
    /// Manage team access to a pipeline.
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
    ///     var pipeline = new Buildkite.Pipeline.Pipeline("pipeline", new()
    ///     {
    ///         Repository = "https://github.com/...",
    ///     });
    ///
    ///     var team = new Buildkite.Team.Team("team", new()
    ///     {
    ///         Privacy = "VISIBLE",
    ///         DefaultTeam = false,
    ///         DefaultMemberRole = "MEMBER",
    ///     });
    ///
    ///     // allow everyone in the "Everyone" team read-only access to pipeline
    ///     var pipelineTeam = new Buildkite.Pipeline.Team("pipelineTeam", new()
    ///     {
    ///         PipelineId = pipeline.Id,
    ///         TeamId = team.Id,
    ///         AccessLevel = "READ_ONLY",
    ///     });
    ///
    /// });
    /// ```
    /// <!--End PulumiCodeChooser -->
    ///
    /// ## Import
    ///
    /// import a pipeline team resource using the GraphQL ID
    ///
    /// #
    ///
    /// you can use this query to find the ID:
    ///
    /// query getPipelineTeamId {
    ///
    ///   pipeline(slug: "ORGANIZATION_SLUG/PIPELINE_SLUG") {
    ///
    ///     teams(first: 5, search: "PIPELINE_SEARCH_TERM") {
    ///
    ///       edges{
    ///
    ///         node{
    ///
    ///           id
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
    /// $ pulumi import buildkite:Pipeline/team:Team guests VGVhbS0tLWU1YjQyMDQyLTUzN2QtNDZjNi04MjY0LTliZjFkMzkyYjZkNQ==
    /// ```
    /// </summary>
    [BuildkiteResourceType("buildkite:Pipeline/team:Team")]
    public partial class Team : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The access level for the team. Either `READ_ONLY`, `BUILD_AND_READ` or `MANAGE_BUILD_AND_READ`.
        /// </summary>
        [Output("accessLevel")]
        public Output<string> AccessLevel { get; private set; } = null!;

        /// <summary>
        /// The GraphQL ID of the pipeline.
        /// </summary>
        [Output("pipelineId")]
        public Output<string> PipelineId { get; private set; } = null!;

        /// <summary>
        /// The GraphQL ID of the team.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;

        /// <summary>
        /// The UUID of the pipeline-team relationship.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Team resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Team(string name, TeamArgs args, CustomResourceOptions? options = null)
            : base("buildkite:Pipeline/team:Team", name, args ?? new TeamArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Team(string name, Input<string> id, TeamState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:Pipeline/team:Team", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Team resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Team Get(string name, Input<string> id, TeamState? state = null, CustomResourceOptions? options = null)
        {
            return new Team(name, id, state, options);
        }
    }

    public sealed class TeamArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access level for the team. Either `READ_ONLY`, `BUILD_AND_READ` or `MANAGE_BUILD_AND_READ`.
        /// </summary>
        [Input("accessLevel", required: true)]
        public Input<string> AccessLevel { get; set; } = null!;

        /// <summary>
        /// The GraphQL ID of the pipeline.
        /// </summary>
        [Input("pipelineId", required: true)]
        public Input<string> PipelineId { get; set; } = null!;

        /// <summary>
        /// The GraphQL ID of the team.
        /// </summary>
        [Input("teamId", required: true)]
        public Input<string> TeamId { get; set; } = null!;

        public TeamArgs()
        {
        }
        public static new TeamArgs Empty => new TeamArgs();
    }

    public sealed class TeamState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access level for the team. Either `READ_ONLY`, `BUILD_AND_READ` or `MANAGE_BUILD_AND_READ`.
        /// </summary>
        [Input("accessLevel")]
        public Input<string>? AccessLevel { get; set; }

        /// <summary>
        /// The GraphQL ID of the pipeline.
        /// </summary>
        [Input("pipelineId")]
        public Input<string>? PipelineId { get; set; }

        /// <summary>
        /// The GraphQL ID of the team.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// The UUID of the pipeline-team relationship.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public TeamState()
        {
        }
        public static new TeamState Empty => new TeamState();
    }
}
