# FTPHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**user** | **str** |  | 
**password** | **str** | The password for the user. The API returns null to hide this sensitive value. | 
**directory** | **str** |  | [optional] [default to '']
**meta** | **str** |  | [optional] [default to '']
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.ftp_harvester import FTPHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of FTPHarvester from a JSON string
ftp_harvester_instance = FTPHarvester.from_json(json)
# print the JSON string representation of the object
print(FTPHarvester.to_json())

# convert the object into a dict
ftp_harvester_dict = ftp_harvester_instance.to_dict()
# create an instance of FTPHarvester from a dict
ftp_harvester_from_dict = FTPHarvester.from_dict(ftp_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


