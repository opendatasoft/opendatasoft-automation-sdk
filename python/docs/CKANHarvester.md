# CKANHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**limit** | **int** |  | [optional] [default to 5]
**offset** | **int** |  | [optional] [default to 3]
**sort** | **str** |  | [optional] [default to 'relevance desc']
**api_key** | **str** | The service API key. If it isn&#39;t blank, the API returns null to hide this sensitive value. | [optional] [default to '']
**group** | **str** |  | [optional] [default to 'education']
**language** | **str** |  | [optional] [default to '']
**query** | **str** |  | [optional] [default to '']
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from openapi_client.models.ckan_harvester import CKANHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of CKANHarvester from a JSON string
ckan_harvester_instance = CKANHarvester.from_json(json)
# print the JSON string representation of the object
print(CKANHarvester.to_json())

# convert the object into a dict
ckan_harvester_dict = ckan_harvester_instance.to_dict()
# create an instance of CKANHarvester from a dict
ckan_harvester_form_dict = ckan_harvester.from_dict(ckan_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


