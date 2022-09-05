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

def HDL_drive():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_results(hdl_value, answer)

def output_HDL_results(hdl_value, charac):
    print("The results for an HDL, value of {} is {}".format(hdl_value, charac))

# interface()
# interface2()

# HDL_input

HDL_drive()