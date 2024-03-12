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
    /// A pipeline schedule is a schedule that triggers a pipeline to run at a specific time.
    ///
    /// You can find more information in the [documentation](https://buildkite.com/docs/pipelines/scheduled-builds).
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
    ///     // create a pipeline
    ///     var pipeline = new Buildkite.Pipeline.Pipeline("pipeline", new()
    ///     {
    ///         Repository = "https://github.com/...",
    ///     });
    ///
    ///     // schedule a build at midnight every day
    ///     var nightly = new Buildkite.Pipeline.Schedule("nightly", new()
    ///     {
    ///         PipelineId = buildkite_pipeline.Repo.Id,
    ///         Label = "Nightly build",
    ///         Cronline = "@midnight",
    ///         Branch = buildkite_pipeline.Repo.Default_branch,
    ///     });
    ///
    /// });
    /// ```
    /// <!--End PulumiCodeChooser -->
    ///
    /// ## Import
    ///
    /// import a pipeline schedule resource using the schedules GraphQL ID
    ///
    /// #
    ///
    /// you can use this query to find the schedule:
    ///
    /// query getPipelineScheduleId {
    ///
    ///   organization(slug: "ORGANIZATION_SLUG") {
    ///
    ///         pipelines(first: 5, search: "PIPELINE_SEARCH_TERM") {
    ///
    ///       edges{
    ///
    ///         node{
    ///
    ///           name
    ///
    ///           schedules{
    ///
    ///             edges{
    ///
    ///               node{
    ///
    ///                 id
    ///
    ///               }
    ///
    ///             }
    ///
    ///           }
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
    /// $ pulumi import buildkite:Pipeline/schedule:Schedule test UGlwZWxpgm5Tf2hhZHVsZ35tLWRk4DdmN7c4LTA5M2ItNDM9YS0gMWE0LTAwZDUgYTAxYvRf49==
    /// ```
    /// </summary>
    [BuildkiteResourceType("buildkite:Pipeline/schedule:Schedule")]
    public partial class Schedule : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The branch that the schedule should run on.
        /// </summary>
        [Output("branch")]
        public Output<string> Branch { get; private set; } = null!;

        /// <summary>
        /// The commit that the schedule should run on.
        /// </summary>
        [Output("commit")]
        public Output<string> Commit { get; private set; } = null!;

        /// <summary>
        /// The cronline that describes when the schedule should run. See[here](https://buildkite.com/docs/pipelines/scheduled-builds#schedule-intervals) for supported syntax.
        /// </summary>
        [Output("cronline")]
        public Output<string> Cronline { get; private set; } = null!;

        /// <summary>
        /// Whether the schedule is enabled or not.
        /// </summary>
        [Output("enabled")]
        public Output<bool> Enabled { get; private set; } = null!;

        /// <summary>
        /// The environment variables that scheduled builds should use.
        /// </summary>
        [Output("env")]
        public Output<ImmutableDictionary<string, string>?> Env { get; private set; } = null!;

        /// <summary>
        /// A label to describe the schedule.
        /// </summary>
        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        /// <summary>
        /// The message the builds show for builds created by this schedule.
        /// </summary>
        [Output("message")]
        public Output<string?> Message { get; private set; } = null!;

        /// <summary>
        /// The GraphQL ID of the pipeline that this schedule belongs to.
        /// </summary>
        [Output("pipelineId")]
        public Output<string> PipelineId { get; private set; } = null!;

        /// <summary>
        /// The UUID of the schedule.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Schedule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Schedule(string name, ScheduleArgs args, CustomResourceOptions? options = null)
            : base("buildkite:Pipeline/schedule:Schedule", name, args ?? new ScheduleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Schedule(string name, Input<string> id, ScheduleState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:Pipeline/schedule:Schedule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Schedule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Schedule Get(string name, Input<string> id, ScheduleState? state = null, CustomResourceOptions? options = null)
        {
            return new Schedule(name, id, state, options);
        }
    }

    public sealed class ScheduleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The branch that the schedule should run on.
        /// </summary>
        [Input("branch", required: true)]
        public Input<string> Branch { get; set; } = null!;

        /// <summary>
        /// The commit that the schedule should run on.
        /// </summary>
        [Input("commit")]
        public Input<string>? Commit { get; set; }

        /// <summary>
        /// The cronline that describes when the schedule should run. See[here](https://buildkite.com/docs/pipelines/scheduled-builds#schedule-intervals) for supported syntax.
        /// </summary>
        [Input("cronline", required: true)]
        public Input<string> Cronline { get; set; } = null!;

        /// <summary>
        /// Whether the schedule is enabled or not.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("env")]
        private InputMap<string>? _env;

        /// <summary>
        /// The environment variables that scheduled builds should use.
        /// </summary>
        public InputMap<string> Env
        {
            get => _env ?? (_env = new InputMap<string>());
            set => _env = value;
        }

        /// <summary>
        /// A label to describe the schedule.
        /// </summary>
        [Input("label", required: true)]
        public Input<string> Label { get; set; } = null!;

        /// <summary>
        /// The message the builds show for builds created by this schedule.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// The GraphQL ID of the pipeline that this schedule belongs to.
        /// </summary>
        [Input("pipelineId", required: true)]
        public Input<string> PipelineId { get; set; } = null!;

        public ScheduleArgs()
        {
        }
        public static new ScheduleArgs Empty => new ScheduleArgs();
    }

    public sealed class ScheduleState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The branch that the schedule should run on.
        /// </summary>
        [Input("branch")]
        public Input<string>? Branch { get; set; }

        /// <summary>
        /// The commit that the schedule should run on.
        /// </summary>
        [Input("commit")]
        public Input<string>? Commit { get; set; }

        /// <summary>
        /// The cronline that describes when the schedule should run. See[here](https://buildkite.com/docs/pipelines/scheduled-builds#schedule-intervals) for supported syntax.
        /// </summary>
        [Input("cronline")]
        public Input<string>? Cronline { get; set; }

        /// <summary>
        /// Whether the schedule is enabled or not.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("env")]
        private InputMap<string>? _env;

        /// <summary>
        /// The environment variables that scheduled builds should use.
        /// </summary>
        public InputMap<string> Env
        {
            get => _env ?? (_env = new InputMap<string>());
            set => _env = value;
        }

        /// <summary>
        /// A label to describe the schedule.
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The message the builds show for builds created by this schedule.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// The GraphQL ID of the pipeline that this schedule belongs to.
        /// </summary>
        [Input("pipelineId")]
        public Input<string>? PipelineId { get; set; }

        /// <summary>
        /// The UUID of the schedule.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public ScheduleState()
        {
        }
        public static new ScheduleState Empty => new ScheduleState();
    }
}
