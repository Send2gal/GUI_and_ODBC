__author__ = 'Gal'

import pyodbc
import os

server_Name = 'GAL-PC\SQLEXPRESS'
my_path = "c:\\temp\\"
row_counter = 1
calib_good  = 1
unit_dic = {}



conn = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = server_Name, database = 'Metrycom')
cursor = conn.cursor()

cursor.execute(" SELECT DISTINCT [MeasNumber] FROM Metrycom.dbo.TestResults WHERE TestId IN ('adc_calib_Pass_','vcc_calib_Pass_','id_calib_Pass_','vin_calib[3000]','vin_current_calib[15000]') and results = 1"  )
row = cursor.fetchone()

Meas_Number_calib_pass = []
while 1:
    row = cursor.fetchone()
    if not row:
        break
    row_counter += 1
    Meas_Number_calib_pass.append(row[0])

for Meas_Number in Meas_Number_calib_pass:
    #print Meas_Number
    cursor.execute(" SELECT  [MeasNumber],[date],[SerialNumber],[TestId],[Results] FROM Metrycom.dbo.TestResults WHERE \
                    ((TestId = 'adc_calib_adcb_offset1') OR (TestId = 'adc_calib_adca_offset3') OR \
                    (TestId = 'vcc_calib_factor1[4900]') OR (TestId = 'vcc_calib_factor2[4900]') OR (TestId = 'vcc_calib_factor3[4900]') OR \
                    (TestId = 'id_calib_factor1[8183]')  OR (TestId = 'id_calib_factor2[8183]') OR  (TestId = 'id_calib_factor3[8183]') OR \
                    (TestId = 'vin_voltage_calib_factor1[3000]') OR (TestId = 'vin_voltage_calib_factor2[3000]') OR (TestId = 'vin_voltage_calib_factor3[3000]') OR \
                    (TestId = 'vin_current_calib_factor1[15000]') OR (TestId = 'vin_current_calib_factor2[15000]') OR  (TestId = 'vin_current_calib_factor3[15000]')) AND \
                    (MeasNumber = ? )  ",Meas_Number)



    row = cursor.fetchone()
    while 1:
        row = cursor.fetchone()
        if not row:
            break
       # print row
        row_num_string = str(row[0])


        if  not unit_dic.has_key(row_num_string) :
            unit_dic[row_num_string]=[row_num_string]
            unit_dic[row_num_string] = [i for i in row][1:]
        else:
            unit_dic[row_num_string] += ([i for i in row][-2:])







#print "number or row =" ,row_counter
#print Meas_Number_calib_pass
print len(unit_dic)
for line in unit_dic:
    if len(unit_dic[line]) == 28:
        print "muser ",line,unit_dic[line]
        folder = "SU-"+unit_dic[line][1].replace(":","")[-4:]
        path = my_path + folder
        try:
            pass
            #print path
            #os.mkdir(path)
        except:
            pass
        #file = open(my_path + folder +"\\" + folder + ".csv" ,"w" )
        #file.write('This is a test\n')
        calib_good += 1

a = 28
for i in unit_dic['681']:
    print len(unit_dic['681'])- a
    print i
    a -= 1


print "number or row from DB =" ,row_counter
print "number or row calib good =" ,calib_good
print "end"

