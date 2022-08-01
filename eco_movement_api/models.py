from dataclasses import dataclass
from typing import Any, Optional, List, Union
from uuid import UUID
from enum import Enum

# It seems that oplaadpalen.nl is using the API of eco-movement.
# Docs of this API can be found here: https://developers.eco-movement.com/reference/locations


class Format(Enum):
    """The format of the connector."""
    CABLE = "CABLE"
    SOCKET = "SOCKET"


class Standard(Enum):
    CHADEMO = "CHADEMO"
    """The connector type is CHAdeMO, DC"""
    DOMESTIC_A = "DOMESTIC_A"
    """Standard or Domestic household, type "A", NEMA 1-15, 2 pins"""
    DOMESTIC_B = "DOMESTIC_B"
    """Standard or Domestic household, type "B", NEMA 5-15, 3 pins"""
    DOMESTIC_C = "DOMESTIC_C"
    """Standard or Domestic household, type "C", CEE 7/17, 2 pins"""
    DOMESTIC_D = "DOMESTIC_D"
    """Standard or Domestic household, type "D", 3 pin"""
    DOMESTIC_E = "DOMESTIC_E"
    """Standard or Domestic household, type "E", CEE 7/5 3 pins"""
    DOMESTIC_F = "DOMESTIC_F"
    """Standard or Domestic household, type "F", CEE 7/4, Schuko, 3 pins"""
    DOMESTIC_G = "DOMESTIC_G"
    """Standard or Domestic household, type "G", BS 1363, Commonwealth, 3 pins"""
    DOMESTIC_H = "DOMESTIC_H"
    """Standard or Domestic household, type "H" SI-32, 3 pins"""
    DOMESTIC_I = "DOMESTIC_I"
    """Standard or Domestic household, type "I", AS 3112, 3 pins"""
    DOMESTIC_J = "DOMESTIC_J"
    """Standard or Domestic household, type "J", SEV 1011, 3 pins"""
    DOMESTIC_K = "DOMESTIC_K"
    """Standard or Domestic household, type "K", DS 60884-2-D1, 3 pins"""
    DOMESTIC_L = "DOMESTIC_L"
    """Standard or Domestic household, type "L", CEI 23-16-VII, 3 pins"""
    IEC_60309_2_single_16 = "IEC_60309_2_single_16"
    """IEC 60309-2 Industrial Connector single phase 16 Amperes (usually blue)"""
    IEC_60309_2_three_16 = "IEC_60309_2_three_16"
    """IEC 60309-2 Industrial Connector three phase 16 Amperes (usually red)"""
    IEC_60309_2_three_32 = "IEC_60309_2_three_32"
    """IEC 60309-2 Industrial Connector three phase 32 Amperes (usually red)"""
    IEC_60309_2_three_64 = "IEC_60309_2_three_64"
    """IEC 60309-2 Industrial Connector three phase 64 Amperes (usually red)"""
    IEC_62196_T1 = "IEC_62196_T1"
    """IEC 62196 Type 1 'SAE J1772'"""
    IEC_62196_T1_COMBO = "IEC_62196_T1_COMBO"
    """Combo Type 1 based, DC"""
    IEC_62196_T2 = "IEC_62196_T2"
    """IEC 62196 Type 2 “Mennekes”"""
    IEC_62196_T2_COMBO = "IEC_62196_T2_COMBO"
    """Combo Type 2 based, DC"""
    IEC_62196_T3A = "IEC_62196_T3A"
    """IEC 62196 Type 3A"""
    IEC_62196_T3C = "IEC_62196_T3C"
    """IEC 62196 Type 3C 'Scame'"""
    TESLA_R = "TESLA_R"
    """Tesla Connector "Roadster" - Type (round, 4 pin)"""
    TESLA_S = "TESLA_S"
    """Tesla Connector "Model-S" - Type (oval, 5 pin)"""


class TariffTypeEnum(Enum):
    """The type of tariff."""
    ENERGY = "ENERGY"
    """The price per kWh."""
    FLAT = "FLAT"
    """The fixed price per charging session."""
    PARKING_TIME = "PARKING_TIME"
    """The parking price per hour."""
    TIME = "TIME"
    """The fixed price per hour."""


@dataclass
class Tariff:
    type: TariffTypeEnum
    price: float
    vat: int
    currency: str


@dataclass
class Connector:
    standard: Standard
    format: Format
    max_power: int
    pricing_id: Optional[UUID] = None
    tariffs: Optional[List[Tariff]] = None


class Status(Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
    CHARGING = "CHARGING"
    INOPERATIVE = "INOPERATIVE"
    OUTOFORDER = "OUTOFORDER"
    PLANNED = "PLANNED"
    REMOVED = "REMOVED"
    RESERVED = "RESERVED"
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
    data: Union[DataClass, List[Any]] = None
