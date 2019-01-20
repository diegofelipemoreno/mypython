import re, pdb, sys
from exceptions import InvalidTypeValue

#pdb.set_trace()

def get_valid_custom_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

def get_valid_type_input(input_value, valid_type):
    valid_type = valid_type.lower()
    output_value = ''
    response = input(input_value)

    def if_boolean():
        if (str(response) == "true" or str(response) == "false"):
            return True

    def if_number():
        return re.match(r"^([\s\d]+)$", response)
    
    def if_string():
        return re.match(r"^\D+[a-zA-Z]\D$", response)

    type_dict = {
        "boolean": if_boolean,
        "number": if_number,
        "string": if_string
    }

    try:
        while (type_dict[valid_type]() == None):
            response = input(input_value)
        return response
    except KeyError as exception:
        raise InvalidTypeValue("\n {} is not part of type_dict: \n\t -boolean \n\t -number \n\t -string".format(exception))