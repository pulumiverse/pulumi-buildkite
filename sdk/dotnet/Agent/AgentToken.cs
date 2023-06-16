// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite.Agent
{
    /// <summary>
    /// ## # Resource: agent_token
    /// 
    /// This resource allows you to create and manage agent tokens.
    /// 
    /// Buildkite Documentation: https://buildkite.com/docs/agent/v3/tokens
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
    ///     var fleet = new Buildkite.Agent.AgentToken("fleet", new()
    ///     {
    ///         Description = "token used by build fleet",
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [BuildkiteResourceType("buildkite:Agent/agentToken:AgentToken")]
    public partial class AgentToken : global::Pulumi.CustomResource
    {
        /// <summary>
        /// This is the description of the agent token.
        /// 
        /// &gt; Changing `description` will cause the resource to be destroyed and re-created.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The value of the created agent token.
        /// </summary>
        [Output("token")]
        public Output<string> Token { get; private set; } = null!;

        /// <summary>
        /// The UUID of the token.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a AgentToken resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AgentToken(string name, AgentTokenArgs? args = null, CustomResourceOptions? options = null)
            : base("buildkite:Agent/agentToken:AgentToken", name, args ?? new AgentTokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AgentToken(string name, Input<string> id, AgentTokenState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:Agent/agentToken:AgentToken", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AgentToken resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AgentToken Get(string name, Input<string> id, AgentTokenState? state = null, CustomResourceOptions? options = null)
        {
            return new AgentToken(name, id, state, options);
        }
    }

    public sealed class AgentTokenArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// This is the description of the agent token.
        /// 
        /// &gt; Changing `description` will cause the resource to be destroyed and re-created.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        public AgentTokenArgs()
        {
        }
        public static new AgentTokenArgs Empty => new AgentTokenArgs();
    }

    public sealed class AgentTokenState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// This is the description of the agent token.
        /// 
        /// &gt; Changing `description` will cause the resource to be destroyed and re-created.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The value of the created agent token.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        /// <summary>
        /// The UUID of the token.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public AgentTokenState()
        {
        }
        public static new AgentTokenState Empty => new AgentTokenState();
    }
}
