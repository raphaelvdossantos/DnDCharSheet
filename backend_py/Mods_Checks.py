# Character's attributes mods, Saves and other characteristics
import Character_Creation


attribute = list(Character_Creation.char_attributes.values())
level = Character_Creation.char_level

mod_value = 0
attribute_mod = [0, 0, 0, 0, 0, 0]
z = 11

# Definition of Characters Attribute's Mods

for i, a in enumerate(attribute):
    while not attribute[i] == z:
        if attribute[i] > z:
            if z % 2 == 0:
                mod_value += 1
                z += 1
            else:
                z += 1

        if attribute[i] < z:
            if z % 2 == 0:
                mod_value -= 1
                z -= 1
            else:
                z -= 1

    if attribute[i] == z and attribute[i] > 10 and z % 2 == 0:
        mod_value += 1
    attribute_mod[i] = mod_value
    mod_value = 0
    z = 11

print(attribute_mod)

Base_Armor = 10
Life_Points = {"Total": 0 + attribute_mod[2], "Talentos": 0, "Mod Atributo": attribute_mod[2]}
Armor_Class = {"Total": Base_Armor + attribute_mod[2], "Bonus de Armadura": 0, "Mod Atributo": attribute_mod[1], "Mod Tamanho": 0}
Surprise_Armor = Armor_Class["Total"] - attribute_mod[2]

base_fortitude = []
base_reflex = []
base_will = []

Fortitude_Save = {"Total": base_fortitude[level] + attribute_mod[2], "Mod Base": 0, "Mod Atributo": attribute_mod[2]}
Reflex_Save = {"Total": base_reflex[level] + attribute_mod[1], "Mod Base": 0, "Mod Atributo": attribute_mod[1]}
Will_Save = {"Total": base_will[level] + attribute_mod[4], "Mod Base": 0, "Mod Atributo": attribute_mod[4]}


