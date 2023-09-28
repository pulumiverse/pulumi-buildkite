// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A test suite is a collection of tests. A run is to a suite what a build is to a Pipeline.Use this resource to manage [Test Suites](https://buildkite.com/docs/test-analytics) on Buildkite.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as buildkite from "@pulumiverse/buildkite";
 *
 * // create a test suite for the main repository
 * const main = new buildkite.testsuite.TestSuite("main", {
 *     defaultBranch: "main",
 *     teamOwnerId: "VGVhbvDf4eRef20tMzIxMGEfYTctNzEF5g00M8f5s6E2YjYtODNlOGNlZgD6HcBi",
 * });
 * ```
 */
export class TestSuite extends pulumi.CustomResource {
    /**
     * Get an existing TestSuite resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TestSuiteState, opts?: pulumi.CustomResourceOptions): TestSuite {
        return new TestSuite(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'buildkite:TestSuite/testSuite:TestSuite';

    /**
     * Returns true if the given object is an instance of TestSuite.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TestSuite {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TestSuite.__pulumiType;
    }

    /**
     * The API token to use to send test run data to the API.
     */
    public /*out*/ readonly apiToken!: pulumi.Output<string>;
    /**
     * The default branch for the repository this test suite is for.
     */
    public readonly defaultBranch!: pulumi.Output<string>;
    /**
     * The name to give the test suite.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The generated slug of the test suite.
     */
    public /*out*/ readonly slug!: pulumi.Output<string>;
    /**
     * The GraphQL ID of the team to mark as the owner/admin of the test suite.
     */
    public readonly teamOwnerId!: pulumi.Output<string>;
    /**
     * The UUID of the test suite.
     */
    public /*out*/ readonly uuid!: pulumi.Output<string>;

    /**
     * Create a TestSuite resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TestSuiteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TestSuiteArgs | TestSuiteState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TestSuiteState | undefined;
            resourceInputs["apiToken"] = state ? state.apiToken : undefined;
            resourceInputs["defaultBranch"] = state ? state.defaultBranch : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["slug"] = state ? state.slug : undefined;
            resourceInputs["teamOwnerId"] = state ? state.teamOwnerId : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
        } else {
            const args = argsOrState as TestSuiteArgs | undefined;
            if ((!args || args.defaultBranch === undefined) && !opts.urn) {
                throw new Error("Missing required property 'defaultBranch'");
            }
            if ((!args || args.teamOwnerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'teamOwnerId'");
            }
            resourceInputs["defaultBranch"] = args ? args.defaultBranch : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["teamOwnerId"] = args ? args.teamOwnerId : undefined;
            resourceInputs["apiToken"] = undefined /*out*/;
            resourceInputs["slug"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["apiToken"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(TestSuite.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TestSuite resources.
 */
export interface TestSuiteState {
    /**
     * The API token to use to send test run data to the API.
     */
    apiToken?: pulumi.Input<string>;
    /**
     * The default branch for the repository this test suite is for.
     */
    defaultBranch?: pulumi.Input<string>;
    /**
     * The name to give the test suite.
     */
    name?: pulumi.Input<string>;
    /**
     * The generated slug of the test suite.
     */
    slug?: pulumi.Input<string>;
    /**
     * The GraphQL ID of the team to mark as the owner/admin of the test suite.
     */
    teamOwnerId?: pulumi.Input<string>;
    /**
     * The UUID of the test suite.
     */
    uuid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TestSuite resource.
 */
export interface TestSuiteArgs {
    /**
     * The default branch for the repository this test suite is for.
     */
    defaultBranch: pulumi.Input<string>;
    /**
     * The name to give the test suite.
     */
    name?: pulumi.Input<string>;
    /**
     * The GraphQL ID of the team to mark as the owner/admin of the test suite.
     */
    teamOwnerId: pulumi.Input<string>;
}
