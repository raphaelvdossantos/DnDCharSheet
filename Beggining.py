import attribute_roll as roll

#char_name = input("Qual o nome do seu personagem? ")

attribute_values = roll.attributes_roll()

'''
print("Os valores rolados para os atributos foram:", attributes_roll())

print("\nDistribua os valores nos atributos desejados:")
'''
print(attribute_values)
char_attribute = ["For", "Des", "Cons", "Int", "Sab", "Car"]
for i in range(len(attribute_values)):
    roll = int(input("Qual valor para " + char_attribute[i] + "? "))
    attribute_values.remove(roll)
    char_attribute[i] += (" " + str(roll))
    print(char_attribute[i], "\n")
    print(attribute_values)

