import json

#Registering the patient
def get_inputs():
    #user input to record the log
    Patient = input("PatientName:")
    Patient_details =  {}
    Patient_details['PatientName'] = input('Enter a patient name:')
    Patient_details['ID'] = input("ID:")
    Patient_details['Mobile Number'] = input("Mobile Number:")
    Patient_details['Age'] = input("Age:")
    Patient_details['Problem'] = input("Problem:")
    return(Patient,Patient_details)

out1 = {}

while True:
    exit = input('Do you want to add another input (y/n)? ')
    if exit.lower() == 'n':
        break
    else:
        Patient, Patient_details = get_inputs()
        out1[Patient] = Patient_details

with open('Patient_details.json','w') as f:
    json.dump(out1, f, indent=2)

