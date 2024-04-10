# DatasetMetadataVisualization

This set of metadata is used to configure the dataset visualizations on your portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyze_disabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**analyze_default** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**table_fields** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**table_default_sort_field** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**table_default_sort_direction** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_disabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_marker_picto** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_marker_color** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_marker_hidemarkershape** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_title** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_fields** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_disabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_html_enabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_html** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_sort_field** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_tooltip_sort_direction** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**map_basemap** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**images_disabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**media_gallery_fields** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**image_title** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**image_fields** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**image_tooltip_html_enabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**image_tooltip_html** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_enabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_event_title** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_event_start** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_event_end** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_tooltip_html_enabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_tooltip_html** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_tooltip_fields** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_event_color** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_available_views** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**calendar_default_view** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**custom_view_enabled** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**custom_view_html** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**custom_view_css** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**custom_view_icon** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**custom_view_title** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**custom_view_slug** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.dataset_metadata_visualization import DatasetMetadataVisualization

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadataVisualization from a JSON string
dataset_metadata_visualization_instance = DatasetMetadataVisualization.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadataVisualization.to_json())

# convert the object into a dict
dataset_metadata_visualization_dict = dataset_metadata_visualization_instance.to_dict()
# create an instance of DatasetMetadataVisualization from a dict
dataset_metadata_visualization_form_dict = dataset_metadata_visualization.from_dict(dataset_metadata_visualization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


