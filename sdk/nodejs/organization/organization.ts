// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ## # Resource: organization
 *
 * This resource allows you to manage the settings for an organization.
 *
 * You must be an organization administrator to manage organization settings.
 *
 * Note: The "Allowed API IP Addresses" feature must be enabled on your organization in order to manage the `allowedApiIpAddresses` attribute.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 *
 * const testSettings = new buildkite.organization.Organization("testSettings", {allowedApiIpAddresses: ["1.1.1.1/32"]});
 * ```
 *
 * ## Import
 *
 * Organization settings can be imported by passing the organization slug to the import command, along with the identifier of the resource.
 *
 * ```sh
 *  $ pulumi import buildkite:Organization/organization:Organization test_settings test_org
 * ```
 *
 *  Your organization's slug can be found in your organisation's [settings](https://buildkite.com/organizations/~/settings) page.
 */
export class Organization extends pulumi.CustomResource {
    /**
     * Get an existing Organization resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationState, opts?: pulumi.CustomResourceOptions): Organization {
        return new Organization(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'buildkite:Organization/organization:Organization';

    /**
     * Returns true if the given object is an instance of Organization.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Organization {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Organization.__pulumiType;
    }

    /**
     * A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
     */
    public readonly allowedApiIpAddresses!: pulumi.Output<string[] | undefined>;
    public /*out*/ readonly uuid!: pulumi.Output<string>;

    /**
     * Create a Organization resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OrganizationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrganizationArgs | OrganizationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OrganizationState | undefined;
            resourceInputs["allowedApiIpAddresses"] = state ? state.allowedApiIpAddresses : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
        } else {
            const args = argsOrState as OrganizationArgs | undefined;
            resourceInputs["allowedApiIpAddresses"] = args ? args.allowedApiIpAddresses : undefined;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Organization.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Organization resources.
 */
export interface OrganizationState {
    /**
     * A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
     */
    allowedApiIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    uuid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Organization resource.
 */
export interface OrganizationArgs {
    /**
     * A list of IP addresses in CIDR format that are allowed to access the Buildkite API. If not set, all IP addresses are allowed (the same as setting 0.0.0.0/0).
     */
    allowedApiIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
}
