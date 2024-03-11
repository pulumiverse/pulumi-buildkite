// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite.Organization
{
    /// <summary>
    /// This resource allows you to create and manage banners for specific organizations, displayed to all members at the top of each page in Buildkite's UI.
    /// 
    /// More information on organization/system banners can be found in the [documentation](https://buildkite.com/docs/team-management/system-banners).
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
    ///     var banner = new Buildkite.Organization.Banner("banner", new()
    ///     {
    ///         Message = ":warning: Please be aware of the maintenance window this weekend!",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// import an organization banner resource using the banner's GraphQL ID
    /// 
    /// # 
    /// 
    ///  you can use this query to find the banner's ID:
    /// 
    ///  query getOrganizationBannerId {
    /// 
    ///  organization(slug: "ORGANIZATION_SLUG") {
    /// 
    ///  banners(first: 1) {
    /// 
    ///  edges {
    /// 
    ///  node {
    /// 
    ///  id
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  }
    /// 
    ///  }
    /// 
    /// ```sh
    /// $ pulumi import buildkite:Organization/banner:Banner banner T3JnYW5pemF0aW9uQmFubmVyLS0tNjZlMmE5YzktM2IzMy00OGE5LTk1NjItMzY2YzMwNzYzN2Uz
    /// ```
    /// </summary>
    [BuildkiteResourceType("buildkite:Organization/banner:Banner")]
    public partial class Banner : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The organization banner's message.
        /// </summary>
        [Output("message")]
        public Output<string> Message { get; private set; } = null!;

        /// <summary>
        /// The UUID of the organization banner.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Banner resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Banner(string name, BannerArgs args, CustomResourceOptions? options = null)
            : base("buildkite:Organization/banner:Banner", name, args ?? new BannerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Banner(string name, Input<string> id, BannerState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:Organization/banner:Banner", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Banner resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Banner Get(string name, Input<string> id, BannerState? state = null, CustomResourceOptions? options = null)
        {
            return new Banner(name, id, state, options);
        }
    }

    public sealed class BannerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The organization banner's message.
        /// </summary>
        [Input("message", required: true)]
        public Input<string> Message { get; set; } = null!;

        public BannerArgs()
        {
        }
        public static new BannerArgs Empty => new BannerArgs();
    }

    public sealed class BannerState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The organization banner's message.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// The UUID of the organization banner.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public BannerState()
        {
        }
        public static new BannerState Empty => new BannerState();
    }
}