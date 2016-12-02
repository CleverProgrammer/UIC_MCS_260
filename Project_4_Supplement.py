from Project_4 import *

# The directory class is a helper class so I can search for patients and 
# treatments (but not insurance, its already included in the patient data).
class directory:
    def __init__(self):
        self.treatment_list = []
        self.patient_list = []

    def add_patient(self, new_patient):
        self.patient_list.append(new_patient)

    def search_patient(self, name):
        for patient in self.patient_list:
            if patient.name == name:
                return patient
        print("That patient is not on file...")
        return 0

    def add_treatment(self, treat):
        self.treatment_list.append(treat)

    def search_treatment(self, name):
        for treat in self.treatment_list:
            if treat.name == name:
                return treat
        print("That treatment is not on file...")
        return 0

# Here I am instantiating some class objects to use in my simulation
# treatment class inputs: name and cost
treat_1 = treatment("Python bite treatment", 100)
treat_2 = treatment("Java poisoning", 1500)
treat_3 = treatment("Vitamin C++ deficiency", 10)
# insurance class inputs: name, copay, and deductible
ins_1 = insurance("Red Cross Red Shield", 25, 2000)
ins_2 = insurance("Divided Health", 35, 1000)
# patient class inputs: name and insurance plan
pat_1 = patient("Bob", ins_1)
pat_2 = patient("Jeane", ins_2)

# Here I am adding the treatments and patients to the directory
direc = directory()
direc.add_treatment(treat_1)
direc.add_treatment(treat_2)
direc.add_treatment(treat_3)
direc.add_patient(pat_1)
direc.add_patient(pat_2)

# This is the user dialogue that interacts with doctors and patients.
answer = 0
while answer != 3:
    print("Welcome.  Please choose among the options.")
    print("1. Login as a patient")
    print("2. Login as a doctor")
    print("3. Quit")
    answer = int(input("Choice: "))
    if answer == 1:
        choice = 0
        current = 0
        while current == 0:
            name = input("Enter your name, or enter q to quit: ")
            if name == 'q':
                choice = 3
                break
            current = direc.search_patient(name)
        while choice != 3:
            print("Please choose among the options.")
            print("1. View your record")
            print("2. Pay your bill")
            print("3. Quit")
            choice = int(input("Choice: "))
            if choice == 1:
                print("-----------")
                current.show_record()
                print("-----------")
            if choice == 2:
                print("-----------")
                amount = float(input("Give amount to pay: "))
                current.pay_bill(amount)
                print("-----------")
    if answer == 2:
        print("Hello doctor.")
        choice = 0
        current = 0
        while current == 0:
            name = input("Please enter the patient name, or enter q to quit: ")
            if name == 'q':
                choice = 3
                break
            current = direc.search_patient(name)
        while choice != 3:
            print("Please choose among the options: ")
            print("1. View the patient's record")
            print("2. Order a treatment for the patient")
            print("3. Quit")
            choice = int(input("Choice: "))
            if choice == 1:
                print("-----------")
                current.show_record()
                print("-----------")
            if choice == 2:
                treat = 0
                while treat == 0:
                    print("-----------")
                    name2 = input("Please enter the treatment name, or enter q to quit: ")
                    print("-----------")
                    if name2 == 'q':
                        break
                    treat = direc.search_treatment(name2)
                if name2 != 'q':
                    current.order_treatment(treat)
                    
