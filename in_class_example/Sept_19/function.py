def add(a, b):
    return a + b


def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    elif HDL_value < 40:
        return "Low"