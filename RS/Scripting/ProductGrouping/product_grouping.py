from dataclasses import dataclass
from Scripting.CargoGrouping.tempzones import WarehouseTempZones

@dataclass
class WarehouseAreas:
    """
    Data class representing different areas within a warehouse.

    Attributes:
    - ambient (str): Ambient area.
    - bulk (str): Bulk storage area.
    - bread (str): Bread storage area.
    - non_food (str): Non-food storage area.
    - limited_offer (str): Limited offer storage area.
    - chilled (str): Chilled storage area.
    - milk (str): Milk storage area.
    - chilled_con (str): Chilled Convenience storage area.
    - meat (str): Meat and Poultry storage area.
    - freezer (str): Freezer storage area.
    - fruit_veg (str): Fruit and Veg storage area.
    - flowers (str): Flowers and Plants storage area.
    """
    ambient: str = "Ambient"
    bulk: str = "Bulk"
    bread: str = "Bread"
    non_food: str = "Non Food"
    limited_offer: str = "Limited Offer"
    chilled: str = "Chilled"
    milk: str = "Milk"
    chilled_con: str = "Chilled Convenience"
    meat: str = "Meat and Poultry"
    freezer: str = "Freezer"
    fruit_veg: str = "Fruit and Veg"
    flowers: str = "Flowers and Plants"

@dataclass
class ProductGroups:
    """
    Data class representing different product groups.

    Attributes:
    - ten (int): Product group 10.
    - twenty (int): Product group 20.
    - twenty_two (int): Product group 22.
    - thirty (int): Product group 30.
    - thirty_one (int): Product group 31.
    - forty (int): Product group 40.
    - forty_one (int): Product group 41.
    - forty_two (int): Product group 42.
    - fifty (int): Product group 50.
    - sixty (int): Product group 60.
    - seventy (int): Product group 70.
    - seventy_one (int): Product group 71.
    """
    ten: int = 10
    twenty: int = 20
    twenty_two: int = 22
    thirty: int = 30
    thirty_one: int = 31
    forty: int = 40
    forty_one: int = 41
    forty_two: int = 42
    fifty: int = 50
    sixty: int = 60
    seventy: int = 70
    seventy_one: int = 71

@dataclass
class ProductGrouping:
    """
    Data class representing a combination of product groups, warehouse areas, and temperature zones.

    Attributes:
    - product_groups (ProductGroups): Instance of ProductGroups.
    - warehouse_areas (WarehouseAreas): Instance of WarehouseAreas.
    - warehouse_temp_zones (WarehouseTempZones): Instance of WarehouseTempZones.
    """
    product_groups: ProductGroups
    warehouse_areas: WarehouseAreas
    warehouse_temp_zones: WarehouseTempZones

# Example usage:
A = ProductGrouping(
    product_groups=ProductGroups(ten=10),
    warehouse_areas=WarehouseAreas(ambient="Ambient"),
    warehouse_temp_zones=WarehouseTempZones(ambient_temp_lower=11.0, ambient_temp_upper=24.0)
)

B = ProductGrouping(
    product_groups=ProductGroups(twenty=20),
    warehouse_areas=WarehouseAreas(bulk="Bulk"),
    warehouse_temp_zones=WarehouseTempZones(bulk_temp_lower=11.0, bulk_temp_lower_temp_upper=24.0)
)

BRD = ProductGrouping(
    product_groups=ProductGroups(twenty_two=22),
    warehouse_areas=WarehouseAreas(bread="Bread"),
    warehouse_temp_zones=WarehouseTempZones(bread_temp_lower=11.0, bread_temp_upper=24.0)
)

NF = ProductGrouping(
    product_groups=ProductGroups(thirty=30),
    warehouse_areas=WarehouseAreas(non_food="Non Food"),
    warehouse_temp_zones=WarehouseTempZones(non_food_temp_lower=11.0, non_food_temp_upper=24.0)
)

LO = ProductGrouping(
    product_groups=ProductGroups(thirty_one=31),
    warehouse_areas=WarehouseAreas(limited_offer="Limited Offer"),
    warehouse_temp_zones=WarehouseTempZones(limited_offer_temp_lower=11.0, limited_offer_temp_upper=24.0)
)

CH = ProductGrouping(
    product_groups=ProductGroups(forty=40),
    warehouse_areas=WarehouseAreas(chilled="Chilled"),
    warehouse_temp_zones=WarehouseTempZones(chilled_temp_lower=3.0, chilled_temp_upper=-2.0)
)

MILK = ProductGrouping(
    product_groups=ProductGroups(forty_one=41),
    warehouse_areas=WarehouseAreas(milk="Milk"),
    warehouse_temp_zones=WarehouseTempZones(milk_temp_lower=3.0, milk_temp_upper=-2.0)
)

CON = ProductGrouping(
    product_groups=ProductGroups(forty_two=42),
    warehouse_areas=WarehouseAreas(chilled_con="Chilled Convenience"),
    warehouse_temp_zones=WarehouseTempZones(chilled_con_temp_lower=3.0, chilled_con_temp_upper=-2.0)
)

MEAT = ProductGrouping(
    product_groups=ProductGroups(fifty=50),
    warehouse_areas=WarehouseAreas(meat="Meat and Poultry"),
    warehouse_temp_zones=WarehouseTempZones(meat_temp_lower=3.0, meat_temp_upper=0.0)
)

FRZ = ProductGrouping(
    product_groups=ProductGroups(sixty=60),
    warehouse_areas=WarehouseAreas(freezer="Freezer"),
    warehouse_temp_zones=WarehouseTempZones(freezer_temp_lower=-28.0, freezer_temp_upper=-18.0)
)

FV = ProductGrouping(
    product_groups=ProductGroups(seventy=70),
    warehouse_areas=WarehouseAreas(fruit_veg="Fruit and Veg"),
    warehouse_temp_zones=WarehouseTempZones(fruit_veg_temp_lower=17.0, fruit_veg_temp_upper=11.0)
)

FP = ProductGrouping(
    product_groups=ProductGroups(seventy_one=71),
    warehouse_areas=WarehouseAreas(flowers="Flowers and Plants"),
    warehouse_temp_zones=WarehouseTempZones(flowers_temp_lower=17.0, flowers_temp_upper=11.0)
)

@dataclass
class Combinations:
    """
    Data class representing combinations of different warehouse areas, product groups, and temperature zones.

    Attributes:
    - FL (tuple): Combination of A, B, BRD, NF, LO, CH, MILK, CON, MEAT, FRZ, FV, FP.
    - AZ (tuple): Combination of A, B, NF, LO, FRZ.
    - FBC (tuple): Combination of CH, MILK, CON, MEAT, BRD, FV, FP.
    - AFB (tuple): Combination of A, B, BRD, FV, FP, NF, LO.
    - AC (tuple): Combination of A, B, CH, MILK, CON, MEAT, NF, LO.
    - CZ (tuple): Combination of CH, MILK, CON, MEAT, FRZ.
    - FBZ (tuple): Combination of BRD, FV, FP, FRZ.
    """
    FL = A, B, BRD, NF, LO, CH, MILK, CON, MEAT, FRZ, FV, FP
    AZ = A, B, NF, LO, FRZ
    FBC = CH, MILK, CON, MEAT, BRD, FV, FP
    AFB = A, B, BRD, FV, FP, NF, LO
    AC = A, B, CH, MILK, CON, MEAT, NF, LO
    CZ = CH, MILK, CON, MEAT, FRZ
    FBZ = BRD, FV, FP, FRZ
