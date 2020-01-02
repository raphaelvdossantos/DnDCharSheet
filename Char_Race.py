# Modificação de atributo de acordo com a raça do personagem


def race(char_race, char_attribute, attribute_values):

    final_attributes = attribute_values
    try:
        if char_race.lower() == "elfo":
            final_attributes[2] = attribute_values[2] - 2
            final_attributes[1] = attribute_values[1] + 2
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(final_attributes[b])
            return char_attribute

        elif char_race.lower() == "meio elfo":
            final_attributes[2] = attribute_values[2] - 2
            final_attributes[1] = attribute_values[1] + 2
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(final_attributes[b])
            return char_attribute

        elif char_race.lower() == "meio orc":
            final_attributes[3] = attribute_values[3] - 2
            final_attributes[5] = attribute_values[5] - 2
            final_attributes[0] = attribute_values[0] + 2
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(final_attributes[b])
            return char_attribute

        elif char_race.lower() == "anão":
            final_attributes[5] = attribute_values[5] - 2
            final_attributes[2] = attribute_values[2] + 2
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(final_attributes[b])
            return char_attribute

        elif char_race.lower() == "halfing":
            final_attributes[0] = attribute_values[0] - 2
            final_attributes[1] = attribute_values[1] + 2
            for b in range(len(char_attribute)):
                char_attribute[b] += " " + str(final_attributes[b])
            return char_attribute
    except:
        print("Opção Inválida, selecione novamente:")
        return "inválido"
