# InlineObject5RecordsErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** | Identifier of the record after processing | [optional] 
**field_uid** | **str** | Unique identifier of the field involved in the error | [optional] 
**processor_uid** | **str** | Unique identifier of the processor which generates the error | [optional] 
**message** | **str** | Human-readable error message | [optional] 

## Example

```python
from opendatasoft_automation.models.inline_object5_records_errors_inner import InlineObject5RecordsErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject5RecordsErrorsInner from a JSON string
inline_object5_records_errors_inner_instance = InlineObject5RecordsErrorsInner.from_json(json)
# print the JSON string representation of the object
print(InlineObject5RecordsErrorsInner.to_json())

# convert the object into a dict
inline_object5_records_errors_inner_dict = inline_object5_records_errors_inner_instance.to_dict()
# create an instance of InlineObject5RecordsErrorsInner from a dict
inline_object5_records_errors_inner_from_dict = InlineObject5RecordsErrorsInner.from_dict(inline_object5_records_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


