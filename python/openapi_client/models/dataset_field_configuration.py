# coding: utf-8

"""
    Opendatasoft's Automation API Documentation

    Opendatasoft REST API to manage your portal and its catalog

    The version of the OpenAPI document: 1.0
    Contact: support@opendatasoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.annotate_dataset_field_configuration import AnnotateDatasetFieldConfiguration
    from openapi_client.models.delete_dataset_field_configuration import DeleteDatasetFieldConfiguration
    from openapi_client.models.description_dataset_field_configuration import DescriptionDatasetFieldConfiguration
    from openapi_client.models.order_dataset_field_configuration import OrderDatasetFieldConfiguration
    from openapi_client.models.rename_dataset_field_configuration import RenameDatasetFieldConfiguration
    from openapi_client.models.type_dataset_field_configuration import TypeDatasetFieldConfiguration

class DatasetFieldConfiguration(BaseModel):
    """
    Field attached to a dataset
    """ # noqa: E501
    uid: Optional[StrictStr] = Field(default=None, description="Unique identifier for the field configuration")
    type: Annotated[str, Field(min_length=1, strict=True)]
    label: StrictStr = Field(description="Friendly label of the field configuration")
    __properties: ClassVar[List[str]] = ["uid", "type", "label"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'annotate': 'AnnotateDatasetFieldConfiguration','delete': 'DeleteDatasetFieldConfiguration','description': 'DescriptionDatasetFieldConfiguration','order': 'OrderDatasetFieldConfiguration','rename': 'RenameDatasetFieldConfiguration','type': 'TypeDatasetFieldConfiguration'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AnnotateDatasetFieldConfiguration, DeleteDatasetFieldConfiguration, DescriptionDatasetFieldConfiguration, OrderDatasetFieldConfiguration, RenameDatasetFieldConfiguration, TypeDatasetFieldConfiguration]]:
        """Create an instance of DatasetFieldConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "uid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AnnotateDatasetFieldConfiguration, DeleteDatasetFieldConfiguration, DescriptionDatasetFieldConfiguration, OrderDatasetFieldConfiguration, RenameDatasetFieldConfiguration, TypeDatasetFieldConfiguration]]:
        """Create an instance of DatasetFieldConfiguration from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'annotate':
            return import_module("openapi_client.models.annotate_dataset_field_configuration").AnnotateDatasetFieldConfiguration.from_dict(obj)
        if object_type ==  'delete':
            return import_module("openapi_client.models.delete_dataset_field_configuration").DeleteDatasetFieldConfiguration.from_dict(obj)
        if object_type ==  'description':
            return import_module("openapi_client.models.description_dataset_field_configuration").DescriptionDatasetFieldConfiguration.from_dict(obj)
        if object_type ==  'order':
            return import_module("openapi_client.models.order_dataset_field_configuration").OrderDatasetFieldConfiguration.from_dict(obj)
        if object_type ==  'rename':
            return import_module("openapi_client.models.rename_dataset_field_configuration").RenameDatasetFieldConfiguration.from_dict(obj)
        if object_type ==  'type':
            return import_module("openapi_client.models.type_dataset_field_configuration").TypeDatasetFieldConfiguration.from_dict(obj)

        raise ValueError("DatasetFieldConfiguration failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


