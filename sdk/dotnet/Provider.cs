// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite
{
    /// <summary>
    /// The provider type for the buildkite package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [BuildkiteResourceType("pulumi:providers:buildkite")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// API token with GraphQL access and `write_pipelines, read_pipelines` and `write_suites` REST API scopes
        /// </summary>
        [Output("apiToken")]
        public Output<string?> ApiToken { get; private set; } = null!;

        /// <summary>
        /// Base URL for the GraphQL API to use
        /// </summary>
        [Output("graphqlUrl")]
        public Output<string?> GraphqlUrl { get; private set; } = null!;

        /// <summary>
        /// The Buildkite organization slug
        /// </summary>
        [Output("organization")]
        public Output<string?> Organization { get; private set; } = null!;

        /// <summary>
        /// Base URL for the REST API to use
        /// </summary>
        [Output("restUrl")]
        public Output<string?> RestUrl { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("buildkite", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse/pulumi-buildkite",
                AdditionalSecretOutputs =
                {
                    "apiToken",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiToken")]
        private Input<string>? _apiToken;

        /// <summary>
        /// API token with GraphQL access and `write_pipelines, read_pipelines` and `write_suites` REST API scopes
        /// </summary>
        public Input<string>? ApiToken
        {
            get => _apiToken;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _apiToken = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Archive pipelines when destroying instead of completely deleting.
        /// </summary>
        [Input("archivePipelineOnDelete", json: true)]
        public Input<bool>? ArchivePipelineOnDelete { get; set; }

        /// <summary>
        /// Base URL for the GraphQL API to use
        /// </summary>
        [Input("graphqlUrl")]
        public Input<string>? GraphqlUrl { get; set; }

        /// <summary>
        /// The Buildkite organization slug
        /// </summary>
        [Input("organization")]
        public Input<string>? Organization { get; set; }

        /// <summary>
        /// Base URL for the REST API to use
        /// </summary>
        [Input("restUrl")]
        public Input<string>? RestUrl { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
