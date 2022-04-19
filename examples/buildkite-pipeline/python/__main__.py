import pulumi
import pulumi_buildkite as buildkite

def main() -> None:
    buildkite.Pipeline(
        "testing-pipeline-python",
        name="testing-pipeline-python",
        repository="https://github.com/grapl-security/pulumi-buildkite",
        description=":pulumi::buildkite::python: A pipeline created to test the pulumi-buildkite provider",
        default_branch="main",
        steps="""
        steps:
          - label: "Hello World"
            command: echo 'Hello World'
        """
    )

if __name__ == "__main__":
    main()
