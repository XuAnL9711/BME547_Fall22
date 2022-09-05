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

def input_HDL():
    HDL_input = input('Enter the HDL value:')
    return int(HDL_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    elif HDL_value < 40:
        return "Low"


# interface()
# interface2()

# HDL_input

check_HDL()