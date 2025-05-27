
# Function to format name to the Title format
def format_name(f_name, l_name):
    """
    Take first and last name and format it
    to return the title case version of the name.
    """

    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


# formatted_name = format_name(l_name="JklaJjka", f_name="viNNy")
# print(formatted_name)
print(format_name(f_name=input("What is your first name?"), l_name=input("What is your last name?")))


# Function that duplicates the input text
def function_1(text):
    return text + " " + text


# Function returns the Title version of the input text
def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)





