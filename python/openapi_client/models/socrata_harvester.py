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

from pydantic import ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.harvester import Harvester
from openapi_client.models.related_user_read_only import RelatedUserReadOnly
from typing import Optional, Set
from typing_extensions import Self

class SocrataHarvester(Harvester):
    """
    SocrataHarvester
    """ # noqa: E501
    url: Annotated[str, Field(min_length=1, strict=True)]
    download_resources: Optional[StrictBool] = Field(default=False, description="If you want to download resources instead of attaching them via URL.")
    metadata_only: Optional[StrictBool] = Field(default=False, description="If you want to harvest the remote datasets metadata without their resources.")
    __properties: ClassVar[List[str]] = ["uid", "type", "name", "status", "version", "restrict_datasets_visibility", "delete_missing_datasets", "forced_metas", "remote_datasets_count", "harvested_datasets_count", "published_datasets_count", "attached_datasets_count", "has_error", "resource_errors_count", "created_at", "updated_at", "updated_by", "last_started_at", "last_success_at", "url", "download_resources", "metadata_only"]

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
        """Create an instance of SocrataHarvester from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updated_by'] = self.updated_by.to_dict()
        # set to None if last_started_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_started_at is None and "last_started_at" in self.model_fields_set:
            _dict['last_started_at'] = None

        # set to None if last_success_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_success_at is None and "last_success_at" in self.model_fields_set:
            _dict['last_success_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SocrataHarvester from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "version": obj.get("version") if obj.get("version") is not None else 1,
            "restrict_datasets_visibility": obj.get("restrict_datasets_visibility"),
            "delete_missing_datasets": obj.get("delete_missing_datasets") if obj.get("delete_missing_datasets") is not None else False,
            "forced_metas": obj.get("forced_metas"),
            "remote_datasets_count": obj.get("remote_datasets_count"),
            "harvested_datasets_count": obj.get("harvested_datasets_count"),
            "published_datasets_count": obj.get("published_datasets_count"),
            "attached_datasets_count": obj.get("attached_datasets_count"),
            "has_error": obj.get("has_error"),
            "resource_errors_count": obj.get("resource_errors_count"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "updated_by": RelatedUserReadOnly.from_dict(obj["updated_by"]) if obj.get("updated_by") is not None else None,
            "last_started_at": obj.get("last_started_at"),
            "last_success_at": obj.get("last_success_at"),
            "url": obj.get("url"),
            "download_resources": obj.get("download_resources") if obj.get("download_resources") is not None else False,
            "metadata_only": obj.get("metadata_only") if obj.get("metadata_only") is not None else False
        })
        return _obj


