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

    def signUpDoctor(self):
        d_name = input("Full name: ")
        d_email = input("Email: ")
        d_specialty = input("Specialty: ")
        d_qualification = input("Qualifications: ")
        d_yearsOfExperience = int(input("Years of experience: "))
        d_workingSchedule = int(input("Working schedule: "))

        doctor_info = {
            "Name" : d_name,
            "Email" : d_email,
            "Specialty" : d_specialty,
            "Qualification" : d_qualification,
            "YOE" : d_yearsOfExperience,
            "WS" : d_workingSchedule
        }

        # print(doctor_info["Qualification"])

    def signUpPatient(self):
        p_name = input("Fullname: ")
        p_age = int(input("Age: "))
        p_gender = input("Gender: ")
        p_email = input("E-mail: ")
        p_contact = int(input("Contact: "))
        p_emergency_contact = int(input("Emergency Contact: "))
        p_blood_group = input("Blood Group (e.g A+, A-, B+, B-, O+, O-, AB+, AB-): ")

        patient_info = {
            "Name": p_name,
            "Age" : p_age,
            "Gender" : p_gender,
            "Email" : p_email,
            "Contact" : p_contact,
            "Emergency Contact" : p_emergency_contact,
            "Blood Group" : p_blood_group
        }

        # print(patient_info["Name"])

    def signUpStaff(self):
        pass

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
end.signUpPatient()
# print(end.to_dict())
# print(end.name)