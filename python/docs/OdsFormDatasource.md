# OdsFormDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_uid** | **str** |  | [optional] 
**domain_id** | **str** |  | [optional] 
**status_to_extract** | **List[str]** |  | [optional] 
**is_available** | **bool** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.ods_form_datasource import OdsFormDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of OdsFormDatasource from a JSON string
ods_form_datasource_instance = OdsFormDatasource.from_json(json)
# print the JSON string representation of the object
print(OdsFormDatasource.to_json())

# convert the object into a dict
ods_form_datasource_dict = ods_form_datasource_instance.to_dict()
# create an instance of OdsFormDatasource from a dict
ods_form_datasource_from_dict = OdsFormDatasource.from_dict(ods_form_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


