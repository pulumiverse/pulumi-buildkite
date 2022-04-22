import * as pulumi from "@pulumi/pulumi";
import * as buildkite from "@grapl/pulumi-buildkite";

new buildkite.Pipeline(
    "testing-pipeline-nodejs",
    {
        name: "testing-pipeline-nodejs",
        repository: "https://github.com/grapl-security/pulumi-buildkite",
        description: ":pulumi::buildkite::nodejs: A pipeline created to test the pulumi-buildkite provider",
        defaultBranch: "main",
        steps: `
        steps:
          - label: "Hello World"
            command: echo 'Hello World'
        `
    }
);
