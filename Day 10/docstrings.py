# Docstrings are used for our code documentation of our code or give explanation to the code
# it should come the first of line after declaration
# Function with multiple return values.

def format_name(f_name, l_name):
    """Take the first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name(input("What is your first name? "),input("What is your last name? "))
print(formated_string)

