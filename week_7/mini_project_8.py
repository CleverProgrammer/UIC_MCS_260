"""
Author: Rafeh Qazi
Modified: October 2016
Program: OOP DragonCard implementation.
"""


class DragonCard:
    card_count = 0
    minimal_balance = 0

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.card_count += 1

    def add_to_balance(self, amount):
        if self.balance + amount <= self.minimal_balance:
            print("DUDE. WHAT ARE YOU TALKING ABOUT.")
        else:
            self.balance += amount

    def activate_SRF_membership(self):
        self.member = True


class StudentDragonCard(DragonCard):
    student_card_count = 0

    def __init__(self, name, balance):
        super(StudentDragonCard, self).__init__(name, balance)
        StudentDragonCard.student_card_count += 1


class FacultyDragonCard(DragonCard):
    faculty_card_count = 0
    member_fee = 50

    def __init__(self, name, balance):
        super(FacultyDragonCard, self).__init__(name, balance)
        FacultyDragonCard.faculty_card_count += 1


    def activate_SRF_membership(self):
        super(FacultyDragonCard, self).activate_SRF_membership()
        self.balance -= self.member_fee

        if self.balance < self.minimal_balance:
            print("You NEED MORE MONEY!")
        else:
            self.member = True


bob = StudentDragonCard('Toby', 100)
bob.add_to_balance(100)
print(bob.balance)

jimmy = StudentDragonCard('bob', 200)
print(StudentDragonCard.student_card_count)

john = FacultyDragonCard('John', 100)
john.activate_SRF_membership()
# print(bob)
