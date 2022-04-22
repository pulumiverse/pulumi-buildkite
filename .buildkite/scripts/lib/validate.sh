#!/usr/bin/env bash

# Assert that the desired HCP plugin binary exists in
# '${PULUMI_HOME}/plugins'.
function validate_plugin {
    _version="${1}"

    echo "--- :pulumi: Contents of \$PULUMI_HOME (${PULUMI_HOME}) plugin directory"
    ls -alh "${PULUMI_HOME}/plugins"

    echo "--- :white_check_mark: Confirming installed plugin version is '${_version}'"
    installed_version="$("${PULUMI_HOME}/plugins/resource-hcp-${_version}/pulumi-resource-hcp" -version)"
    readonly installed_version

    if [ "${installed_version}" != "${_version}" ]; then
        echo "--- :rotating_light: Version mismatch! Expected '${_version}' but got '${installed_version}'"
        exit 1
    fi
}
