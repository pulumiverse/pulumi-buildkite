// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ## # Data Source: organization
 *
 * Use this data source to look up the organization settings. It currently supports
 * allowed_api_ip_addresses.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as buildkite from "@pulumi/buildkite";
 *
 * const testkite = buildkite.Organization.getOrganization({});
 * const fromBuildkite = new aws.ec2.SecurityGroup("fromBuildkite", {ingress: [{
 *     fromPort: "*",
 *     toPort: 443,
 *     protocol: "tcp",
 *     cidrBlocks: data.buildkite_organization.allowed_api_ip_addresses,
 * }]});
 * ```
 */
export function getOrganization(args?: GetOrganizationArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("buildkite:Organization/getOrganization:getOrganization", {
        "allowedApiIpAddresses": args.allowedApiIpAddresses,
    }, opts);
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationArgs {
    /**
     * list of IP addresses in CIDR format that are allowed to access the Buildkite API.
     */
    allowedApiIpAddresses?: string[];
}

/**
 * A collection of values returned by getOrganization.
 */
export interface GetOrganizationResult {
    /**
     * list of IP addresses in CIDR format that are allowed to access the Buildkite API.
     */
    readonly allowedApiIpAddresses?: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly uuid: string;
}
/**
 * ## # Data Source: organization
 *
 * Use this data source to look up the organization settings. It currently supports
 * allowed_api_ip_addresses.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as buildkite from "@pulumi/buildkite";
 *
 * const testkite = buildkite.Organization.getOrganization({});
 * const fromBuildkite = new aws.ec2.SecurityGroup("fromBuildkite", {ingress: [{
 *     fromPort: "*",
 *     toPort: 443,
 *     protocol: "tcp",
 *     cidrBlocks: data.buildkite_organization.allowed_api_ip_addresses,
 * }]});
 * ```
 */
export function getOrganizationOutput(args?: GetOrganizationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationResult> {
    return pulumi.output(args).apply((a: any) => getOrganization(a, opts))
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationOutputArgs {
    /**
     * list of IP addresses in CIDR format that are allowed to access the Buildkite API.
     */
    allowedApiIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
}
