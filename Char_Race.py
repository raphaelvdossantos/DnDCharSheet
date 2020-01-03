# Modification of the character's attributes accordingly to each race


def race(char_race, char_attribute, attribute_values):

    final_attributes = attribute_values
    attributes = {}

    try:
        if char_race.lower() == "elfo":
            final_attributes[2] = attribute_values[2] - 2
            final_attributes[1] = attribute_values[1] + 2
            for a, b in enumerate(char_attribute):
                attributes[char_attribute[a]] = final_attributes[a]
            return attributes

        elif char_race.lower() == "meio elfo":
            final_attributes[2] = attribute_values[2] - 2
            final_attributes[1] = attribute_values[1] + 2
            for a, b in enumerate(char_attribute):
                attributes[char_attribute[a]] = final_attributes[a]
            return attributes

        elif char_race.lower() == "meio orc":
            final_attributes[3] = attribute_values[3] - 2
            final_attributes[5] = attribute_values[5] - 2
            final_attributes[0] = attribute_values[0] + 2
            for a, b in enumerate(char_attribute):
                attributes[char_attribute[a]] = final_attributes[a]
            return attributes

        elif char_race.lower() == "anão":
            final_attributes[5] = attribute_values[5] - 2
            final_attributes[2] = attribute_values[2] + 2
            for a, b in enumerate(char_attribute):
                attributes[char_attribute[a]] = final_attributes[a]
            return attributes

        elif char_race.lower() == "halfing":
            final_attributes[0] = attribute_values[0] - 2
            final_attributes[1] = attribute_values[1] + 2
            for a, b in enumerate(char_attribute):
                attributes[char_attribute[a]] = final_attributes[a]
            return attributes
        elif char_race.lower() == "humano":
            for a, b in enumerate(char_attribute):
                attributes[char_attribute[a]] = final_attributes[a]
            return attributes
    except:
        print("Opção Inválida, selecione novamente:")
        return "inválido"
