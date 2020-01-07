# Listing of items armors and weapons
# Each item is a dictionary with the characteristics given in the DnD 3.5 books:
# Weapon Name - Price (in gold) - Damage (Small) - Damage (Medium) - Critical - Range (in meters) - Weight (in Kilos)

# WEAPONS

# Simple Weapons

# --> Light Melee Weapons
Dagger = {"Name": "Dagger", "Price": 2, "Damage S": 3, "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Light_Mace = {"Name": "Dagger", "Price": 5, "Damage S": 4, "Damage M": 6, "Critical": 2, "Range": 1.5, "Weight": 2}
Sickle = {"Name": "Sickle", "Price": 6, "Damage S": 4, "Damage M": 6, "Critical": 2, "Range": 1.5, "Weight": 1}

# --> One-Handed Melee Weapons
Club = {"Name": "Club", "Price": 0, "Damage S": 8, "Damage M ": 4, "Critical": 2, "Range": 1.5, "Weight": 1.5}
Heavy_Mace = {"Name": "Heavy Mace", "Price": 12, "Damage S": 6, "Damage M": 8, "Critical": 2, "Range": 1.5, "Weight": 5}
Morningstar = {"Name": "Morningstar", "Price": 8, "Damage S": 6, "Damage M": 8, "Critical": 2, "Range": 1.5, "Weight": 3.5}
Shortspear = {"Name": "Shortspear", "Price": 1, "Damage S": 4, "Damage M": 6, "Critical": 2, "Range": 1.5, "Weight": 0.5}

# --> Two-Handed Melee Weapons
Longspear = {"Name": "Longspear", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Quarterstaff = {"Name": "Quarterstaff", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Spear = {"Name": "Spear", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}

# --> Ranged Weapons
Heavy_Crossbow  = {"Name": "Dagger", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Light_Crossbow = {"Name": "Dagger", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Dart = {"Name": "Dagger", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Javelin = {"Name": "Dagger", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}
Sling = {"Name": "Dagger", "Price": 2, "Damage S": "d3", "Damage M": 4, "Critical": 2, "Range": 1.5, "Weight": 0.5}

fighter_basic_weapons = [Club, Dagger, Heavy_Mace, Morningstar]
