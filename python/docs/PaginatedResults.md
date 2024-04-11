# PaginatedResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.paginated_results import PaginatedResults

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResults from a JSON string
paginated_results_instance = PaginatedResults.from_json(json)
# print the JSON string representation of the object
print(PaginatedResults.to_json())

# convert the object into a dict
paginated_results_dict = paginated_results_instance.to_dict()
# create an instance of PaginatedResults from a dict
paginated_results_form_dict = paginated_results.from_dict(paginated_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


