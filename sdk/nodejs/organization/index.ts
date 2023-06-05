// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetOrganizationArgs, GetOrganizationResult, GetOrganizationOutputArgs } from "./getOrganization";
export const getOrganization: typeof import("./getOrganization").getOrganization = null as any;
export const getOrganizationOutput: typeof import("./getOrganization").getOrganizationOutput = null as any;
utilities.lazyLoad(exports, ["getOrganization","getOrganizationOutput"], () => require("./getOrganization"));

export { SettingsArgs, SettingsState } from "./settings";
export type Settings = import("./settings").Settings;
export const Settings: typeof import("./settings").Settings = null as any;
utilities.lazyLoad(exports, ["Settings"], () => require("./settings"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "buildkite:Organization/settings:Settings":
                return new Settings(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("buildkite", "Organization/settings", _module)
