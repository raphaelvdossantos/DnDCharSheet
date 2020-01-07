# Character Sheet

import random as dice
import Items_List as list
#import Mods_Checks as saving
import Saving_Throws as test

class char_sheet:
    # Definition of the Character's Attributes

    def attributes_roll():
        attribute_roll = [0, 0, 0, 0]
        char_attribute = [0, 0, 0, 0, 0, 0]

        try:
            for a, c in enumerate(char_attribute):
                for i, o in enumerate(attribute_roll):
                    attribute_roll[i] = dice.randint(1, 6)
                    attribute = sorted(attribute_roll)
                char_attribute[a] = sum(attribute[1:4])
            return char_attribute

        except Exception as e:
            print(e)
            print("System Error")

    def race(self, char_attribute, attribute_values):

        final_attributes = attribute_values
        attributes = {}
        try:
            if self.lower() == "elfo":
                final_attributes[2] = attribute_values[2] - 2
                final_attributes[1] = attribute_values[1] + 2
                for a, b in enumerate(char_attribute):
                    attributes[char_attribute[a]] = final_attributes[a]
                return attributes

            elif self.lower() == "meio elfo":
                final_attributes[2] = attribute_values[2] - 2
                final_attributes[1] = attribute_values[1] + 2
                for a, b in enumerate(char_attribute):
                    attributes[char_attribute[a]] = final_attributes[a]
                return attributes

            elif self.lower() == "meio orc":
                final_attributes[3] = attribute_values[3] - 2
                final_attributes[5] = attribute_values[5] - 2
                final_attributes[0] = attribute_values[0] + 2
                for a, b in enumerate(char_attribute):
                    attributes[char_attribute[a]] = final_attributes[a]
                return attributes

            elif self.lower() == "anão":
                final_attributes[5] = attribute_values[5] - 2
                final_attributes[2] = attribute_values[2] + 2
                for a, b in enumerate(char_attribute):
                    attributes[char_attribute[a]] = final_attributes[a]
                return attributes

            elif self.lower() == "halfing":
                final_attributes[0] = attribute_values[0] - 2
                final_attributes[1] = attribute_values[1] + 2
                for a, b in enumerate(char_attribute):
                    attributes[char_attribute[a]] = final_attributes[a]
                return attributes
            elif self.lower() == "humano":
                for a, b in enumerate(char_attribute):
                    attributes[char_attribute[a]] = final_attributes[a]
                return attributes
        except Exception as e:
            print("Algo deu errado, procure por ", e)

    # Definition of Items and Skills accordingly to the chosen class
    def char_class(self):

        if self.lower() == "barbaro":
            saving.base_fortitude = test.Proficiency
            saving.base_reflex = test.Nonproficiency
            saving.base_will = test.Nonproficiency
            Savings = [saving.Fortitude_Save["Total"], saving.Reflex_Save["Total"], saving.Will_Save["Total"]]
            weapons_list =[0, 0]
            for a, weapon in enumerate(weapons_list):
                weapons_list[a] = list.fighter_basic_weapons[dice.randint(1, len(list.fighter_basic_weapons)-1)]["Name"]
            return weapons_list, Savings

        elif self.lower() == "guerreiro":
            saving.base_fortitude = test.Proficiency
            saving.base_reflex = test.Nonproficiency
            saving.base_will = test.Nonproficiency
            Savings = [saving.Fortitude_Save["Total"], saving.Reflex_Save["Total"], saving.Will_Save["Total"]]
            weapons_list = [0]
            for a, weapon in enumerate(weapons_list):
                weapons_list[a] = list.fighter_basic_weapons[dice.randint(1, len(list.fighter_basic_weapons)-1)]["Name"]
            return weapons_list, Savings

    # Method to roll tasks and skills
    def roll_task(task, modificators):
        return None

