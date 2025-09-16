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
        try:
            p_age = int(input("Age: "))
        except ValueError:
            print("Invalid age! Please enter a number.")
            return
        p_gender = input("Gender: ")
        p_email = input("E-mail: ")
        try:
            p_contact = int(input("Contact: "))
            p_emergency_contact = int(input("Emergency Contact: "))
        except ValueError:
            print("Contact must be numbers!")
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

    def main_menu(self):
        while True:
            print("""
                    -------MAIN MENU-------
                    1. Admin / Staff Login
                    2. Doctor Login
                    3. Patient Login
                    4. Exit
                """)
            option = input("Select an option(1-4): ")
            if option == '1':
                pass
            elif option == '2':
                doc = Doctor(self.user_id, self.name, "Doctor", self.email)
                doc.doc_menu()
            elif option == '3':
                pass
            elif option == '4':
                print("Thanks for visiting our hospital.....")
                break
            else:
                print("Inb=valid option, try again!")

class Patient(User):
    def patient_menu(self):
        print("""
                -------PATIENT MENU-------
                1. Book Appointment
                2. View Appointments
                3. View Bills
                4. View Medical History
                5. Back to Main Menu
            """)

class Doctor(User):
    def doc_menu(self):
        print("""
                -------DOCTOR MENU-------
                1. View Patients
                2. View Schedule
                3. Update Availability
                4. Back to Main Menu
            """)

class Appointment():
    def appointment_menu(self):
        print("""
                -------APPOINTMENT MENU-------
                1. Book Appointment
                2. View All APpointments
                3. Search Appointment (patient ID / doc ID)
                4. Reschedule Appointment
                5. Cancel Appointment
                6. Back to Hospital Menu
            """)

class Payment():
    def payment_menu(self):
        print("""
                -------PAYMENT MENU-------
                1. Make Payment
                2. View Payment History
                3. Back to Main Menu
            """)

class Hospital():
    def hospital_menu(self):
        print("""
                -------HOSPITAL MENU-------
                1. Doctor Management
                2. Patient Management
                3. Appointment Management
                4. Billing & Payments
                5. Back to Main Menu
            """)

end = User(1, 'Dara',  'Doctor', 'fm@gmail.com')
end.signUpPatient()
# print(end.to_dict())
# print(end.name)