import random as dice

# Dice Roller for all functions that requires dice rolling


def dice_rolling(dice_quantity=1, sided_dice=6):

    sorted_result = []
    roll_result = []
    for i in range(dice_quantity):
        roll_result.append(dice.randint(1, sided_dice))
        sorted_result = sorted(roll_result)

    roll_sum = sum(sorted_result)
    return roll_sum

'''
def character_attack(character, talent):
    attack = character.mod[] + talent + dice.radint(1,20)
    return  attack
'''


