from dataclasses import dataclass

@dataclass
class TrailerTempZones:
    """
    Data class representing temperature zones for a trailer.

    Attributes:
    - zone_1 (str): The first zone, typically "Front".
    - zone_2 (str): The second zone, typically "Back".
    """
    zone_1: str = "Front"
    zone_2: str = "Back"

@dataclass
class WarehouseTempZones:
    """
    Data class representing temperature zones for a warehouse.

    Attributes:
    - ambient_temp_lower (float): Lower limit for ambient temperature.
    - ambient_temp_upper (float): Upper limit for ambient temperature.
    - bulk_temp_lower (float): Lower limit for bulk temperature.
    - bulk_temp_lower_temp_upper (float): Upper limit for bulk temperature.
    - bread_temp_lower (float): Lower limit for bread temperature.
    - bread_temp_upper (float): Upper limit for bread temperature.
    - non_food_temp_lower (float): Lower limit for non-food temperature.
    - non_food_temp_upper (float): Upper limit for non-food temperature.
    - limited_offer_temp_lower (float): Lower limit for limited offer temperature.
    - limited_offer_temp_upper (float): Upper limit for limited offer temperature.
    - chilled_temp_upper (float): Upper limit for chilled temperature.
    - chilled_temp_lower (float): Lower limit for chilled temperature.
    - milk_temp_upper (float): Upper limit for milk temperature.
    - milk_temp_lower (float): Lower limit for milk temperature.
    - chilled_con_temp_upper (float): Upper limit for chilled convenience temperature.
    - chilled_con_temp_lower (float): Lower limit for chilled convenience temperature.
    - meat_temp_upper (float): Upper limit for meat temperature.
    - meat_temp_lower (float): Lower limit for meat temperature.
    - freezer_temp_upper (float): Upper limit for freezer temperature.
    - freezer_temp_lower (float): Lower limit for freezer temperature.
    - fruit_veg_temp_upper (float): Upper limit for fruit and veg temperature.
    - fruit_veg_temp_lower (float): Lower limit for fruit and veg temperature.
    - flowers_temp_upper (float): Upper limit for flowers temperature.
    - flowers_temp_lower (float): Lower limit for flowers temperature.
    """
    ambient_temp_lower: float = 11.0
    ambient_temp_upper: float = 24.0
    bulk_temp_lower: float = 11.0
    bulk_temp_lower_temp_upper: float = 24.0
    bread_temp_lower: float = 11.0
    bread_temp_upper: float = 24.0
    non_food_temp_lower: float = 11.0
    non_food_temp_upper: float = 24.0
    limited_offer_temp_lower: float = 11.0
    limited_offer_temp_upper: float = 24.0
    chilled_temp_upper: float = -2.0
    chilled_temp_lower: float = 3.0
    milk_temp_upper: float = -2.0
    milk_temp_lower: float = 3.0
    chilled_con_temp_upper: float = -2.0
    chilled_con_temp_lower: float = 3.0
    meat_temp_upper: float = 0.0
    meat_temp_lower: float = 3.0
    freezer_temp_upper: float = -18.0
    freezer_temp_lower: float = -28.0
    fruit_veg_temp_upper: float = 11.0
    fruit_veg_temp_lower: float = 17.0
    flowers_temp_upper: float = 11.0
    flowers_temp_lower: float = 17.0
