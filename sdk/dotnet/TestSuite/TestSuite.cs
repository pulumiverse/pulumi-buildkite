// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite.TestSuite
{
    /// <summary>
    /// ## # Resource: test_suite
    /// 
    /// This resources allows you to create and manage a Test Suite.
    /// 
    /// Buildkite documentation: https://buildkite.com/docs/test-analytics
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
    ///     var test = new Buildkite.Team.Team("test", new()
    ///     {
    ///         Privacy = "VISIBLE",
    ///         DefaultTeam = false,
    ///         DefaultMemberRole = "MEMBER",
    ///     });
    /// 
    ///     var unitTests = new Buildkite.TestSuite.TestSuite("unitTests", new()
    ///     {
    ///         DefaultBranch = "main",
    ///         TeamOwnerId = test.Id,
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [BuildkiteResourceType("buildkite:TestSuite/testSuite:TestSuite")]
    public partial class TestSuite : global::Pulumi.CustomResource
    {
        /// <summary>
        /// This is the unique API token used when send test results.
        /// </summary>
        [Output("apiToken")]
        public Output<string> ApiToken { get; private set; } = null!;

        /// <summary>
        /// This is the default branch used to compare tests against.
        /// </summary>
        [Output("defaultBranch")]
        public Output<string> DefaultBranch { get; private set; } = null!;

        /// <summary>
        /// This is the name of the test suite.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// This is the unique slug generated from the name upon creation.
        /// </summary>
        [Output("slug")]
        public Output<string> Slug { get; private set; } = null!;

        /// <summary>
        /// This is a single team linked to the test suite upon creation.
        /// </summary>
        [Output("teamOwnerId")]
        public Output<string> TeamOwnerId { get; private set; } = null!;

        /// <summary>
        /// This is the UUID of the suite.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a TestSuite resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TestSuite(string name, TestSuiteArgs args, CustomResourceOptions? options = null)
            : base("buildkite:TestSuite/testSuite:TestSuite", name, args ?? new TestSuiteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TestSuite(string name, Input<string> id, TestSuiteState? state = null, CustomResourceOptions? options = null)
            : base("buildkite:TestSuite/testSuite:TestSuite", name, state, MakeResourceOptions(options, id))
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
        /// <summary>
        /// Get an existing TestSuite resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TestSuite Get(string name, Input<string> id, TestSuiteState? state = null, CustomResourceOptions? options = null)
        {
            return new TestSuite(name, id, state, options);
        }
    }

    public sealed class TestSuiteArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// This is the default branch used to compare tests against.
        /// </summary>
        [Input("defaultBranch", required: true)]
        public Input<string> DefaultBranch { get; set; } = null!;

        /// <summary>
        /// This is the name of the test suite.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// This is a single team linked to the test suite upon creation.
        /// </summary>
        [Input("teamOwnerId", required: true)]
        public Input<string> TeamOwnerId { get; set; } = null!;

        public TestSuiteArgs()
        {
        }
        public static new TestSuiteArgs Empty => new TestSuiteArgs();
    }

    public sealed class TestSuiteState : global::Pulumi.ResourceArgs
    {
        [Input("apiToken")]
        private Input<string>? _apiToken;

        /// <summary>
        /// This is the unique API token used when send test results.
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
        /// This is the default branch used to compare tests against.
        /// </summary>
        [Input("defaultBranch")]
        public Input<string>? DefaultBranch { get; set; }

        /// <summary>
        /// This is the name of the test suite.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// This is the unique slug generated from the name upon creation.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        /// <summary>
        /// This is a single team linked to the test suite upon creation.
        /// </summary>
        [Input("teamOwnerId")]
        public Input<string>? TeamOwnerId { get; set; }

        /// <summary>
        /// This is the UUID of the suite.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public TestSuiteState()
        {
        }
        public static new TestSuiteState Empty => new TestSuiteState();
    }
}
