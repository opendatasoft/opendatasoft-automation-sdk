# GetDatasetStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**since** | **datetime** | Date when the dataset entered the current status | [optional] 
**is_published** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**records_errors** | [**List[GetDatasetStatus200ResponseRecordsErrorsInner]**](GetDatasetStatus200ResponseRecordsErrorsInner.md) | The record error describes errors which occurred during the processing. An error comes from: - a processor: when a value is invalid or an operation failed - a type conversion: when a value cannot be converted. For example the string \&quot;s\&quot; converted to an integer. | [optional] 
**params** | **object** | Status-dependent additional information. For example, if &#x60;status&#x60; is &#x60;limit reached&#x60;, this will contain an &#x60;error&#x60; object that contains a &#x60;limit_type&#x60;, a &#x60;limit&#x60; and a &#x60;value&#x60;. | [optional] 

## Example

```python
from opendatasoft_automation.models.get_dataset_status200_response import GetDatasetStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetStatus200Response from a JSON string
get_dataset_status200_response_instance = GetDatasetStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetDatasetStatus200Response.to_json())

# convert the object into a dict
get_dataset_status200_response_dict = get_dataset_status200_response_instance.to_dict()
# create an instance of GetDatasetStatus200Response from a dict
get_dataset_status200_response_from_dict = GetDatasetStatus200Response.from_dict(get_dataset_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


