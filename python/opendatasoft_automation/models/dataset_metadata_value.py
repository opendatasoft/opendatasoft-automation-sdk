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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DatasetMetadataValue(BaseModel):
    """
    DatasetMetadataValue
    """ # noqa: E501
    value: Optional[Any] = Field(description="The effective metadata value. If the dataset is linked to a remote dataset and `override_remote_value`  is `false`, this value will be the same as `remote_value`.")
    remote_value: Optional[Any] = Field(default=None, description="The metadata value on the remote dataset. This property is present only if the dataset is linked to a remote  dataset (a federated dataset for example).")
    override_remote_value: Optional[StrictBool] = Field(default=None, description="Defines if the remote value is overridden (`true`), or if it is kept in sync with the value on the remote  dataset. This property is present only if the dataset is linked to a remote  dataset (a federated dataset for example).")
    __properties: ClassVar[List[str]] = ["value", "remote_value", "override_remote_value"]

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
        """Create an instance of DatasetMetadataValue from a JSON string"""
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
            "remote_value",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if remote_value (nullable) is None
        # and model_fields_set contains the field
        if self.remote_value is None and "remote_value" in self.model_fields_set:
            _dict['remote_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatasetMetadataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "value": obj.get("value"),
            "remote_value": obj.get("remote_value"),
            "override_remote_value": obj.get("override_remote_value")
        })
        return _obj


