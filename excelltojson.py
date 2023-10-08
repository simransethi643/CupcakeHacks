# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 20:51:15 2023

@author: jaime
"""
import json
import pandas as pd
import re
file_location = 'C:\\Users\\jaime\\OneDrive\\Documents\\hackathon2023\\ArcCubeGMUHackathonPlotData-Take1-5Oct2023.xlsx'
sheet = pd.read_excel(file_location)
firstCol= sheet.iloc[:,0]
secondCol= sheet.iloc[:,1]
thirdCol = sheet.iloc[:,2]
fourCol = sheet.iloc[:,3]
fiveCol = sheet.iloc[:,4]
sixCol = sheet.iloc[:,5]
sevenCol = sheet.iloc[:,6]



longitudes=[]
latitudes =[]

#print(thirdCol)


newData = []


#getting info from second row
for i in range(len(firstCol)):
    stringIn2 = str(secondCol[i])
    if "Month" in stringIn2:
        internalDic2={}
        strCol2 = re.findall("\d+",stringIn2)
               
        internalDic2.update({'Month':strCol2[0] })
    if "Minute" in stringIn2:
        
        strCol22 = re.findall("\d+",stringIn2)
               
        internalDic2.update({'Minute':strCol22[0] })
    if "accel" in stringIn2:
        
        strCol23 = re.findall("\d+",stringIn2)
               
        internalDic2.update({'accely':strCol23[0] })
        newData.extend([internalDic2])

#getting info from first column
entriesCount =0
for i in range(len(firstCol)):
    str1 = str(firstCol[i])
    if "Year" in str1:
        str11 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Year':str11[0]})
        
    if "Hour" in str1:
        str12 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Hour':str12[0]})
        
    if "Satellite Count" in str1:
        str13 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Satellite Count':str13[0]})
        
        #print(str1)
    if "Latitude" in str1:
        
    
        str14 = re.findall("\d+\.\d+",str1)
#        
#        newData[entriesCount].update({'latitude1':str14})
        if str14:
            newData[entriesCount].update({'latitude1': str14[0]})
        else:
    # Handle the case where no latitude is found in the string
            newData[entriesCount].update({'latitude1': None})
    
    if "Longitude" in str1:
        str15 = re.findall("\d+\.\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Longitude':str15[0]})
        #print(str1)
    
    
#    if "HDOP" in str1:
#        
#        
#    
#        str16 = re.findall("\d+",str1)
#               
#        #internalDictionary.update({'latitude':str2[0] })
#        newData[entriesCount].update({'HDOP':str16[0]})
    if "Course" in str1:
        
        
    
        str17 = re.findall("\d+\.\d+",str1)
               
        #internalDictionary.update({'latitude':str2[0] })
        newData[entriesCount].update({'Course in degrees':str17[0]})
    
    
    
    
   
    if "Speed" in str1:
        str18 = re.findall("\d+\.\d+",str1)
        #internalDictionary.update({'speed':str5[0]})
        newData[entriesCount].update({'speed':str18[0]})
    if "Altitude" in str1:
        str19 = re.findall("\d+\.\d+",str1)
               
        #internalDictionary.update({'Altitude(unit feet)':str4[0] })
        newData[entriesCount].update({'Altitude':str19[0]})
    
    if "LightSensor" in str1:
        str110 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Light Sensor':str110[0]})
        #print(str1)
        
    if "accelX" in str1:
        str111 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'accelX':str111[0]})
    
    if "temperature" in str1:
        str112 = re.findall("\d+\.\d+",str1)
               
        
        #internalDictionary.update({'temperature':str6[0]})
        newData[entriesCount].update({'temperature':str112[0]})
        
    if "pressure" in str1:
        str113 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'pressure':str113[0]})
    
    if "altitude" in str1:
        str114 = re.findall("\d+\.\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'altitude':str114[0]})
        
    if "humidity" in str1:
        str115 = re.findall("\d+\.\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'humidity':str115[0]})
        
    if "Sensor operating status" in str1:
        str116 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Sensor operating status':str116[0]})
        
    if "Air quality" in str1:
        str117 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Air quality':str117[0]}) 
        
    if "Concentration" in str1:
        str118 = re.findall("\d+",str1)
               
        
        #internalDictionary.update({'longitude':str3[0]})
        newData[entriesCount].update({'Concentration':str118[0]})

               
        
    if "Carbon" in str1:
        str119 = re.findall("\d+",str1)
        #internalDictionary.update({'carbon':str7[0]})
        newData[entriesCount].update({'carbon':str119[0]})
        entriesCount +=1
entriesCount = 0
for i in range(len(firstCol)):
    stringIn3 = str(thirdCol[i])
    
    if "Day" in stringIn3:
        str1col3 = re.findall("\d+",stringIn3)
        newData[entriesCount].update({'day':str1col3[0] })
         
    if "Second" in stringIn3:
        str2col3 = re.findall("\d+",stringIn3)
        newData[entriesCount].update({'second':str2col3[0] })
         
    if "accelZ" in stringIn3:
        str3col3 = re.findall("\d+",stringIn3)      
        newData[entriesCount].update({'accelZ':str3col3[0] })
        entriesCount +=1
        
           
        
        
entriesCount = 0        
for i in range(len(firstCol)):
    stringIn4 = str(fourCol[i])
    
    if "Centisecond" in stringIn4:
        
        str1col4 = re.findall("\d+",stringIn4)
        newData[entriesCount].update({'centisecond':str1col4[0] })
         
    if "temp" in stringIn4:
        str2col4 = re.findall("\d+\.\d+",stringIn4)
        newData[entriesCount].update({'temp':str2col4[0] })
        entriesCount +=1
        
        

        
entriesCount = 0   
for i in range(len(firstCol)):
    stringIn5 = str(fiveCol[i])
    
    if "gyroX" in stringIn5:
        str1col5 = re.findall("\d+",stringIn5)
        newData[entriesCount].update({'gyroX':str1col5[0] })
        entriesCount +=1
   
        
        
entriesCount = 0    
for i in range(len(firstCol)):
    stringIn6 = str(sixCol[i])
    
    if "gyroY" in stringIn6:
        str1col6 = re.findall("\d+",stringIn6)
        newData[entriesCount].update({'gyroY':str1col6[0] })
        entriesCount +=1
   
        
  
entriesCount = 0    
for i in range(len(sevenCol)):
    stringIn7 = str(sevenCol[i])
    
    if "gyroZ" in stringIn7:
        str1col7 = re.findall("\d+",stringIn7)
        newData[entriesCount].update({'gyroZ':str1col7[0] })
        entriesCount +=1
   

    
print(newData)

with open ("example1.json","w") as outfile:
    json.dump(newData,outfile)