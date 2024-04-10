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

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from openapi_client.models.dataset_field_configuration import DatasetFieldConfiguration
from typing import Optional, Set
from typing_extensions import Self

class RenameDatasetFieldConfiguration(DatasetFieldConfiguration):
    """
    RenameDatasetFieldConfiguration
    """ # noqa: E501
    from_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The original technical identifier")
    to_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The new technical identifier")
    field_label: Annotated[str, Field(min_length=1, strict=True)] = Field(description="A user friendly label for the field")
    __properties: ClassVar[List[str]] = ["uid", "type", "label", "from_name", "to_name", "field_label"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RenameDatasetFieldConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RenameDatasetFieldConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "type": obj.get("type"),
            "label": obj.get("label"),
            "from_name": obj.get("from_name"),
            "to_name": obj.get("to_name"),
            "field_label": obj.get("field_label")
        })
        return _obj


