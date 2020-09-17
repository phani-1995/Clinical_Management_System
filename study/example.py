import pandas as pd
print("The Doctors related data")
#Reading doctors data
df = pd.read_json('doctor_details1.json')
data = df.T
data.reset_index(drop=True, inplace=True)
print(data)

print('---------------------------------------------')
print("The Patient related data")

#Reading patients data
df1 = pd.read_json('Patient_details.json')
data1 = df1.T
patients_data = data1.rename({'Mobile Number': 'Mob_Num'}, axis=1)
patients_data.reset_index(drop=True, inplace=True)
print(patients_data)

print('-------------------------------------------')

#User want to search doctor with their specilization and availability
x = input("Enter the Doctor specialization:")
#y = input("Enter the Doctor Availability(Y/N):")
# def avail_check():
#     avail = data[data['Availability'].str.contains(y)]
#     if avail:
#         return True
#     return False

#User want to search for a patient with respect to their problem
z = input("Enter the patient problem:")

# def check_availability():
#     try:
#         if avail_check():
#             print('Doctor is available')
#             print('-------------------')
#             return True
#         else:
#             print('Doctor is not available')
#             print('-----------------------')
#             return False
#     except IOError:
#         pass
#
# print('-----------------------------------------------')


def check_specialist():
    try:
        x = input("Enter the Doctor specialization:")
        specialist = (data['Specialization'] == x) & (data['Availability'] == 'Y')
        #print(specialist.value_count())
        print("The specialist is available")
        # print(data[data['Doctor_Name', 'Specialization', 'Availability']])
    except SyntaxError:
        pass


doc = data[data['Specialization'].str.contains(x)]
fil_doc = doc[['Doctor_Name', 'Specialization', 'Availability', 'date']]
print(fil_doc)

print('---------------------------------------------------')

pat = patients_data[patients_data['Problem'].str.contains(z)]
fil_pat = pat[['PatientName', 'Mob_Num', 'Problem']]
print(fil_pat)

print('---------------------------------------------------')


fil_doc.reset_index(drop=True, inplace=True)
fil_pat.reset_index(drop=True, inplace=True)
final = pd.concat([fil_doc, fil_pat], axis=1)
print(final)

print('----------------------------------------------------')

print('The appointment details shown below')

print('--------------------------------------------')

try:
    if check_availability():
        appointments = final[['Doctor_Name', 'Specialization', 'PatientName', 'Mob_Num', 'date']]
        print(appointments)
except IOError:
    pass
