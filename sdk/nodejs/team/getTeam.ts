// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve a team by slug or id. You can find out more about teams in the Buildkite
 * [documentation](https://buildkite.com/docs/pipelines/permissions).
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumi/buildkite";
 *
 * const teamDev = buildkite.Team.getTeam({
 *     id: buildkite_team.team_dev.id,
 * });
 * const team = buildkite.Team.getTeam({
 *     slug: "Everyone",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getTeam(args?: GetTeamArgs, opts?: pulumi.InvokeOptions): Promise<GetTeamResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("buildkite:Team/getTeam:getTeam", {
        "id": args.id,
        "slug": args.slug,
    }, opts);
}

/**
 * A collection of arguments for invoking getTeam.
 */
export interface GetTeamArgs {
    /**
     * The GraphQL ID of the team to find.
     */
    id?: string;
    /**
     * The slug of the team to find.
     */
    slug?: string;
}

/**
 * A collection of values returned by getTeam.
 */
export interface GetTeamResult {
    /**
     * The default member role of the team.
     */
    readonly defaultMemberRole: string;
    /**
     * Whether the team is the default team.
     */
    readonly defaultTeam: boolean;
    /**
     * The description of the team.
     */
    readonly description: string;
    /**
     * The GraphQL ID of the team to find.
     */
    readonly id: string;
    /**
     * Whether members can create pipelines.
     */
    readonly membersCanCreatePipelines: boolean;
    /**
     * The name of the team.
     */
    readonly name: string;
    /**
     * The privacy setting of the team.
     */
    readonly privacy: string;
    /**
     * The slug of the team to find.
     */
    readonly slug: string;
    /**
     * The UUID of the team.
     */
    readonly uuid: string;
}
/**
 * Use this data source to retrieve a team by slug or id. You can find out more about teams in the Buildkite
 * [documentation](https://buildkite.com/docs/pipelines/permissions).
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumi/buildkite";
 *
 * const teamDev = buildkite.Team.getTeam({
 *     id: buildkite_team.team_dev.id,
 * });
 * const team = buildkite.Team.getTeam({
 *     slug: "Everyone",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getTeamOutput(args?: GetTeamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTeamResult> {
    return pulumi.output(args).apply((a: any) => getTeam(a, opts))
}

/**
 * A collection of arguments for invoking getTeam.
 */
export interface GetTeamOutputArgs {
    /**
     * The GraphQL ID of the team to find.
     */
    id?: pulumi.Input<string>;
    /**
     * The slug of the team to find.
     */
    slug?: pulumi.Input<string>;
}
