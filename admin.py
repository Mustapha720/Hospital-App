from colorama import init, Fore, Style
init(autoreset = True)
# from database import my_con
# from database import my_cursor

class User():
    def __init__(self, user_id, name, role, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.signed_user = []
        self.role = role # doctor, patient, nurse

    def signUp(self):
        self.name = input("Full name: ")
        self.email = input("Email: ")
        self.specialty = input("Specialty: ")
        self.qualification = input("Qualifications: ")
        self.yearsOfExperience = int(input("Years of experience: "))
        self.workingSchedule = int(input("Working schedule: "))

    def to_dict(self):
        return {
            "Full name": self.name,
            "Email": self.email,
            "Specialty": self.specialty,
            "YOE": self.yearsOfExperience,
            "WS": self.workingSchedule,
            "Qualification": self.qualification
        }

    def login(self):
        pass

    def confirm(self):
        pass

    def logout(self):
        pass

class Patient(User):
    pass

class Doctor(User):
    pass

class Appointment(User):
    pass

class Payment(User):
    pass

class Hospital(User):
    pass

end = User(1, 'Dara',  'Dentist', 'fm@gmail.com')
end.signUp()
print(end.to_dict())
print(end.name)