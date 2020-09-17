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

# x = input("Enter the Doctor specialization:")

# y = input("Enter the Doctor Availability(Y/N):")

#User want to search for a patient with respect to their problem

#z = input("Enter the patient problem:")



def check_specialist():
    try:
        x = input("Enter the Doctor specialization:")
        specialist = (data['Specialization'] == x) & (data['Availability'] == 'Y')
        #print(specialist.value_count())
        print("The specialist is available")
        # print(data[data['Doctor_Name', 'Specialization', 'Availability']])
    except SyntaxError:
        pass





















#
#
#
#
# doc = data[data['Specialization'].str.contains(x)]
# print(doc)
#
#
# fil_doc = doc[['Doctor_Name', 'Specialization', 'Availability', 'date']]
# print(fil_doc)
#
# print('---------------------------------------------------')
#
# pat = patients_data[patients_data['Problem'].str.contains(z)]
# fil_pat = pat[['PatientName', 'Mob_Num', 'Problem']]
# print(fil_pat)
#
# print('---------------------------------------------------')
#
# fil_doc.reset_index(drop=True, inplace=True)
# fil_pat.reset_index(drop=True, inplace=True)
# final = pd.concat([fil_doc, fil_pat], axis=1)
# print(final)
#


#def check_specialist():
#     res = final.isin([x, y]).any().any()
#     if res:
#         print('specialist is available')
#     else:
#         print('Specialist is not available')

#
# def check_availability():
#     if check_specialist():
#         res1 = final.isin(['Y']).any().any()
#         if res1:
#             print('Doctor is available')
#         else:
#             print('Doctor is not available')

# print('-----------------------------------------------------')
# print('|       The appointment details shown below         |')
# print('-----------------------------------------------------')

# try:
#     if check_specialist():
#         appointments = final[['Doctor_Name', 'Specialization', 'PatientName', 'Mob_Num', 'date']]
#         print(appointments)
# except IOError:
#     pass








#
# doc = data[data['Specialization'].str.contains(x)==True]
# if doc == True:
#     fil_doc = doc[['Doctor_Name', 'Specialization', 'Availability', 'date']]
# print(fil_doc)
#
#
#
# print('---------------------------------------------------')
#
# pat = patients_data[patients_data['Problem'].str.contains(y)]
# fil_pat = pat[['PatientName', 'Mob_Num', 'Problem']]
# print(fil_pat)
#
# print('---------------------------------------------------')
#
# fil_doc.reset_index(drop=True, inplace=True)
# fil_pat.reset_index(drop=True, inplace=True)
# fin1 = pd.concat([fil_doc, fil_pat], axis=1)
# print(fin1)
#
# def check_availability():
#     for i in fin1['Specialization']:
#         for j in fin1['Availability']:
#             if i == x and j == 'Y':
#                 print('Doctor is available ')
#             elif i == x and j == 'N':
#                 print('Doctor is not available')
#             else:
#                 print('No doctor found')
# check_availability()
# if check_availability():
#     print('--------------------------------------------------------')
#     print('|                Your Appointment details               |')
#     print('---------------------------------------------------------')
#     print(fin1[['Doctor_Name', 'Specialization', 'PatientName', 'Availability', 'Mob_Num', 'date'][0]])













#     try:
#         if 'Y' in data.values:
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
# # def cheking_specalist():
# #     for i in data['Specialization']:
# #         if i == x:
# #             print("Specialist is available")
# #         else:
# #             print("Specialist is not available")
#
#
# doc = data[data['Specialization'].str.contains(x)]
# fil_doc = doc[['Doctor_Name', 'Specialization', 'Availability', 'date']]
# print(fil_doc)
#
#
# print('---------------------------------------------------')
#
# pat = patients_data[patients_data['Problem'].str.contains(z)]
# fil_pat = pat[['PatientName', 'Mob_Num', 'Problem']]
# print(fil_pat)
#
# print('---------------------------------------------------')
#
# fil_doc.reset_index(drop=True, inplace=True)
# fil_pat.reset_index(drop=True, inplace=True)
# final = pd.concat([fil_doc, fil_pat], axis=1)
# print(final)
#
# print('----------------------------------------------------')
#
# print('The appointment details shown below')
#
# print('----------------------------------------------------')
#
# try:
#     if check_availability():
#         appointments = final[['Doctor_Name', 'Specialization', 'PatientName', 'Mob_Num', 'date']]
#         print(appointments)
# except IOError:
#     pass
