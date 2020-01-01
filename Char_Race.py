# Modificação de atributo de acordo com a raça do personagem


def race(char_race, char_attribute, attribute_values):

    try:
        if char_race.lower() == "elfo":
            char_attribute[2] += " " + str((attribute_values[2] - 2))
            char_attribute[3] += " " + str((attribute_values[3] + 2))
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(attribute_values[b])
            return char_attribute

        elif char_race.lower() == "meio elfo":
            char_attribute[2] += " " + str((attribute_values[2] - 2))
            char_attribute[3] += " " + str((attribute_values[3] + 2))
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(attribute_values[b])
            return char_attribute

        elif char_race.lower() == "meio orc":
            char_attribute[2] += " " + str((attribute_values[2] - 2))
            char_attribute[3] += " " + str((attribute_values[3] + 2))
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(attribute_values[b])
            return char_attribute

        elif char_race.lower() == "anão":
            char_attribute[2] += " " + str((attribute_values[2] - 2))
            char_attribute[3] += " " + str((attribute_values[3] + 2))
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(attribute_values[b])
            return char_attribute

        elif char_race.lower() == "halfing":
            char_attribute[2] += " " + str((attribute_values[2] - 2))
            char_attribute[3] += " " + str((attribute_values[3] + 2))
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(attribute_values[b])
            return char_attribute
    except:
        print("Opção Inválida, selecione novamente:")
        return "inválido"
