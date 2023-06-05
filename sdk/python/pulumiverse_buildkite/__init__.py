# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .get_meta import *
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumiverse_buildkite.agent as __agent
    agent = __agent
    import pulumiverse_buildkite.config as __config
    config = __config
    import pulumiverse_buildkite.organization as __organization
    organization = __organization
    import pulumiverse_buildkite.pipeline as __pipeline
    pipeline = __pipeline
    import pulumiverse_buildkite.team as __team
    team = __team
else:
    agent = _utilities.lazy_import('pulumiverse_buildkite.agent')
    config = _utilities.lazy_import('pulumiverse_buildkite.config')
    organization = _utilities.lazy_import('pulumiverse_buildkite.organization')
    pipeline = _utilities.lazy_import('pulumiverse_buildkite.pipeline')
    team = _utilities.lazy_import('pulumiverse_buildkite.team')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "buildkite",
  "mod": "Agent/agentToken",
  "fqn": "pulumiverse_buildkite.agent",
  "classes": {
   "buildkite:Agent/agentToken:AgentToken": "AgentToken"
  }
 },
 {
  "pkg": "buildkite",
  "mod": "Organization/settings",
  "fqn": "pulumiverse_buildkite.organization",
  "classes": {
   "buildkite:Organization/settings:Settings": "Settings"
  }
 },
 {
  "pkg": "buildkite",
  "mod": "Pipeline/pipeline",
  "fqn": "pulumiverse_buildkite.pipeline",
  "classes": {
   "buildkite:Pipeline/pipeline:Pipeline": "Pipeline"
  }
 },
 {
  "pkg": "buildkite",
  "mod": "Pipeline/schedule",
  "fqn": "pulumiverse_buildkite.pipeline",
  "classes": {
   "buildkite:Pipeline/schedule:Schedule": "Schedule"
  }
 },
 {
  "pkg": "buildkite",
  "mod": "Team/member",
  "fqn": "pulumiverse_buildkite.team",
  "classes": {
   "buildkite:Team/member:Member": "Member"
  }
 },
 {
  "pkg": "buildkite",
  "mod": "Team/team",
  "fqn": "pulumiverse_buildkite.team",
  "classes": {
   "buildkite:Team/team:Team": "Team"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "buildkite",
  "token": "pulumi:providers:buildkite",
  "fqn": "pulumiverse_buildkite",
  "class": "Provider"
 }
]
"""
)