# DiskCleanUp in Azure by using Azure automate runbook
In order to minimize costs, we delete disks that are in an "unattached" state, this script helps us
automate this process by utillizing Azure runbook automations.

## Installation
- in the Azure Automation account go to Python packages and add the following dependencies: azure_mgmt_core, azure_mgmt_resource, azure_mgmt_compute,
azure_core, azure_identity, msal, typing_extension
- Add the following ENV var in the variables section: AZURE_SUBSCRIPTION_ID, RESOURCE_GROUP
- Make sure that the automation account has a contributor role permission.
- Copy the code in main.py and change the <key> and <value> to the needed key and values or leave it empty in order for the script to delete the disk.

## Usage
Once the code is published you can run the code at any time or create a job that will do it by scheduled time
