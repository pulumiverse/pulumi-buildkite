// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## # Resource: pipeline
 *
 * This resource allows you to create and manage pipelines for repositories.
 *
 * Buildkite Documentation: https://buildkite.com/docs/pipelines
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 * import * as fs from "fs";
 *
 * // in ./steps.yml:
 * // steps:
 * //   - label: ':pipeline:'
 * //     command: buildkite-agent pipeline upload
 * const repo2 = new buildkite.pipeline.Pipeline("repo2", {
 *     repository: "git@github.com:org/repo2",
 *     steps: fs.readFileSync("./steps.yml"),
 *     teams: [{
 *         slug: "everyone",
 *         accessLevel: "READ_ONLY",
 *     }],
 * });
 * ```
 * ### With Command Timeouts
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 * import * as fs from "fs";
 *
 * const testNew = new buildkite.pipeline.Pipeline("testNew", {
 *     repository: "https://github.com/buildkite/terraform-provider-buildkite.git",
 *     steps: fs.readFileSync("./deploy-steps.yml"),
 *     defaultTimeoutInMinutes: 60,
 *     maximumTimeoutInMinutes: 120,
 * });
 * ```
 *
 * Currently, the `defaultTimeoutInMinutes` and `maximumTimeoutInMinutes` will be retained in state even if removed from the configuration. In order to remove them, you must set them to `0` in either the configuration or the web UI.
 * ### With Deletion Protection
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 * import * as fs from "fs";
 *
 * const testNew = new buildkite.pipeline.Pipeline("testNew", {
 *     repository: "https://github.com/buildkite/terraform-provider-buildkite.git",
 *     steps: fs.readFileSync("./deploy-steps.yml"),
 *     deletionProtection: true,
 * });
 * ```
 *
 * `deletionProtection` will block `destroy` actions on the **pipeline**. Attached resources, such as `schedules` will still be destroyed.
 * ### With GitHub Provider Settings
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 * import * as fs from "fs";
 *
 * // Pipeline that should not be triggered from a GitHub webhook
 * const repo2_deploy = new buildkite.pipeline.Pipeline("repo2-deploy", {
 *     repository: "git@github.com:org/repo2",
 *     steps: fs.readFileSync("./deploy-steps.yml"),
 *     providerSettings: {
 *         triggerMode: "none",
 *     },
 * });
 * // Release pipeline (triggered only when tags are pushed)
 * const repo2_release = new buildkite.pipeline.Pipeline("repo2-release", {
 *     repository: "git@github.com:org/repo2",
 *     steps: fs.readFileSync("./release-steps.yml"),
 *     providerSettings: {
 *         buildBranches: false,
 *         buildTags: true,
 *         buildPullRequests: false,
 *         triggerMode: "code",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Pipelines can be imported using the `GraphQL ID` (not UUID), e.g.
 *
 * ```sh
 *  $ pulumi import buildkite:Pipeline/pipeline:Pipeline fleet UGlwZWxpbmUtLS00MzVjYWQ1OC1lODFkLTQ1YWYtODYzNy1iMWNmODA3MDIzOGQ=
 * ```
 */
export class Pipeline extends pulumi.CustomResource {
    /**
     * Get an existing Pipeline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PipelineState, opts?: pulumi.CustomResourceOptions): Pipeline {
        return new Pipeline(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'buildkite:Pipeline/pipeline:Pipeline';

    /**
     * Returns true if the given object is an instance of Pipeline.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Pipeline {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Pipeline.__pulumiType;
    }

    /**
     * A boolean on whether or not to allow rebuilds for the pipeline.
     */
    public readonly allowRebuilds!: pulumi.Output<boolean | undefined>;
    /**
     * The pipeline's last build status so you can display build status badge.
     */
    public /*out*/ readonly badgeUrl!: pulumi.Output<string>;
    /**
     * Limit which branches and tags cause new builds to be created, either via a code push or via the Builds REST API.
     */
    public readonly branchConfiguration!: pulumi.Output<string | undefined>;
    /**
     * A boolean to enable automatically cancelling any running builds on the same branch when a new build is created.
     */
    public readonly cancelIntermediateBuilds!: pulumi.Output<boolean | undefined>;
    /**
     * Limit which branches build cancelling applies to, for example !master will ensure that the master branch won't have its builds automatically cancelled.
     */
    public readonly cancelIntermediateBuildsBranchFilter!: pulumi.Output<string | undefined>;
    /**
     * The GraphQL ID of the cluster you want to use for the pipeline.
     */
    public readonly clusterId!: pulumi.Output<string | undefined>;
    /**
     * The default branch to prefill when new builds are created or triggered, usually main or master but can be anything.
     */
    public readonly defaultBranch!: pulumi.Output<string | undefined>;
    /**
     * The default timeout for commands in this pipeline, in minutes.
     */
    public readonly defaultTimeoutInMinutes!: pulumi.Output<number | undefined>;
    /**
     * Set to either `true` or `false`. When set to `true`, `destroy` actions on a pipeline will be blocked and fail with a message "Deletion protection is enabled for pipeline: <pipeline name>"
     */
    public readonly deletionProtection!: pulumi.Output<boolean | undefined>;
    /**
     * A description of the pipeline.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The maximum timeout for commands in this pipeline, in minutes.
     */
    public readonly maximumTimeoutInMinutes!: pulumi.Output<number | undefined>;
    /**
     * The name of the pipeline.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Source control provider settings for the pipeline. See Provider Settings Configuration below for details.
     */
    public readonly providerSettings!: pulumi.Output<outputs.Pipeline.PipelineProviderSettings>;
    /**
     * The git URL of the repository.
     */
    public readonly repository!: pulumi.Output<string>;
    /**
     * A boolean to enable automatically skipping any unstarted builds on the same branch when a new build is created.
     */
    public readonly skipIntermediateBuilds!: pulumi.Output<boolean | undefined>;
    /**
     * Limit which branches build skipping applies to, for example `!master` will ensure that the master branch won't have its builds automatically skipped.
     */
    public readonly skipIntermediateBuildsBranchFilter!: pulumi.Output<string | undefined>;
    /**
     * The buildkite slug of the team.
     */
    public /*out*/ readonly slug!: pulumi.Output<string>;
    /**
     * The string YAML steps to run the pipeline. Defaults to `buildkite-agent pipeline upload` if not specified.
     */
    public readonly steps!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * Set team access for the pipeline. Can be specified multiple times for each team. See Teams Configuration below for details.
     */
    public readonly teams!: pulumi.Output<outputs.Pipeline.PipelineTeam[] | undefined>;
    /**
     * The Buildkite webhook URL to configure on the repository to trigger builds on this pipeline.
     */
    public /*out*/ readonly webhookUrl!: pulumi.Output<string>;

    /**
     * Create a Pipeline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PipelineArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PipelineArgs | PipelineState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PipelineState | undefined;
            resourceInputs["allowRebuilds"] = state ? state.allowRebuilds : undefined;
            resourceInputs["badgeUrl"] = state ? state.badgeUrl : undefined;
            resourceInputs["branchConfiguration"] = state ? state.branchConfiguration : undefined;
            resourceInputs["cancelIntermediateBuilds"] = state ? state.cancelIntermediateBuilds : undefined;
            resourceInputs["cancelIntermediateBuildsBranchFilter"] = state ? state.cancelIntermediateBuildsBranchFilter : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["defaultBranch"] = state ? state.defaultBranch : undefined;
            resourceInputs["defaultTimeoutInMinutes"] = state ? state.defaultTimeoutInMinutes : undefined;
            resourceInputs["deletionProtection"] = state ? state.deletionProtection : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["maximumTimeoutInMinutes"] = state ? state.maximumTimeoutInMinutes : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["providerSettings"] = state ? state.providerSettings : undefined;
            resourceInputs["repository"] = state ? state.repository : undefined;
            resourceInputs["skipIntermediateBuilds"] = state ? state.skipIntermediateBuilds : undefined;
            resourceInputs["skipIntermediateBuildsBranchFilter"] = state ? state.skipIntermediateBuildsBranchFilter : undefined;
            resourceInputs["slug"] = state ? state.slug : undefined;
            resourceInputs["steps"] = state ? state.steps : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["teams"] = state ? state.teams : undefined;
            resourceInputs["webhookUrl"] = state ? state.webhookUrl : undefined;
        } else {
            const args = argsOrState as PipelineArgs | undefined;
            if ((!args || args.repository === undefined) && !opts.urn) {
                throw new Error("Missing required property 'repository'");
            }
            resourceInputs["allowRebuilds"] = args ? args.allowRebuilds : undefined;
            resourceInputs["branchConfiguration"] = args ? args.branchConfiguration : undefined;
            resourceInputs["cancelIntermediateBuilds"] = args ? args.cancelIntermediateBuilds : undefined;
            resourceInputs["cancelIntermediateBuildsBranchFilter"] = args ? args.cancelIntermediateBuildsBranchFilter : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["defaultBranch"] = args ? args.defaultBranch : undefined;
            resourceInputs["defaultTimeoutInMinutes"] = args ? args.defaultTimeoutInMinutes : undefined;
            resourceInputs["deletionProtection"] = args ? args.deletionProtection : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["maximumTimeoutInMinutes"] = args ? args.maximumTimeoutInMinutes : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["providerSettings"] = args ? args.providerSettings : undefined;
            resourceInputs["repository"] = args ? args.repository : undefined;
            resourceInputs["skipIntermediateBuilds"] = args ? args.skipIntermediateBuilds : undefined;
            resourceInputs["skipIntermediateBuildsBranchFilter"] = args ? args.skipIntermediateBuildsBranchFilter : undefined;
            resourceInputs["steps"] = args ? args.steps : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["teams"] = args ? args.teams : undefined;
            resourceInputs["badgeUrl"] = undefined /*out*/;
            resourceInputs["slug"] = undefined /*out*/;
            resourceInputs["webhookUrl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Pipeline.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Pipeline resources.
 */
export interface PipelineState {
    /**
     * A boolean on whether or not to allow rebuilds for the pipeline.
     */
    allowRebuilds?: pulumi.Input<boolean>;
    /**
     * The pipeline's last build status so you can display build status badge.
     */
    badgeUrl?: pulumi.Input<string>;
    /**
     * Limit which branches and tags cause new builds to be created, either via a code push or via the Builds REST API.
     */
    branchConfiguration?: pulumi.Input<string>;
    /**
     * A boolean to enable automatically cancelling any running builds on the same branch when a new build is created.
     */
    cancelIntermediateBuilds?: pulumi.Input<boolean>;
    /**
     * Limit which branches build cancelling applies to, for example !master will ensure that the master branch won't have its builds automatically cancelled.
     */
    cancelIntermediateBuildsBranchFilter?: pulumi.Input<string>;
    /**
     * The GraphQL ID of the cluster you want to use for the pipeline.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The default branch to prefill when new builds are created or triggered, usually main or master but can be anything.
     */
    defaultBranch?: pulumi.Input<string>;
    /**
     * The default timeout for commands in this pipeline, in minutes.
     */
    defaultTimeoutInMinutes?: pulumi.Input<number>;
    /**
     * Set to either `true` or `false`. When set to `true`, `destroy` actions on a pipeline will be blocked and fail with a message "Deletion protection is enabled for pipeline: <pipeline name>"
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * A description of the pipeline.
     */
    description?: pulumi.Input<string>;
    /**
     * The maximum timeout for commands in this pipeline, in minutes.
     */
    maximumTimeoutInMinutes?: pulumi.Input<number>;
    /**
     * The name of the pipeline.
     */
    name?: pulumi.Input<string>;
    /**
     * Source control provider settings for the pipeline. See Provider Settings Configuration below for details.
     */
    providerSettings?: pulumi.Input<inputs.Pipeline.PipelineProviderSettings>;
    /**
     * The git URL of the repository.
     */
    repository?: pulumi.Input<string>;
    /**
     * A boolean to enable automatically skipping any unstarted builds on the same branch when a new build is created.
     */
    skipIntermediateBuilds?: pulumi.Input<boolean>;
    /**
     * Limit which branches build skipping applies to, for example `!master` will ensure that the master branch won't have its builds automatically skipped.
     */
    skipIntermediateBuildsBranchFilter?: pulumi.Input<string>;
    /**
     * The buildkite slug of the team.
     */
    slug?: pulumi.Input<string>;
    /**
     * The string YAML steps to run the pipeline. Defaults to `buildkite-agent pipeline upload` if not specified.
     */
    steps?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Set team access for the pipeline. Can be specified multiple times for each team. See Teams Configuration below for details.
     */
    teams?: pulumi.Input<pulumi.Input<inputs.Pipeline.PipelineTeam>[]>;
    /**
     * The Buildkite webhook URL to configure on the repository to trigger builds on this pipeline.
     */
    webhookUrl?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Pipeline resource.
 */
export interface PipelineArgs {
    /**
     * A boolean on whether or not to allow rebuilds for the pipeline.
     */
    allowRebuilds?: pulumi.Input<boolean>;
    /**
     * Limit which branches and tags cause new builds to be created, either via a code push or via the Builds REST API.
     */
    branchConfiguration?: pulumi.Input<string>;
    /**
     * A boolean to enable automatically cancelling any running builds on the same branch when a new build is created.
     */
    cancelIntermediateBuilds?: pulumi.Input<boolean>;
    /**
     * Limit which branches build cancelling applies to, for example !master will ensure that the master branch won't have its builds automatically cancelled.
     */
    cancelIntermediateBuildsBranchFilter?: pulumi.Input<string>;
    /**
     * The GraphQL ID of the cluster you want to use for the pipeline.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The default branch to prefill when new builds are created or triggered, usually main or master but can be anything.
     */
    defaultBranch?: pulumi.Input<string>;
    /**
     * The default timeout for commands in this pipeline, in minutes.
     */
    defaultTimeoutInMinutes?: pulumi.Input<number>;
    /**
     * Set to either `true` or `false`. When set to `true`, `destroy` actions on a pipeline will be blocked and fail with a message "Deletion protection is enabled for pipeline: <pipeline name>"
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * A description of the pipeline.
     */
    description?: pulumi.Input<string>;
    /**
     * The maximum timeout for commands in this pipeline, in minutes.
     */
    maximumTimeoutInMinutes?: pulumi.Input<number>;
    /**
     * The name of the pipeline.
     */
    name?: pulumi.Input<string>;
    /**
     * Source control provider settings for the pipeline. See Provider Settings Configuration below for details.
     */
    providerSettings?: pulumi.Input<inputs.Pipeline.PipelineProviderSettings>;
    /**
     * The git URL of the repository.
     */
    repository: pulumi.Input<string>;
    /**
     * A boolean to enable automatically skipping any unstarted builds on the same branch when a new build is created.
     */
    skipIntermediateBuilds?: pulumi.Input<boolean>;
    /**
     * Limit which branches build skipping applies to, for example `!master` will ensure that the master branch won't have its builds automatically skipped.
     */
    skipIntermediateBuildsBranchFilter?: pulumi.Input<string>;
    /**
     * The string YAML steps to run the pipeline. Defaults to `buildkite-agent pipeline upload` if not specified.
     */
    steps?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Set team access for the pipeline. Can be specified multiple times for each team. See Teams Configuration below for details.
     */
    teams?: pulumi.Input<pulumi.Input<inputs.Pipeline.PipelineTeam>[]>;
}