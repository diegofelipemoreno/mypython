import re, pdb

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
        return re.match(r"^\D+[a-zA-Z].\D$", response)

    switcher = {
        "boolean": if_boolean,
        "number": if_number,
        "string": if_string
    }

    if (valid_type in switcher):

        while (switcher[valid_type]() == None):
            response = input(input_value)
        return response
    else:
        raise Exception("Invalid type value, valid type (string, number, boolean)")
    

def match(self, filter):
    '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.'''
    return filter in self.memo or filter in self.tags