# functions with outputs

def format_name(f_name, l_name):
    """reformats first & last name to title case"""
    if f_name =="" or l_name == "":
        return "You didn't enter a name."          # if no first or last name is given, return ends the function
    first_name = f_name.title()
    last_name = l_name.title()
    return f"Result: {first_name} {last_name}"   # return ends the function
print(format_name(input("What is your first name?"),input("what is your last name?")))
