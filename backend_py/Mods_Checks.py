# Character's attributes mods, Saves and other characteristics
from backend_py import Saving_Throws as test
from backend_py import Dice_Roller as dice

def define_mods(attribute):
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

    return attribute_mod


def base_status(attribute_mod, level, style, life_dice):

    dv = dice.dice_rolling(level, life_dice)
    Base_Armor = 10
    Life_Points = {"Total": dv + attribute_mod[2], "Talentos": 0, "Mod Atributo": attribute_mod[2]}
    Armor_Class = {"Total": Base_Armor + attribute_mod[2], "Bonus de Armadura": 0, "Mod Atributo": attribute_mod[1], "Mod Tamanho": 0}
    Surprise_Armor = Armor_Class["Total"] - attribute_mod[2]

    base_fortitude = []
    base_reflex = []
    base_will = []

    if style == "primary fighter":
        base_fortitude = test.Proficiency
        base_reflex = test.Nonproficiency
        base_will = test.Nonproficiency

    Fortitude_Save = {"Total": base_fortitude[level] + attribute_mod[2], "Mod Base": 0, "Mod Atributo": attribute_mod[2]}
    Reflex_Save = {"Total": base_reflex[level] + attribute_mod[1], "Mod Base": 0, "Mod Atributo": attribute_mod[1]}
    Will_Save = {"Total": int(base_will[level]) + int(attribute_mod[4]), "Mod Base": 0, "Mod Atributo": attribute_mod[4]}
    Savings = [Fortitude_Save["Total"], Reflex_Save["Total"], Will_Save["Total"]]
    return Armor_Class["Total"], Savings, Life_Points["Total"]