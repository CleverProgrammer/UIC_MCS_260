"""
MCS 260 Project by Rafeh Qazi.
Modified: November 2016
"""


class Insurance:
    def __init__(self, name, copay, deductible):
        self.name = name
        self.copay = copay
        self.deductible = deductible

    def __repr__(self):
        return self.name

    def patient_bill(self, treatment_cost, total_exp):
        return treatment_cost + total_exp


class Treatment:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Patient:
    def __init__(self, insurance_plan, name):
        self.insurance_plan = insurance_plan.name
        self.name = name

        self.account_balance = 0
        self.total_exp = 0
        self.medical_history = []

    def show_record(self):
        print("Name of patient: " + self.name)
        print("Insurance Plan on file: " + self.insurance_plan)
        print("Bill year-to-date: {}".format(self.total_exp))
        print("Account Balance: {}".format(self.account_balance))
        print("Medical History: {}".format(self.medical_history))

    def pay_bill(self, pay):
        self.account_balance += pay

    def order_treatment(self, treatment):
        self.medical_history.append(treatment)

    def __repr__(self):
        return '<{}: {}>'.format(self.name, self.insurance_plan)


aetna = Insurance('Aetna', 20, 300)
p1 = Patient(aetna, 'Bob')
p1.show_record()
# print(p1)
