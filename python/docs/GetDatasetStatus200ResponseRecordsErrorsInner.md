# GetDatasetStatus200ResponseRecordsErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** | Identifier of the record after processing | [optional] 
**field_uid** | **str** | Unique identifier of the field involved in the error | [optional] 
**processor_uid** | **str** | Unique identifier of the processor which generates the error | [optional] 
**message** | **str** | Human-readable error message | [optional] 

## Example

```python
from opendatasoft_automation.models.get_dataset_status200_response_records_errors_inner import GetDatasetStatus200ResponseRecordsErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetStatus200ResponseRecordsErrorsInner from a JSON string
get_dataset_status200_response_records_errors_inner_instance = GetDatasetStatus200ResponseRecordsErrorsInner.from_json(json)
# print the JSON string representation of the object
print(GetDatasetStatus200ResponseRecordsErrorsInner.to_json())

# convert the object into a dict
get_dataset_status200_response_records_errors_inner_dict = get_dataset_status200_response_records_errors_inner_instance.to_dict()
# create an instance of GetDatasetStatus200ResponseRecordsErrorsInner from a dict
get_dataset_status200_response_records_errors_inner_from_dict = GetDatasetStatus200ResponseRecordsErrorsInner.from_dict(get_dataset_status200_response_records_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


