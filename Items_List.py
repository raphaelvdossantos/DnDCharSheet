# Listing of items armors and weapons
# Each item is a dictionary with the characteristics given in the DnD 3.5 books:
# Weapon Name - Price (in gold) - Damage (Small) - Damage (Medium) - Critical - Range (in meters) - Weight (in Kilos)

# WEAPONS


Club = {"Name": "Club", "Price": 0, "Damage S": "d4", "Damage M ": "d6", "Critical": 2, "Range": 1.5, "Weight": 1.5}
Dagger = {"Name": "Dagger", "Price": 2, "Damage S": "d3", "Damage M": "d4", "Critical": 2, "Range": 1.5, "Weight": 0.5}
Heavy_Mace = {"Name": "Heavy Mace", "Price": 12, "Damage S": "d6", "Damage M": "d8", "Critical": 2, "Range": 1.5, "Weight": 5}
Morningstar = {"Name": "Morningstar", "Price": 8, "Damage S": "d6", "Damage M": "d8", "Critical": 2, "Range": 1.5, "Weight": 3.5}

fighter_weapons = [Club, Dagger, Heavy_Mace, Morningstar]
