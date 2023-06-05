// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export namespace Pipeline {
    export interface PipelineProviderSettings {
        /**
         * Whether to create builds when branches are pushed.
         */
        buildBranches?: pulumi.Input<boolean>;
        /**
         * Whether to create builds for pull requests from third-party forks.
         */
        buildPullRequestForks?: pulumi.Input<boolean>;
        /**
         * Whether to create builds for pull requests when labels are added or removed.
         */
        buildPullRequestLabelsChanged?: pulumi.Input<boolean>;
        buildPullRequestReadyForReview?: pulumi.Input<boolean>;
        /**
         * Whether to create builds for commits that are part of a Pull Request.
         */
        buildPullRequests?: pulumi.Input<boolean>;
        /**
         * Whether to create builds when tags are pushed.
         *
         * Properties available for Bitbucket Cloud, GitHub, and GitHub Enterprise:
         */
        buildTags?: pulumi.Input<boolean>;
        /**
         * A boolean to enable automatically cancelling any running builds for a branch if the branch is deleted.
         *
         * Additional properties available for GitHub:
         */
        cancelDeletedBranchBuilds?: pulumi.Input<boolean>;
        /**
         * The condition to evaluate when deciding if a build should run. More details available in [the documentation](https://buildkite.com/docs/pipelines/conditionals#conditionals-in-pipelines)
         */
        filterCondition?: pulumi.Input<string>;
        /**
         * [true/false] Whether to filter builds to only run when the condition in `filterCondition` is true
         */
        filterEnabled?: pulumi.Input<boolean>;
        /**
         * Prefix branch names for third-party fork builds to ensure they don't trigger branch conditions. For example, the `master` branch from `some-user` will become `some-user:master`.
         */
        prefixPullRequestForkBranchNames?: pulumi.Input<boolean>;
        /**
         * The status to use for blocked builds. Pending can be used with [required status checks](https://help.github.com/en/articles/enabling-required-status-checks) to prevent merging pull requests with blocked builds.
         */
        publishBlockedAsPending?: pulumi.Input<boolean>;
        /**
         * Whether to update the status of commits in Bitbucket or GitHub.
         */
        publishCommitStatus?: pulumi.Input<boolean>;
        /**
         * Whether to create a separate status for each job in a build, allowing you to see the status of each job directly in Bitbucket or GitHub.
         */
        publishCommitStatusPerStep?: pulumi.Input<boolean>;
        /**
         * The branch filtering pattern. Only pull requests on branches matching this pattern will cause builds to be created.
         */
        pullRequestBranchFilterConfiguration?: pulumi.Input<string>;
        /**
         * Whether to limit the creation of builds to specific branches or patterns.
         */
        pullRequestBranchFilterEnabled?: pulumi.Input<boolean>;
        /**
         * Whether to create a separate status for pull request builds, allowing you to require a passing pull request build in your [required status checks](https://help.github.com/en/articles/enabling-required-status-checks) in GitHub.
         */
        separatePullRequestStatuses?: pulumi.Input<boolean>;
        /**
         * Whether to skip creating a new build for a pull request if an existing build for the commit and branch already exists.
         */
        skipPullRequestBuildsForExistingCommits?: pulumi.Input<boolean>;
        /**
         * What type of event to trigger builds on. Must be one of:
         */
        triggerMode?: pulumi.Input<string>;
    }

    export interface PipelineTeam {
        /**
         * The level of access to grant. Must be one of `READ_ONLY`, `BUILD_AND_READ` or `MANAGE_BUILD_AND_READ`.
         */
        accessLevel: pulumi.Input<string>;
        /**
         * The buildkite slug of the team.
         */
        slug: pulumi.Input<string>;
    }
}
