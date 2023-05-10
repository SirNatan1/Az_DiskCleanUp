import os
import automationassets
from automationassets import AutomationAssetNotFound
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

# Read Azure subscription ID from environment variable
subscription_id = automationassets.get_automation_variable("AZURE_SUBSCRIPTION_ID")
resource_group = automationassets.get_automation_variable("RESOURCE_GROUP")
tag_key = <key>
tag_value = <value>

# Initialize Azure credentials
credential = DefaultAzureCredential()

# Initialize the Azure clients
compute_client = ComputeManagementClient(credential, subscription_id)
resource_client = ResourceManagementClient(credential, subscription_id)

# get all the managed and unmanaged disks in the subscription
disks = []
for disk in compute_client.disks.list():
    disks.append(disk)
for disk in compute_client.disks.list_by_resource_group(resource_group):
    disks.append(disk)

unattached_disks = []
for disk in disks:
    if disk.managed_by is None and disk.disk_state == 'Unattached':
        if (disk.tags and tag_key in disk.tags and disk.tags[tag_key] == tag_value) or not disk.tags:
            unattached_disks.append(disk)

for disk in unattached_disks:
    resource_client.resources.begin_delete_by_id(disk.id, api_version='2023-01-02')
    # print the name of the deleted disk
    print("Deleted disks:", disk.name)
