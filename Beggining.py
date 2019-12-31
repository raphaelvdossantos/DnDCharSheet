import attribute_roll as roll
import Char_Race as race

char_name = input("Qual o nome do seu personagem? ")

rolled_values = roll.attributes_roll()

print("Os valores rolados para os atributos foram:", rolled_values)

print("\nDistribua os valores nos atributos desejados:")


print(rolled_values)
attribute_values = []

attribute = ["For", "Des", "Cons", "Int", "Sab", "Car"]
for i in range(len(rolled_values)):
    roll = int(input("Qual valor para " + attribute[i] + "? "))
    rolled_values.remove(roll)
    attribute_values.append(roll)
    print(attribute_values, "\n")
    print(rolled_values)

races_dict = {"a":"Elfo", "b":"Meio- Elfo", "c":"Meio-Orc", "d":"Anão", "e":"Halfling"}
choose_race= input("Qual a raça do seu personagem:" + str(races_dict))
chosen_race = str(races_dict[choose_race])
print(chosen_race)



