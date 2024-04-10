# QuandlHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_code** | **str** |  | 
**api_key** | **str** | The API key for the Quandl service. The API returns null to hide this sensitive value. | 
**number_of_datasets** | **int** |  | 
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from openapi_client.models.quandl_harvester import QuandlHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of QuandlHarvester from a JSON string
quandl_harvester_instance = QuandlHarvester.from_json(json)
# print the JSON string representation of the object
print(QuandlHarvester.to_json())

# convert the object into a dict
quandl_harvester_dict = quandl_harvester_instance.to_dict()
# create an instance of QuandlHarvester from a dict
quandl_harvester_form_dict = quandl_harvester.from_dict(quandl_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


