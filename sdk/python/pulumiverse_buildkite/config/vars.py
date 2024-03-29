# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

import types

__config__ = pulumi.Config('buildkite')


class _ExportableConfig(types.ModuleType):
    @property
    def api_token(self) -> Optional[str]:
        return __config__.get('apiToken')

    @property
    def archive_pipeline_on_delete(self) -> Optional[bool]:
        """
        Enable this to archive pipelines when destroying the resource. This is opposed to completely deleting pipelines.
        """
        return __config__.get_bool('archivePipelineOnDelete')

    @property
    def graphql_url(self) -> Optional[str]:
        """
        Base URL for the GraphQL API to use. If not provided, the value is taken from the `BUILDKITE_GRAPHQL_URL` environment
        variable.
        """
        return __config__.get('graphqlUrl')

    @property
    def organization(self) -> Optional[str]:
        """
        The Buildkite organization slug. This can be found on the [settings](https://buildkite.com/organizations/~/settings)
        page. If not provided, the value is taken from the `BUILDKITE_ORGANIZATION_SLUG` environment variable.
        """
        return __config__.get('organization')

    @property
    def rest_url(self) -> Optional[str]:
        """
        Base URL for the REST API to use. If not provided, the value is taken from the `BUILDKITE_REST_URL` environment
        variable.
        """
        return __config__.get('restUrl')

    @property
    def timeouts(self) -> Optional[str]:
        return __config__.get('timeouts')

