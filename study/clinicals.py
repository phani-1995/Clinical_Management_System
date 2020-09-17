import json

#Registering the Doctors
def get_inputs():
    #user input to record the log
    Doctor = input("Doctorname:")
    doctor_details1 =  {}
    doctor_details1['Doctor_Name'] = input('Enter the doctor name: ')
    doctor_details1['date'] = input('Enter a date in YYYY-MM-DD format:')
    doctor_details1['ID'] = input("ID:")
    doctor_details1['Specialization'] = input("Specialization:")
    doctor_details1['Availability'] = input("Availability(Y/N):")
    return(Doctor,doctor_details1)

out2 = {}

while True:
    exit = input('Do you want to add another input (y/n)? ')
    if exit.lower() == 'n':
        break
    else:
        Doctor, doctor_details1 = get_inputs()
        out2[Doctor] = doctor_details1

with open('doctor_details1.json','w') as f:
    json.dump(out2, f, indent=2)

