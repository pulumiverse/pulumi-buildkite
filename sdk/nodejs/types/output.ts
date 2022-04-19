// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface PipelineProviderSettings {
    /**
     * Whether to create builds when branches are pushed.
     */
    buildBranches: boolean;
    /**
     * Whether to create builds for pull requests from third-party forks.
     */
    buildPullRequestForks: boolean;
    /**
     * Whether to create builds for pull requests when labels are added or removed.
     */
    buildPullRequestLabelsChanged: boolean;
    buildPullRequestReadyForReview: boolean;
    /**
     * Whether to create builds for commits that are part of a Pull Request.
     */
    buildPullRequests: boolean;
    /**
     * Whether to create builds when tags are pushed.
     */
    buildTags: boolean;
    /**
     * A boolean to enable automatically cancelling any running builds for a branch if the branch is deleted.
     */
    cancelDeletedBranchBuilds: boolean;
    /**
     * The condition to evaluate when deciding if a build should run. More details available in [the documentation](https://buildkite.com/docs/pipelines/conditionals#conditionals-in-pipelines)
     */
    filterCondition: string;
    /**
     * [true/false] Whether to filter builds to only run when the condition in `filterCondition` is true
     */
    filterEnabled: boolean;
    /**
     * Prefix branch names for third-party fork builds to ensure they don't trigger branch conditions. For example, the `master` branch from `some-user` will become `some-user:master`.
     */
    prefixPullRequestForkBranchNames: boolean;
    /**
     * The status to use for blocked builds. Pending can be used with [required status checks](https://help.github.com/en/articles/enabling-required-status-checks) to prevent merging pull requests with blocked builds.
     */
    publishBlockedAsPending: boolean;
    /**
     * Whether to update the status of commits in Bitbucket or GitHub.
     */
    publishCommitStatus: boolean;
    /**
     * Whether to create a separate status for each job in a build, allowing you to see the status of each job directly in Bitbucket or GitHub.
     */
    publishCommitStatusPerStep: boolean;
    /**
     * The branch filtering pattern. Only pull requests on branches matching this pattern will cause builds to be created.
     */
    pullRequestBranchFilterConfiguration: string;
    /**
     * Whether to limit the creation of builds to specific branches or patterns.
     */
    pullRequestBranchFilterEnabled: boolean;
    /**
     * Whether to create a separate status for pull request builds, allowing you to require a passing pull request build in your [required status checks](https://help.github.com/en/articles/enabling-required-status-checks) in GitHub.
     */
    separatePullRequestStatuses: boolean;
    /**
     * Whether to skip creating a new build for a pull request if an existing build for the commit and branch already exists.
     */
    skipPullRequestBuildsForExistingCommits: boolean;
    /**
     * What type of event to trigger builds on. Must be one of:
     */
    triggerMode: string;
}

export interface PipelineTeam {
    /**
     * The level of access to grant. Must be one of `READ_ONLY`, `BUILD_AND_READ` or `MANAGE_BUILD_AND_READ`.
     */
    accessLevel: string;
    /**
     * The buildkite slug of the team.
     */
    slug: string;
}

