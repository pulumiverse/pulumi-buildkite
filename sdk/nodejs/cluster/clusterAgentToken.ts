// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ## # Resource: clusterAgentToken
 *
 * This resource allows you to create and manage cluster agent tokens.
 *
 * Buildkite Documentation: https://buildkite.com/docs/clusters/manage-clusters#set-up-clusters-connect-agents-to-a-cluster
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 *
 * const cluster_token_1 = new buildkite.cluster.ClusterAgentToken("cluster-token-1", {
 *     clusterId: "Q2x1c3Rlci0tLTkyMmVjOTA4LWRmNWItNDhhYS1hMThjLTczMzE0YjQ1ZGYyMA==",
 *     description: "agent token for cluster-1",
 * });
 * ```
 */
export class ClusterAgentToken extends pulumi.CustomResource {
    /**
     * Get an existing ClusterAgentToken resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterAgentTokenState, opts?: pulumi.CustomResourceOptions): ClusterAgentToken {
        return new ClusterAgentToken(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'buildkite:Cluster/clusterAgentToken:ClusterAgentToken';

    /**
     * Returns true if the given object is an instance of ClusterAgentToken.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterAgentToken {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterAgentToken.__pulumiType;
    }

    /**
     * The ID of the cluster that this cluster queue belongs to.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The UUID of the cluster that this cluster queue belongs to.
     */
    public /*out*/ readonly clusterUuid!: pulumi.Output<string>;
    /**
     * A description about what this cluster agent token is used for.
     */
    public readonly description!: pulumi.Output<string>;
    public /*out*/ readonly token!: pulumi.Output<string>;
    /**
     * The UUID of the created cluster queue.
     */
    public /*out*/ readonly uuid!: pulumi.Output<string>;

    /**
     * Create a ClusterAgentToken resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterAgentTokenArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterAgentTokenArgs | ClusterAgentTokenState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ClusterAgentTokenState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["clusterUuid"] = state ? state.clusterUuid : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["token"] = state ? state.token : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
        } else {
            const args = argsOrState as ClusterAgentTokenArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["clusterUuid"] = undefined /*out*/;
            resourceInputs["token"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["token"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(ClusterAgentToken.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ClusterAgentToken resources.
 */
export interface ClusterAgentTokenState {
    /**
     * The ID of the cluster that this cluster queue belongs to.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The UUID of the cluster that this cluster queue belongs to.
     */
    clusterUuid?: pulumi.Input<string>;
    /**
     * A description about what this cluster agent token is used for.
     */
    description?: pulumi.Input<string>;
    token?: pulumi.Input<string>;
    /**
     * The UUID of the created cluster queue.
     */
    uuid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ClusterAgentToken resource.
 */
export interface ClusterAgentTokenArgs {
    /**
     * The ID of the cluster that this cluster queue belongs to.
     */
    clusterId: pulumi.Input<string>;
    /**
     * A description about what this cluster agent token is used for.
     */
    description: pulumi.Input<string>;
}
