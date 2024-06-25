# AnnotateDatasetFieldConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The technical identifier of the field whose annotation you want to configure | 
**annotation** | **str** | Annotations are a mean to configure special behavior for the fields.  Some annotations are only available for certain field types. Setting the facet annotation on a field unlocks other annotations for the field. | Annotation name     | Field type                                   | Description                                                                                                                                                                                     | |---------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | id                  | all field types                              | Whether this field should constitute one of the keys of the records unique IDs. If no field has this annotation, all fields contribute to the creation of the records unique ID.                | | facet               | &#x60;date&#x60;, &#x60;datetime&#x60;, &#x60;int&#x60;, &#x60;decimal&#x60;, &#x60;text&#x60; | Whether the field can serve as a filter                                                                                                                                                         | | facetsort           | all field types, facet only                  | How to sort the facets. Possible arguments are &#x60;count&#x60; and &#x60;-count&#x60; for all field types, &#x60;alphanum&#x60; and &#x60;-alphanum&#x60; for &#x60;date&#x60;, &#x60;datetime&#x60; and &#x60;text&#x60;, &#x60;num&#x60; and &#x60;-num&#x60; for &#x60;decimal&#x60; and &#x60;int&#x60; | | disjunctive         | &#x60;decimal&#x60;, &#x60;int&#x60; and &#x60;text&#x60;, facet only      | Whether multiple values can be selected for the facet                                                                                                                                           | | timeserie_precision | &#x60;date&#x60; and &#x60;datetime&#x60;                        | display precision of the field. Possible arguments are &#x60;year&#x60;, &#x60;month&#x60; and &#x60;day&#x60; for &#x60;date&#x60;, &#x60;hour&#x60; and &#x60;minute&#x60; for &#x60;datetime&#x60;                                                                 | | timerangeFilter     | &#x60;date&#x60; and &#x60;datetime&#x60;, facet only            | Whether to activate the timerange filter                                                                                                                                                        | | unit                | &#x60;int&#x60; and &#x60;decimal&#x60;                          | The unit of the field                                                                                                                                                                           | | decimals            | &#x60;decimal&#x60;                                    | The argument is the number of digits to appear after the decimal point                                                                                                                          | | sortable            | &#x60;text&#x60;                                       | whether the field should be sortable in table view                                                                                                                                              | | multivalued         | &#x60;text&#x60;                                       | whether the field contains multiple values separated by a character. The separator must be given as the argument                                                                                | | hierarchical        | &#x60;text&#x60;, facet only                           | whether the field is hierarchical. The separator must be given as the argument                                                                                                                  | | 
**args** | [**List[AnnotateDatasetFieldConfiguration1Args]**](AnnotateDatasetFieldConfiguration1Args.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.annotate_dataset_field_configuration import AnnotateDatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotateDatasetFieldConfiguration from a JSON string
annotate_dataset_field_configuration_instance = AnnotateDatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(AnnotateDatasetFieldConfiguration.to_json())

# convert the object into a dict
annotate_dataset_field_configuration_dict = annotate_dataset_field_configuration_instance.to_dict()
# create an instance of AnnotateDatasetFieldConfiguration from a dict
annotate_dataset_field_configuration_from_dict = AnnotateDatasetFieldConfiguration.from_dict(annotate_dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


