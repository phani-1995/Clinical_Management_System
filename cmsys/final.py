import ReadJSON
import WriteJSON


class clinicManagement(object):
    def AppointmentIndexInDoctorsDataBase(self, patient_ID):
        for i in Doctors_DataBase:
            for j in Doctors_DataBase[i]:
                if str(patient_ID) == str(j[0]):
                    Appointment_index = Doctors_DataBase[i].index(j)
                    return Appointment_index, i

    def admin(self):
        tries = 0
        print("-----------------------------------------")
        print("WARNING: Entering ADMIN MODE!")
        Password = input("Please enter your password: ")
        print("ADMIN MODE Initialised!")
        while True:
            if Password == "1234":
                print("-----------------------------------------")
                print("1.Manage Patients Info\n2.Manage Doctors Info\n3.Manage Appointments\nB.Go back")
                print("-----------------------------------------")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Patients Management
                    print("-----------------------------------------")
                    print(
                        "1.Enter Patients Details\n2.Display Patient Details\n3.Delete Patient Details\n4.Edit Patient Details\nB.Go Back")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Patients Management --> Enter new patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID in Patients_DataBase:  # if Admin entered used ID
                                patient_ID = int(input("This ID is unavailable, please try another ID : "))
                            Department = input("Enter Patient department                : ")
                            DoctorName = input("Enter name of doctor following the case : ")
                            Name = input("Enter Patient name                      : ")
                            Age = input("Enter Patient age                       : ")
                            Gender = input("Enter Patient gender                    : ")
                            Address = input("Enter Patient address                   : ")
                            RoomNumber = input("Enter Patient room number               : ")
                            Patients_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address,
                                                             RoomNumber]
                            print("----------------------Patient added successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Patients Management --> Display patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Patients_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter valid patient ID : "))
                            print("\nPatient name        : ", Patients_DataBase[patient_ID][2])
                            print("Patient age         : ", Patients_DataBase[patient_ID][3])
                            print("Patient gender      : ", Patients_DataBase[patient_ID][4])
                            print("Patient address     : ", Patients_DataBase[patient_ID][5])
                            print("Patient room number : ", Patients_DataBase[patient_ID][6])
                            print("Patient is in " + Patients_DataBase[patient_ID][0] + " department")
                            print("Patient is followed by doctor : " + Patients_DataBase[patient_ID][1])
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Patients Management --> Delete patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter Patient ID : "))
                            while patient_ID not in Patients_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            Patients_DataBase.pop(patient_ID)
                            print("----------------------Patient data deleted successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Patients Management --> Edit patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Patients_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            while True:
                                print("------------------------------------------")
                                print(
                                    "1.Edit Patient Department\n2.Edit Doctor Following The Case\n3.Edit Patient Name\n4.Edit Patient Age\n5.Edit Patient Gender\n6.Edit Patient Address\n7.Edit Patient RoomNumber\nB.Go Back")
                                print("-----------------------------------------")
                                Admin_choice = input("Enter your choice : ")
                                Admin_choice = Admin_choice.upper()
                                if Admin_choice == "1":
                                    Patients_DataBase[patient_ID][0] = input("\nEnter Patient department : ")
                                    print(
                                        "----------------------Patient Department Edited Successfully----------------------")

                                elif Admin_choice == "2":
                                    Patients_DataBase[patient_ID][1] = input("\nEnter Doctor following case : ")
                                    print(
                                        "----------------------Doctor follouing case Edited Successfully----------------------")

                                elif Admin_choice == "3":
                                    Patients_DataBase[patient_ID][2] = input("\nEnter Patient Name : ")
                                    print(
                                        "----------------------Patient Name Edited Successfully----------------------")

                                elif Admin_choice == "4":
                                    Patients_DataBase[patient_ID][3] = input("\nEnter Patient Age : ")
                                    print(
                                        "----------------------Patient Age Edited Successfully----------------------")

                                elif Admin_choice == "5":
                                    Patients_DataBase[patient_ID][4] = input("\nEnter Patient Gender : ")
                                    print(
                                        "----------------------Patient Address Gender Successfully----------------------")

                                elif Admin_choice == "6":
                                    Patients_DataBase[patient_ID][5] = input("\nEnter Patient Address : ")
                                    print(
                                        "----------------------Patient Address Edited Successfully----------------------")

                                elif Admin_choice == "7":
                                    Patients_DataBase[patient_ID][6] = input("\nEnter Patient RoomNumber : ")
                                    print(
                                        "----------------------Patient RoomNumber Edited Successfully----------------------")

                                elif Admin_choice == "B":
                                    break

                                else:
                                    print("Please Enter a correct choice")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "B":  # Admin mode --> Patients Management --> Back
                        break

                    else:
                        print("Please enter a correct choice\n")

                elif AdminOptions == "2":  # Admin mode --> Doctors Management
                    print("-----------------------------------------")
                    print(
                        "1.Enter Doctor Details\n2.Display Doctor Details\n3.Delete Doctor Details\n4.Edit Doctor Details\nB.Go back")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice: ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Doctors Management --> Enter new doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID: "))
                            while Doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                                Doctor_ID = int(input("This ID is unavailable, please try another ID : "))

                            Department = input("Enter Doctor department : ")
                            Name = input("Enter Doctor name       : ")
                            Address = input("Enter Doctor address    : ")
                            Doctors_DataBase[Doctor_ID] = [[Department, Name, Address]]
                            print("----------------------Doctor added successfully----------------------")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Doctors Management --> Display doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID: "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID! Please enter Doctor ID: "))
                            print("Doctor Name    : ", Doctors_DataBase[Doctor_ID][0][1])
                            print("Doctor Address : ", Doctors_DataBase[Doctor_ID][0][2])
                            print("Doctor is in " + Doctors_DataBase[Doctor_ID][0][0] + " department")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Doctors Management --> Delete doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter Doctor ID : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            Doctors_DataBase.pop(Doctor_ID)
                            print("/----------------------Doctor data deleted successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Doctors Management --> Edit Doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = input("Enter doctor ID : ")
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            print("-----------------------------------------")
                            print(
                                "1.Edit Doctor's Department\n2.To Edit Doctor's Name\n3.To Edit Doctor's Address\nB.Go Back")
                            print("-----------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                Doctors_DataBase[Doctor_ID][0][0] = input("Enter Doctor's Department : ")
                                print(
                                    "/----------------------Doctor's department edited successfully----------------------/")

                            elif Admin_choice == "2":
                                Doctors_DataBase[Doctor_ID][0][1] = input("Enter Doctor's Name : ")
                                print(
                                    "----------------------Doctor's name edited successfully----------------------")

                            elif Admin_choice == "3":
                                Doctors_DataBase[Doctor_ID][0][2] = input("Enter Doctor's Address : ")
                                print(
                                    "----------------------Doctor's address edited successfully----------------------")

                            elif Admin_choice == "B":
                                break

                            else:
                                print("\nPlease enter a correct choice\n")

                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "B":  # Back
                        break

                    else:
                        print("\nPlease enter a correct choice\n")

                elif AdminOptions == "3":  # Admin mode --> Appointment Management
                    print("-----------------------------------------")
                    print("1.Book an Appointment\n2.Edit an Appointment\n3.Cancel an Appointment\nB.Go Back")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()
                    if Admin_choice == "1":  # Admin mode --> Appointment Management --> Book an appointment
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter the ID of doctor : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
                            print("---------------------------------------------------------")
                            print(
                                "1.Book an appointment for an existing patient\n2.Book an appointment for a new patient\nB.Go Back")
                            print("---------------------------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                patient_ID = int(input("Enter Patient ID : "))
                                while patient_ID not in Patients_DataBase:  # if Admin entered incorrect ID
                                    patient_ID = int(input("Incorrect ID! Please enter a correct patient ID: "))


                            elif Admin_choice == "2":
                                patient_ID = int(input("Enter Patient ID : "))
                                while patient_ID in Patients_DataBase:  # if Admin entered used ID
                                    patient_ID = int(input("This ID is unavailable! Please try another ID: "))
                                Department = Doctors_DataBase[Doctor_ID][0][0]
                                DoctorName = Doctors_DataBase[Doctor_ID][0][1]
                                Name = input("Enter Patient name    : ")
                                Age = input("Enter Patient age     : ")
                                Gender = input("Enter Patient gender  : ")
                                Address = input("Enter Patient address : ")
                                RoomNumber = ""
                                Patients_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address,
                                                                 RoomNumber]

                            elif Admin_choice == "B":
                                break

                            Session_Start = input("Session starts at: ")
                            while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                Session_Start = input(
                                    "Appointments should be between 01:00PM to 10:00PM! Please enter a time between working hours: ")

                            for i in Doctors_DataBase[Doctor_ID]:
                                if type(i[0]) != str:
                                    while Session_Start >= i[1] and Session_Start < i[2]:
                                        Session_Start = input(
                                            "This appointment is already booked! Please Enter an other time for start of session: ")
                            Session_End = input("Session ends at: ")

                            New_Appointment = list()
                            New_Appointment.append(patient_ID)
                            New_Appointment.append(Session_Start)
                            New_Appointment.append(Session_End)
                            Doctors_DataBase[Doctor_ID].append(New_Appointment)
                            print("/----------------------Appointment booked successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Appointment Management --> Edit an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter Patient ID: "))
                            while patient_ID not in Patients_DataBase:
                                patient_ID = int(input("Incorrect ID! Please Enter correct patient ID: "))
                            try:  # To avoid no return function
                                AppointmentIndex, PairKey = self.AppointmentIndexInDoctorsDataBase(patient_ID)
                                Session_Start = input("Please enter the new start time: ")
                                while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                    Session_Start = input(
                                        "Appointments should be between 01:00PM to 10:00PM! Please enter a time between working hours: ")

                                for i in Doctors_DataBase[Doctor_ID]:
                                    if type(i[0]) != str:
                                        while Session_Start >= i[1] and Session_Start < i[2]:
                                            Session_Start = input(
                                                "This Appointment is already booked! Please enter an other time for start of session: ")
                                Session_End = input("Please enter the new end time : ")
                                Doctors_DataBase[PairKey][AppointmentIndex] = [patient_ID, Session_Start,
                                                                               Session_End]
                                print(
                                    "/----------------------Appointment Edited Successfully!----------------------/")
                            except:
                                print("No Appointment for this Patient")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Appointment Management --> Cancel an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID: "))
                            while patient_ID not in Patients_DataBase:
                                patient_ID = int(input("Incorrect ID! Enter patient ID: "))
                            try:
                                AppointmentIndex, PairKey = self.AppointmentIndexInDoctorsDataBase(patient_ID)
                                Doctors_DataBase[PairKey].pop(AppointmentIndex)
                                print(
                                    "/----------------------Appointment Cancelled Successfully----------------------/")
                            except:
                                print("No Appointment for this Patient!")
                        except:  # To avoid no return function
                            print("Patient ID should be an integer number!")

                    elif Admin_choice == "B":  # Back
                        break

                    else:
                        print("Please enter a correct option!")

                elif AdminOptions == "B":  # Back
                    break

                else:
                    print("Please enter a correct option!")

            elif Password != "1234":
                if tries < 2:
                    Password = input("Password Incorrect! Please try again: ")
                    tries += 1
                else:
                    print("Incorrect password! No more tries!")
                    break

            WriteJSON.Write_Patients_DataBase(Patients_DataBase)
            WriteJSON.Write_Doctors_DataBase(Doctors_DataBase)

    def user(self):
        print("USER MODE Initialized!")
        while True:
            print("\n-----------------------------------------")
            print(
                "1.Display Hospital Departments\n2.Display Hospital Doctors\n3.Display Patient's Address\n4.Display Patient's Details\n5.Display Doctor's Appointments\nB.Go Back")
            print("-----------------------------------------")
            UserOptions = input("Enter your choice: ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1":  # User mode --> view hospital's departments
                print("Hospital's Departments: ")
                for i in Doctors_DataBase:
                    print("	" + Doctors_DataBase[i][0][0])

            elif UserOptions == "2":  # User mode --> view hospital's Doctors
                print("Hospital's Doctors: ")
                for i in Doctors_DataBase:
                    print(
                        "	" + Doctors_DataBase[i][0][1] + " in " + Doctors_DataBase[i][0][
                            0] + " department, from " +
                        Doctors_DataBase[i][0][2])

            elif UserOptions == "3":  # User mode --> view patients' residents
                for i in Patients_DataBase:
                    print("	Patient : " + Patients_DataBase[i][2] + " in " + Patients_DataBase[i][
                        0] + " department and followed by " + Patients_DataBase[i][1] + ", age: " +
                          Patients_DataBase[i][3] + ", from: " + Patients_DataBase[i][5] + ", RoomNumber: " +
                          Patients_DataBase[i][6])

            elif UserOptions == "4":  # User mode --> view patient's details
                try:  # To avoid non integer input
                    patient_ID = int(input("Enter patient's ID: "))
                    while patient_ID not in Patients_DataBase:
                        patient_ID = int(input("Incorrect ID! Please enter patient ID: "))
                    print("	Patient Name        : ", Patients_DataBase[patient_ID][2])
                    print("	Patient Age         : ", Patients_DataBase[patient_ID][3])
                    print("	Patient Gender      : ", Patients_DataBase[patient_ID][4])
                    print("	Patient Address     : ", Patients_DataBase[patient_ID][5])
                    print("	Patient Room number : ", Patients_DataBase[patient_ID][6])
                    print("	Patient is in " + Patients_DataBase[patient_ID][0] + " department")
                    print("	Patient is followed by doctor : " + Patients_DataBase[patient_ID][1])
                except:
                    print("Patient ID should be an integer number")

            elif UserOptions == "5":  # User mode --> view doctor's appointments
                try:  # To avoid non integer input
                    Doctor_ID = int(input("Enter Doctor's ID: "))
                    while Doctor_ID not in Doctors_DataBase:
                        Doctor_ID = int(input("Incorrect ID! Please enter Doctor ID: "))
                    print(Doctors_DataBase[Doctor_ID][0][1] + " has appointments:")
                    for i in Doctors_DataBase[Doctor_ID]:
                        if type(i[0]) == str:
                            continue
                        else:
                            print("	from: " + i[1] + "    to: " + i[2])
                except:
                    print("Doctor's ID should be an integer number!")

            elif UserOptions == "B":  # Back
                break

            else:
                print("Please enter a correct choice!")

    def run(self):
        tries_flag = ""
        while not tries_flag:
            print("-----------------------------------------")
            print("1.ADMIN MODE\n2.USER MODE\nE.TO EXIT")
            print("-----------------------------------------")
            mode = input("Enter your choice: ")

            if mode == "1":  # Admin mode
                self.admin()

            elif mode == "2":  # User mode
                self.user()

            elif mode.upper() == "E":
                print("Exiting the program! Thank You!")
                break
            else:
                print("Invalid input! Try Again!")


start = clinicManagement()
print("Clinic Management System")
Patients_DataBase = ReadJSON.Read_Patients_DataBase()
Doctors_DataBase = ReadJSON.Read_Doctors_DataBase()
start.run()
