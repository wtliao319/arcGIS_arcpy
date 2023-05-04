import arcpy
import pandas as pd
import csv

'''
This python script is to convert point shape file to csv file.
'''


# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# set input and output
Krig_point = "\\path"
krig_output = "\\path"


# read the shp file and create a list
geo_list = []
fields = ['id','State','County' ,'Long', 'Lat', 'DataValue']

with arcpy.da.SearchCursor(Krig_copd_point, ["X", "STATE_NAME", "NAME","SHAPE@XY","RASTERVALU"]) as cursor:
    for r in cursor:
        g_id = r[0]
        s_name = r[1]
        c_name = r[2]
        x = r[3][0]
        y = r[3][1]
        value = r[4]

        geo_list.append([g_id,s_name,c_name ,x, y, value])


# write csv file
with open(krig_output, 'w') as file:
    # creating a csv writer object 
    csvwriter = csv.writer(file)

    #write the fields
    csvwriter.writerow(fields)

    # write rows
    csvwriter.writerows(geo_list)






