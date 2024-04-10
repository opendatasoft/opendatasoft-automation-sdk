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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.dataset_metadata_value import DatasetMetadataValue
from typing import Optional, Set
from typing_extensions import Self

class DatasetMetadataInternal(BaseModel):
    """
    This set of metadata is used for dataset configuration and won't appear on your portal.
    """ # noqa: E501
    license_id: Optional[DatasetMetadataValue] = None
    theme_id: Optional[DatasetMetadataValue] = None
    draft: Optional[DatasetMetadataValue] = None
    __properties: ClassVar[List[str]] = ["license_id", "theme_id", "draft"]

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
        """Create an instance of DatasetMetadataInternal from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of license_id
        if self.license_id:
            _dict['license_id'] = self.license_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of theme_id
        if self.theme_id:
            _dict['theme_id'] = self.theme_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of draft
        if self.draft:
            _dict['draft'] = self.draft.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatasetMetadataInternal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "license_id": DatasetMetadataValue.from_dict(obj["license_id"]) if obj.get("license_id") is not None else None,
            "theme_id": DatasetMetadataValue.from_dict(obj["theme_id"]) if obj.get("theme_id") is not None else None,
            "draft": DatasetMetadataValue.from_dict(obj["draft"]) if obj.get("draft") is not None else None
        })
        return _obj


