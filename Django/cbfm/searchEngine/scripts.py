#Scripts for the search

import mysql.connector

#Returns the quantity as a volume in liters
def convertToLiters(quantity, units):

    if units == "liter":
        return quantity * 1.0
    elif units == "milliliter":
        return quantity/1000.0
    elif units == "gallons":
        return quantity*4.54609
    elif units == "pints":
        return quantity/1.7598


def convertToKilograms(quantity, units):

    if units == "kilograms":
        return quantity*1.0
    elif units == "grams":
        return quantity/1000.0
    elif units == "tonnes":
        return quantity * 1000.0
    elif units == "stone":
        return quantity*6.35029
    elif units == "pounds":
        return quantity/2.20462
    elif units == "ounces":
        return quantity/35.274

def search(quantity, units, keywords, region, usertype):

    unitFamily = ""

    #Determine if liquid, solid or loose
    #Convert to corresponding standard measure(liters, kilograms, pieces)

    if units in ["liters", "milliliters", "gallons", "pints"]:
        unitFamily="liquids"
        convertToLiters(quantity, units)
        
    elif units in ["kilograms", "grams", "tonnes", "stone", "pounds", "ounces"]:
        unitFamily="solids"
        convertToKilograms(quantity, units)
    else:
        unitFamily = "loose"

        
    #function convertToLiters
    #function convertToKilograms


    #Access database


        
        cnx = mysql.connector.connect(user='root', password='cfg2014!', host='127.0.0.1', database='c4g', port='3306')

        cursor = cnx.cursor()

        query = ("SELECT User1, User2 FROM friendship ")

        cursor.execute(query)

        for (User1, User2) in cursor:
                print("User1: " + str(User1) + " |User2:  " + str(User2))
		print("")


        
        #Find carriers with end region in range
        #Find sellers within the ranges of carriers
        #Organise by quantity
        #find closest to required quantity

    #Return as JSON
    
