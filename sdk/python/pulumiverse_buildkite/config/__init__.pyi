# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

apiToken: Optional[str]
"""
API token with GraphQL access and `write_pipelines, read_pipelines` and `write_suites` REST API scopes
"""

archivePipelineOnDelete: Optional[bool]
"""
Archive pipelines when destroying instead of completely deleting.
"""

graphqlUrl: Optional[str]
"""
Base URL for the GraphQL API to use
"""

organization: Optional[str]
"""
The Buildkite organization slug
"""

restUrl: Optional[str]
"""
Base URL for the REST API to use
"""

