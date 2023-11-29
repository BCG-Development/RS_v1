from dataclasses import dataclass

@dataclass
class TrailerTempZones:
    zone_1: str = "Front"
    zone_2: str = "Back"
    
@dataclass
class WarehouseZones:
    ambient: str = "Ambient"
    freezer: str = "Freezer"
    chilled: str = "Chilled"
    chilled_con: str = "Chilled Convienence"
    meat: str = "Meat and Poultry"
    fruit_veg: str = "Fruite and Veg"
    bread: str = "Bread"