#Functions with Outputs

#함수 제일 첫번째 줄은 독스트링(Docstring)이라고 하고 해당 함수에 대한 부연설명을 적을 수 있다. -> 함수를 쓰려고할 때 나타남
def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name."""


    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()


    return f"Result: {formated_f_name} {formated_l_name}"

formated_name = format_name(input("What is your first name? "), input("What is your last name? "))
print(formated_name)

# format_name("wonkyoung") 
