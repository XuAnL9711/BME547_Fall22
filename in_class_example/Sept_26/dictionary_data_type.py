
def create_patient_entry(patient_first_name, patient_last_name, patient_id, patient_age):
    new_patient = {"First Name": patient_first_name,
                    "Last Name": patient_last_name,
                    "Id": patient_id,
                    "Age": patient_age,
                    "Tests": []}
    return new_patient


def print_database(db):
    for patient_key in db:
        # print("Name: {}, id: {}, age: {}".format(patient["First Name"],
        #                                         patient["Id"],
        #                                         patient["Age"]))
        # print("Name: {}, id: {}, age: {}".format(get_full_name(db[patient_key]),
        #                                         db[patient_key]["Id"],
        #                                         db[patient_key]["Age"]))
        print("Name: {}, id: {}, age: {}".format(get_full_name(patient_key),
                                        patient_key["Id"],
                                        patient_key["Age"]))


def get_full_name(patient):
    print('full name', patient["First Name"], patient["Last Name"])
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name

def find_patient(db, id_no):
    # for patient in db:
    #     if patient[1] == id_no:
    #         return patient
    # return False
    patient = db[id_no]
    return patient

def add_test_to_patient(db, id_no, test_name, test_value):
    # patient = find_patient(db, id_no)
    # patient[3].append(create_patient_entry("Ann", "Ables", 11, 30))
    # patient[3].append(create_patient_entry("Bob", "Boyles", 22, 34))
    # patient[3].append(create_patient_entry("Chris", "Chou", 3, 2))
    # print_database(db)
    # add_test_to_patient(db, 3, "HDL", 100)
    patient = find_patient(db, id_no)
    return patient


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"

def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 11, 30))
    db.append(create_patient_entry("Bob", "Boyles", 22, 34))
    db.append(create_patient_entry("Chris", "Chou", 3, 25))
    print_database(db)
    # exit(0)
    add_test_to_patient(db, 2, "HDL", 100)
    print_database(db)
    print("Patient {} is a {}".format(get_full_name(db[2]),
                                        adult_or_minor(db[2])))


if __name__ == "__main__":
    main()
