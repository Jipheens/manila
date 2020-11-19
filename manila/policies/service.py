#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import versionutils
from oslo_policy import policy

from manila.policies import base


BASE_POLICY_NAME = 'service:%s'

DEPRECATED_REASON = """
The service API now supports system scope and default roles.
"""

deprecated_service_index = policy.DeprecatedRule(
    name=BASE_POLICY_NAME % 'index',
    check_str=base.RULE_ADMIN_API
)
deprecated_service_update = policy.DeprecatedRule(
    name=BASE_POLICY_NAME % 'update',
    check_str=base.RULE_ADMIN_API
)


service_policies = [
    policy.DocumentedRuleDefault(
        name=BASE_POLICY_NAME % 'index',
        check_str=base.SYSTEM_READER,
        scope_types=['system'],
        description="Return a list of all running services.",
        operations=[
            {
                'method': 'GET',
                'path': '/os-services',
            },
            {
                'method': 'GET',
                'path': '/os-services?{query}',
            },
            {
                'method': 'GET',
                'path': '/services',
            },
            {
                'method': 'GET',
                'path': '/services?{query}',
            }
        ],
        deprecated_rule=deprecated_service_index,
        deprecated_reason=DEPRECATED_REASON,
        deprecated_since=versionutils.deprecated.WALLABY
    ),
    policy.DocumentedRuleDefault(
        name=BASE_POLICY_NAME % 'update',
        check_str=base.SYSTEM_ADMIN,
        scope_types=['system'],
        description="Enable/Disable scheduling for a service.",
        operations=[
            {
                'method': 'PUT',
                'path': '/os-services/disable',
            },
            {
                'method': 'PUT',
                'path': '/os-services/enable',
            },
            {
                'method': 'PUT',
                'path': '/services/disable',
            },
            {
                'method': 'PUT',
                'path': '/services/enable',
            },
        ],
        deprecated_rule=deprecated_service_update,
        deprecated_reason=DEPRECATED_REASON,
        deprecated_since=versionutils.deprecated.WALLABY
    ),
]


def list_rules():
    return service_policies
