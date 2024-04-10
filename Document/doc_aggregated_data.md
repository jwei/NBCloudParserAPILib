# API Introduction
Gets the  run-time state of a virtual machine via Azure's API response of "Virtual Machine - Instance View". The data structure of "statuses" field is modified from original response for easier usage.

# Response Data Structure
Below are the Response Data Structure
|**Name**|**Data Type**|**Description**|
|------|------|------|
| computerName | string | The computer name assigned to the virtual machine. |
| status | object[] | xxx. |
| status.code | string | The status code. |
| status.displayStatus | string | The short localizable label for the status. |
| ... | ... | ... |