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

from pydantic import ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.datasource import Datasource
from openapi_client.models.federated_datasource_all_of_dataset import FederatedDatasourceAllOfDataset
from openapi_client.models.federated_datasource_all_of_domain import FederatedDatasourceAllOfDomain
from openapi_client.models.related_user_read_only import RelatedUserReadOnly
from typing import Optional, Set
from typing_extensions import Self

class FederatedDatasource(Datasource):
    """
    FederatedDatasource
    """ # noqa: E501
    domain: FederatedDatasourceAllOfDomain
    dataset: FederatedDatasourceAllOfDataset
    permissions_user: Optional[RelatedUserReadOnly] = None
    impersonate_permissions: StrictBool
    parameters: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["type", "domain", "dataset", "permissions_user", "impersonate_permissions", "parameters"]

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
        """Create an instance of FederatedDatasource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of domain
        if self.domain:
            _dict['domain'] = self.domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dataset
        if self.dataset:
            _dict['dataset'] = self.dataset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions_user
        if self.permissions_user:
            _dict['permissions_user'] = self.permissions_user.to_dict()
        # set to None if permissions_user (nullable) is None
        # and model_fields_set contains the field
        if self.permissions_user is None and "permissions_user" in self.model_fields_set:
            _dict['permissions_user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FederatedDatasource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "domain": FederatedDatasourceAllOfDomain.from_dict(obj["domain"]) if obj.get("domain") is not None else None,
            "dataset": FederatedDatasourceAllOfDataset.from_dict(obj["dataset"]) if obj.get("dataset") is not None else None,
            "permissions_user": RelatedUserReadOnly.from_dict(obj["permissions_user"]) if obj.get("permissions_user") is not None else None,
            "impersonate_permissions": obj.get("impersonate_permissions"),
            "parameters": obj.get("parameters")
        })
        return _obj


