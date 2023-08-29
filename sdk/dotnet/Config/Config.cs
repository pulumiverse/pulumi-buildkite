// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumiverse.Buildkite
{
    public static class Config
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("buildkite");

        private static readonly __Value<string?> _apiToken = new __Value<string?>(() => __config.Get("apiToken"));
        /// <summary>
        /// API token with GraphQL access and `write_pipelines, read_pipelines` and `write_suites` REST API scopes
        /// </summary>
        public static string? ApiToken
        {
            get => _apiToken.Get();
            set => _apiToken.Set(value);
        }

        private static readonly __Value<bool?> _archivePipelineOnDelete = new __Value<bool?>(() => __config.GetBoolean("archivePipelineOnDelete"));
        /// <summary>
        /// Archive pipelines when destroying instead of completely deleting.
        /// </summary>
        public static bool? ArchivePipelineOnDelete
        {
            get => _archivePipelineOnDelete.Get();
            set => _archivePipelineOnDelete.Set(value);
        }

        private static readonly __Value<string?> _graphqlUrl = new __Value<string?>(() => __config.Get("graphqlUrl"));
        /// <summary>
        /// Base URL for the GraphQL API to use
        /// </summary>
        public static string? GraphqlUrl
        {
            get => _graphqlUrl.Get();
            set => _graphqlUrl.Set(value);
        }

        private static readonly __Value<string?> _organization = new __Value<string?>(() => __config.Get("organization"));
        /// <summary>
        /// The Buildkite organization slug
        /// </summary>
        public static string? Organization
        {
            get => _organization.Get();
            set => _organization.Set(value);
        }

        private static readonly __Value<string?> _restUrl = new __Value<string?>(() => __config.Get("restUrl"));
        /// <summary>
        /// Base URL for the REST API to use
        /// </summary>
        public static string? RestUrl
        {
            get => _restUrl.Get();
            set => _restUrl.Set(value);
        }

    }
}
