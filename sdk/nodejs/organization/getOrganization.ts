// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to look up the organization settings.
 */
export function getOrganization(opts?: pulumi.InvokeOptions): Promise<GetOrganizationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("buildkite:Organization/getOrganization:getOrganization", {
    }, opts);
}

/**
 * A collection of values returned by getOrganization.
 */
export interface GetOrganizationResult {
    /**
     * List of IP addresses in CIDR format that are allowed to access the Buildkite API for this organization.
     */
    readonly allowedApiIpAddresses: string[];
    /**
     * The GraphQL ID of the organization.
     */
    readonly id: string;
    /**
     * The UUID of the organization.
     */
    readonly uuid: string;
}
/**
 * Use this data source to look up the organization settings.
 */
export function getOrganizationOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationResult> {
    return pulumi.output(getOrganization(opts))
}
