from dataclasses import dataclass
from typing import Any, Optional, List, Union
from uuid import UUID
from enum import Enum


class ApiException(Exception):
    """Exception class containing reasons of API get failures.

    Args:
        Exception (_type_): _description_
    """
    def __init__(self, status_message: str, status_code: int):
        self.status_message = status_message
        self.status_code = status_code


class Format(Enum):
    CABLE = "CABLE"
    SOCKET = "SOCKET"


class Standard(Enum):
    CHADEMO = "CHADEMO"
    IEC_62196__T2 = "IEC_62196_T2"
    IEC_62196__T2_COMBO = "IEC_62196_T2_COMBO"
    TESLA_S = "TESLA_S"


class Currency(Enum):
    EUR = "EUR"


class TypeEnum(Enum):
    ENERGY = "ENERGY"


@dataclass
class Tariff:
    type: TypeEnum
    price: float
    vat: int
    currency: Currency


@dataclass
class Connector:
    standard: Standard
    format: Format
    max_power: int
    pricing_id: Optional[UUID] = None
    tariffs: Optional[List[Tariff]] = None


class Status(Enum):
    AVAILABLE = "AVAILABLE"
    CHARGING = "CHARGING"
    OUTOFORDER = "OUTOFORDER"
    UNKNOWN = "UNKNOWN"


@dataclass
class Evse:
    status: Status
    connectors: List[Connector]


@dataclass
class Operator:
    name: str
    website: str


@dataclass
class DataClass:
    address: str
    city: str
    postal_code: str
    country: str
    evses: List[Evse]
    operator: Operator
    access_type: str
    support_phone_number: str
    suboperator: Optional[Operator] = None


@dataclass
class LocationApiResponse:
    status_code: int
    status_message: str
    data: Union[DataClass, List[Any]]
