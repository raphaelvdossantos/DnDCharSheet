#Rolagem dos attributos do personagem

import random as dice


def attributes_roll():
    attribute_roll = [0, 0, 0, 0]
    char_attribute = [0, 0, 0, 0, 0, 0]

    for a in range(len(char_attribute)):
        for i in range(len(attribute_roll)):
            attribute_roll[i] = dice.randint(1,6)
            attribute = sorted(attribute_roll)
        char_attribute[a] = sum(attribute[1:4])

    return char_attribute