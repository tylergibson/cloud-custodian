# Copyright 2019 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from c7n_azure.provider import resources
from c7n_azure.resources.arm import ArmResourceManager


@resources.register('aks')
class KubernetesService(ArmResourceManager):
    """Azure Kubernetes Service Resource

    :example:
    Returns all aks clusters that did not provision successfully

    .. code-block:: yaml

        policies:
          - name: broken-aks
            resource: azure.aks
            filters:
              - type: value
                key: properties.provisioningState
                op: not-equal
                value_type: normalize
                value: succeeded


    """

    class resource_type(ArmResourceManager.resource_type):
        service = 'azure.mgmt.containerservice'
        client = 'ContainerServiceClient'
        enum_spec = ('managed_clusters', 'list', None)
        default_report_fields = (
            'name',
            'location',
            'resourceGroup'
        )
        resource_type = 'Microsoft.ContainerService/managedClusters'
