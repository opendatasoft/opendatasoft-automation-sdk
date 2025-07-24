# DatasetMetadataAssetContentConfiguration

This template defines metadata for configuring how asset content are displayed in the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facets** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**fields_displayed_in_specific_languages** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**records_search_boosts** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.dataset_metadata_asset_content_configuration import DatasetMetadataAssetContentConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadataAssetContentConfiguration from a JSON string
dataset_metadata_asset_content_configuration_instance = DatasetMetadataAssetContentConfiguration.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadataAssetContentConfiguration.to_json())

# convert the object into a dict
dataset_metadata_asset_content_configuration_dict = dataset_metadata_asset_content_configuration_instance.to_dict()
# create an instance of DatasetMetadataAssetContentConfiguration from a dict
dataset_metadata_asset_content_configuration_from_dict = DatasetMetadataAssetContentConfiguration.from_dict(dataset_metadata_asset_content_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


