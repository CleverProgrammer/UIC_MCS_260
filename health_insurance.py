"""
Author: Rafeh
"""
class Insurance:
    def __init__(self, name, copay, deductible):
        self.name = name
        self.copay = copay
        self.deductible = deductible

    def __repr__(self):
        return self.name

    def patient_bill(self, treatment_cost):
        pass


class Treatment:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Patient:
    def __init__(self, insurance_plan, name):
        self.name = name
        self.insurance_plan = insurance_plan

    def __repr__(self):
        return '<{}: {}>'.format(self.name, self.insurance_plan)

aetna = Insurance('aetna', 20, 300)
p1 = Patient(aetna, 'bob')
print(p1)
