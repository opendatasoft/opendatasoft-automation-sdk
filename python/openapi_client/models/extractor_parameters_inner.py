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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ExtractorParametersInner(BaseModel):
    """
    ExtractorParametersInner
    """ # noqa: E501
    type: StrictStr
    is_mandatory: StrictBool
    name: StrictStr
    label: Optional[StrictStr] = None
    default: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    hidden: Optional[StrictBool] = None
    trim: Optional[StrictStr] = None
    choices: Optional[List[StrictStr]] = None
    can_create_field: Optional[StrictBool] = None
    impacts_guessed_parameters: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["type", "is_mandatory", "name", "label", "default", "description", "hidden", "trim", "choices", "can_create_field", "impacts_guessed_parameters"]

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
        """Create an instance of ExtractorParametersInner from a JSON string"""
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
        """Create an instance of ExtractorParametersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "is_mandatory": obj.get("is_mandatory"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "default": obj.get("default"),
            "description": obj.get("description"),
            "hidden": obj.get("hidden"),
            "trim": obj.get("trim"),
            "choices": obj.get("choices"),
            "can_create_field": obj.get("can_create_field"),
            "impacts_guessed_parameters": obj.get("impacts_guessed_parameters")
        })
        return _obj


