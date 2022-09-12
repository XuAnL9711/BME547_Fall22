print("This is the calculator.py module")
print("Pyton thinks this is called {}".format(__name__))

def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    if choice=='9':
        return

def interface2():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return

def input_LDL():
    LDL_input = input('Enter the LDL value:')
    return int(LDL_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    elif HDL_value < 40:
        return "Low"

def check_LDL(LDL_value):
    if LDL_value <= 130:
        return "Normal"
    elif 130 <= LDL_value < 159:
        return "Borderline High"
    elif 160 <= LDL_value < 189:
        return "High"
    elif LDL_value >= 190:
        return "Very High"

def check_total_Cholesterol(LDL_value):
    if LDL_value <= 200:
        return "Normal"
    elif 200 < LDL_value < 239:
        return "Borderline high"
    elif LDL_value >= 240:
        return "High"

def LDL_drive():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_results(ldl_value, answer)
    answer_cholesterol = check_total_Cholesterol(ldl_value)
    output_cholesterol_results(ldl_value, answer_cholesterol)

def output_LDL_results(ldl_value, charac):
    print("The results for an LDL, value of {} is {}".format(ldl_value, charac))

def output_cholesterol_results(ldl_value, charac):
    print("The results for a total Cholesterol Check, value of {} is {}".format(ldl_value, charac))

# interface()
# interface2()

# HDL_input

# HDL_drive()

if __name__ == "__main__":
    LDL_drive()