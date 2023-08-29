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
    public static class GetPipeline
    {
        /// <summary>
        /// ## # Data Source: pipeline
        /// 
        /// Use this data source to look up properties on a specific pipeline. This is
        /// particularly useful for looking up the webhook URL for each pipeline.
        /// 
        /// Buildkite Documentation: https://buildkite.com/docs/pipelines
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Buildkite = Pulumi.Buildkite;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var repo2 = Buildkite.Pipeline.GetPipeline.Invoke(new()
        ///     {
        ///         Slug = "repo2",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPipelineResult> InvokeAsync(GetPipelineArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPipelineResult>("buildkite:Pipeline/getPipeline:getPipeline", args ?? new GetPipelineArgs(), options.WithDefaults());

        /// <summary>
        /// ## # Data Source: pipeline
        /// 
        /// Use this data source to look up properties on a specific pipeline. This is
        /// particularly useful for looking up the webhook URL for each pipeline.
        /// 
        /// Buildkite Documentation: https://buildkite.com/docs/pipelines
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Buildkite = Pulumi.Buildkite;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var repo2 = Buildkite.Pipeline.GetPipeline.Invoke(new()
        ///     {
        ///         Slug = "repo2",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPipelineResult> Invoke(GetPipelineInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPipelineResult>("buildkite:Pipeline/getPipeline:getPipeline", args ?? new GetPipelineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPipelineArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The slug of the pipeline, available in the URL of the pipeline on buildkite.com
        /// </summary>
        [Input("slug", required: true)]
        public string Slug { get; set; } = null!;

        public GetPipelineArgs()
        {
        }
        public static new GetPipelineArgs Empty => new GetPipelineArgs();
    }

    public sealed class GetPipelineInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The slug of the pipeline, available in the URL of the pipeline on buildkite.com
        /// </summary>
        [Input("slug", required: true)]
        public Input<string> Slug { get; set; } = null!;

        public GetPipelineInvokeArgs()
        {
        }
        public static new GetPipelineInvokeArgs Empty => new GetPipelineInvokeArgs();
    }


    [OutputType]
    public sealed class GetPipelineResult
    {
        /// <summary>
        /// The default branch to prefill when new builds are created or triggered, usually main or master but can be anything.
        /// </summary>
        public readonly string DefaultBranch;
        /// <summary>
        /// A description of the pipeline.
        /// </summary>
        public readonly string Description;
        public readonly string Id;
        /// <summary>
        /// The name of the pipeline.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The git URL of the repository.
        /// </summary>
        public readonly string Repository;
        public readonly string Slug;
        /// <summary>
        /// The Buildkite webhook URL that triggers builds on this pipeline.
        /// </summary>
        public readonly string WebhookUrl;

        [OutputConstructor]
        private GetPipelineResult(
            string defaultBranch,

            string description,

            string id,

            string name,

            string repository,

            string slug,

            string webhookUrl)
        {
            DefaultBranch = defaultBranch;
            Description = description;
            Id = id;
            Name = name;
            Repository = repository;
            Slug = slug;
            WebhookUrl = webhookUrl;
        }
    }
}
