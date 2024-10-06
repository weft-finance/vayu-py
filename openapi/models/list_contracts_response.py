# coding: utf-8

"""
    Vayu API

    The Vayu API is a RESTful API that allows you to submit events for processing and storage & manage billing related entities.           The API is secured using the Bearer Authentication scheme with JWT tokens.           To obtain a JWT token, please contact Vayu at team@withvayu.com

    The version of the OpenAPI document: 1.0.0
    Contact: dev@withvayu.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi.models.get_contract_response_contract import GetContractResponseContract
from typing import Optional, Set
from typing_extensions import Self

class ListContractsResponse(BaseModel):
    """
    ListContractsResponse
    """ # noqa: E501
    contracts: List[GetContractResponseContract]
    total: Union[StrictFloat, StrictInt]
    has_more: StrictBool = Field(alias="hasMore")
    next_cursor: Optional[StrictStr] = Field(default=None, alias="nextCursor")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["contracts", "total", "hasMore", "nextCursor"]

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
        """Create an instance of ListContractsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in contracts (list)
        _items = []
        if self.contracts:
            for _item_contracts in self.contracts:
                if _item_contracts:
                    _items.append(_item_contracts.to_dict())
            _dict['contracts'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListContractsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contracts": [GetContractResponseContract.from_dict(_item) for _item in obj["contracts"]] if obj.get("contracts") is not None else None,
            "total": obj.get("total"),
            "hasMore": obj.get("hasMore"),
            "nextCursor": obj.get("nextCursor")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


