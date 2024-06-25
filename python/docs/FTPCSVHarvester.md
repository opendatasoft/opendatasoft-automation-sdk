# FTPCSVHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**user** | **str** |  | 
**password** | **str** | The password for the user. The API returns null to hide this sensitive value. | 
**directory** | **str** |  | [optional] [default to '']
**metadata_file** | **str** |  | 
**metadata_join_key** | **str** |  | [optional] [default to 'source_dataset']
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.ftpcsv_harvester import FTPCSVHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of FTPCSVHarvester from a JSON string
ftpcsv_harvester_instance = FTPCSVHarvester.from_json(json)
# print the JSON string representation of the object
print(FTPCSVHarvester.to_json())

# convert the object into a dict
ftpcsv_harvester_dict = ftpcsv_harvester_instance.to_dict()
# create an instance of FTPCSVHarvester from a dict
ftpcsv_harvester_from_dict = FTPCSVHarvester.from_dict(ftpcsv_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


