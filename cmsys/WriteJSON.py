def Write_Patients_DataBase(Patients_DataBase):
    myfile = open("Patients_DataBase.json", "w")
    for i in Patients_DataBase:
        myfile.write(
            str(i) + ";" + Patients_DataBase[i][0] + ";" + Patients_DataBase[i][1] + ";" + Patients_DataBase[i][
                2] + ";" + Patients_DataBase[i][3] + ";" + Patients_DataBase[i][4] + ";" + Patients_DataBase[i][
                5] + ";" + Patients_DataBase[i][6] + "\n")
    myfile.close()


def Write_Doctors_DataBase(Doctors_DataBase):
    myfile = open("Doctors_DataBase.json", "w")
    for i in Doctors_DataBase:
        myfile.write(str(i) + ";")
        for j in Doctors_DataBase[i]:
            myfile.write(str(j[0]) + ";" + j[1] + ";" + j[2] + ";")
        myfile.write("\n")
    myfile.close()
