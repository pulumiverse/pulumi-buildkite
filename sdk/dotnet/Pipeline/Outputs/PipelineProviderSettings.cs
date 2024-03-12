// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Buildkite.Pipeline.Outputs
{

    [OutputType]
    public sealed class PipelineProviderSettings
    {
        /// <summary>
        /// Whether to create builds when branches are pushed.
        /// </summary>
        public readonly bool? BuildBranches;
        /// <summary>
        /// Whether to create builds for pull requests from third-party forks.
        /// </summary>
        public readonly bool? BuildPullRequestForks;
        /// <summary>
        /// Whether to create builds for pull requests when labels are added or removed.
        /// </summary>
        public readonly bool? BuildPullRequestLabelsChanged;
        /// <summary>
        /// Whether to create a build when a pull request changes to "Ready for review".
        /// </summary>
        public readonly bool? BuildPullRequestReadyForReview;
        /// <summary>
        /// Whether to create builds for commits that are part of a pull request.
        /// </summary>
        public readonly bool? BuildPullRequests;
        /// <summary>
        /// Whether to create builds when tags are pushed.
        /// </summary>
        public readonly bool? BuildTags;
        /// <summary>
        /// Automatically cancel running builds for a branch if the branch is deleted.
        /// </summary>
        public readonly bool? CancelDeletedBranchBuilds;
        /// <summary>
        /// The condition to evaluate when deciding if a build should run. More details available in [the documentation](https://buildkite.com/docs/pipelines/conditionals#conditionals-in-pipelines).
        /// </summary>
        public readonly string? FilterCondition;
        /// <summary>
        /// Whether to filter builds to only run when the condition in `filter_condition` is true.
        /// </summary>
        public readonly bool? FilterEnabled;
        /// <summary>
        /// Prefix branch names for third-party fork builds to ensure they don't trigger branch conditions. For example, the main branch from some-user will become some-user:main.
        /// </summary>
        public readonly bool? PrefixPullRequestForkBranchNames;
        /// <summary>
        /// The status to use for blocked builds. Pending can be used with [required status checks](https://help.github.com/en/articles/enabling-required-status-checks) to prevent merging pull requests with blocked builds.
        /// </summary>
        public readonly bool? PublishBlockedAsPending;
        /// <summary>
        /// Whether to update the status of commits in Bitbucket or GitHub.
        /// </summary>
        public readonly bool? PublishCommitStatus;
        /// <summary>
        /// Whether to create a separate status for each job in a build, allowing you to see the status of each job directly in Bitbucket or GitHub.
        /// </summary>
        public readonly bool? PublishCommitStatusPerStep;
        /// <summary>
        /// Filter pull requests builds by the branch filter.
        /// </summary>
        public readonly string? PullRequestBranchFilterConfiguration;
        /// <summary>
        /// Filter pull request builds.
        /// </summary>
        public readonly bool? PullRequestBranchFilterEnabled;
        /// <summary>
        /// Whether to create a separate status for pull request builds, allowing you to require a passing pull request build in your [required status checks](https://help.github.com/en/articles/enabling-required-status-checks) in GitHub.
        /// </summary>
        public readonly bool? SeparatePullRequestStatuses;
        /// <summary>
        /// Whether to skip creating a new build if an existing build for the commit and branch already exists. This option is only valid if the pipeline uses a GitHub repository.
        /// </summary>
        public readonly bool? SkipBuildsForExistingCommits;
        /// <summary>
        /// Whether to skip creating a new build for a pull request if an existing build for the commit and branch already exists.
        /// </summary>
        public readonly bool? SkipPullRequestBuildsForExistingCommits;
        /// <summary>
        /// What type of event to trigger builds on. Must be one of:
        /// 	- `code` will create builds when code is pushed to GitHub.
        /// 	- `deployment` will create builds when a deployment is created in GitHub.
        /// 	- `fork` will create builds when the GitHub repository is forked.
        /// 	- `none` will not create any builds based on GitHub activity.
        /// 
        /// 	> `trigger_mode` is only valid if the pipeline uses a GitHub repository.
        /// </summary>
        public readonly string? TriggerMode;

        [OutputConstructor]
        private PipelineProviderSettings(
            bool? buildBranches,

            bool? buildPullRequestForks,

            bool? buildPullRequestLabelsChanged,

            bool? buildPullRequestReadyForReview,

            bool? buildPullRequests,

            bool? buildTags,

            bool? cancelDeletedBranchBuilds,

            string? filterCondition,

            bool? filterEnabled,

            bool? prefixPullRequestForkBranchNames,

            bool? publishBlockedAsPending,

            bool? publishCommitStatus,

            bool? publishCommitStatusPerStep,

            string? pullRequestBranchFilterConfiguration,

            bool? pullRequestBranchFilterEnabled,

            bool? separatePullRequestStatuses,

            bool? skipBuildsForExistingCommits,

            bool? skipPullRequestBuildsForExistingCommits,

            string? triggerMode)
        {
            BuildBranches = buildBranches;
            BuildPullRequestForks = buildPullRequestForks;
            BuildPullRequestLabelsChanged = buildPullRequestLabelsChanged;
            BuildPullRequestReadyForReview = buildPullRequestReadyForReview;
            BuildPullRequests = buildPullRequests;
            BuildTags = buildTags;
            CancelDeletedBranchBuilds = cancelDeletedBranchBuilds;
            FilterCondition = filterCondition;
            FilterEnabled = filterEnabled;
            PrefixPullRequestForkBranchNames = prefixPullRequestForkBranchNames;
            PublishBlockedAsPending = publishBlockedAsPending;
            PublishCommitStatus = publishCommitStatus;
            PublishCommitStatusPerStep = publishCommitStatusPerStep;
            PullRequestBranchFilterConfiguration = pullRequestBranchFilterConfiguration;
            PullRequestBranchFilterEnabled = pullRequestBranchFilterEnabled;
            SeparatePullRequestStatuses = separatePullRequestStatuses;
            SkipBuildsForExistingCommits = skipBuildsForExistingCommits;
            SkipPullRequestBuildsForExistingCommits = skipPullRequestBuildsForExistingCommits;
            TriggerMode = triggerMode;
        }
    }
}
