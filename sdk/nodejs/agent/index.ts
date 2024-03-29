// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { AgentTokenArgs, AgentTokenState } from "./agentToken";
export type AgentToken = import("./agentToken").AgentToken;
export const AgentToken: typeof import("./agentToken").AgentToken = null as any;
utilities.lazyLoad(exports, ["AgentToken"], () => require("./agentToken"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "buildkite:Agent/agentToken:AgentToken":
                return new AgentToken(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("buildkite", "Agent/agentToken", _module)
