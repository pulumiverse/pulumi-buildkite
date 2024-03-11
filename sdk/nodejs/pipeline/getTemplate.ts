// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve a pipeline template by its ID or name.
 *
 * More information on pipeline templates can be found in the [documentation](https://buildkite.com/docs/pipelines/templates).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumi/buildkite";
 * import * as buildkite from "@pulumiverse/buildkite";
 *
 * const repository = "git@github.com:my-org/my-repo.git";
 * const devTemplate = buildkite.Pipeline.getTemplate({
 *     id: buildkite_pipeline_template.template_dev.id,
 * });
 * const frontendTemplate = buildkite.Pipeline.getTemplate({
 *     name: "Frontend app template",
 * });
 * const apiv2Dev = new buildkite.pipeline.Pipeline("apiv2Dev", {
 *     repository: repository,
 *     pipelineTemplateId: devTemplate.then(devTemplate => devTemplate.id),
 * });
 * const frontend = new buildkite.pipeline.Pipeline("frontend", {
 *     repository: repository,
 *     pipelineTemplateId: frontendTemplate.then(frontendTemplate => frontendTemplate.id),
 * });
 * ```
 */
export function getTemplate(args?: GetTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetTemplateResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("buildkite:Pipeline/getTemplate:getTemplate", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getTemplate.
 */
export interface GetTemplateArgs {
    /**
     * The GraphQL ID of the pipeline template.
     */
    id?: string;
    /**
     * The name of the pipeline template.
     */
    name?: string;
}

/**
 * A collection of values returned by getTemplate.
 */
export interface GetTemplateResult {
    /**
     * If the pipeline template is available for assignment by non admin users.
     */
    readonly available: boolean;
    /**
     * The YAML step configuration for the pipeline template.
     */
    readonly configuration: string;
    /**
     * The description for the pipeline template.
     */
    readonly description: string;
    /**
     * The GraphQL ID of the pipeline template.
     */
    readonly id: string;
    /**
     * The name of the pipeline template.
     */
    readonly name: string;
    /**
     * The UUID of the pipeline template.
     */
    readonly uuid: string;
}
/**
 * Use this data source to retrieve a pipeline template by its ID or name.
 *
 * More information on pipeline templates can be found in the [documentation](https://buildkite.com/docs/pipelines/templates).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumi/buildkite";
 * import * as buildkite from "@pulumiverse/buildkite";
 *
 * const repository = "git@github.com:my-org/my-repo.git";
 * const devTemplate = buildkite.Pipeline.getTemplate({
 *     id: buildkite_pipeline_template.template_dev.id,
 * });
 * const frontendTemplate = buildkite.Pipeline.getTemplate({
 *     name: "Frontend app template",
 * });
 * const apiv2Dev = new buildkite.pipeline.Pipeline("apiv2Dev", {
 *     repository: repository,
 *     pipelineTemplateId: devTemplate.then(devTemplate => devTemplate.id),
 * });
 * const frontend = new buildkite.pipeline.Pipeline("frontend", {
 *     repository: repository,
 *     pipelineTemplateId: frontendTemplate.then(frontendTemplate => frontendTemplate.id),
 * });
 * ```
 */
export function getTemplateOutput(args?: GetTemplateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTemplateResult> {
    return pulumi.output(args).apply((a: any) => getTemplate(a, opts))
}

/**
 * A collection of arguments for invoking getTemplate.
 */
export interface GetTemplateOutputArgs {
    /**
     * The GraphQL ID of the pipeline template.
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the pipeline template.
     */
    name?: pulumi.Input<string>;
}