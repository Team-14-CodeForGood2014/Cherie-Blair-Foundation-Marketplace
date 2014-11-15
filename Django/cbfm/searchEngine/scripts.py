#Scripts for the search

import mysql.connector


class carrier():

     Name = ""
     Email = ""
     Location = []

class seller():

    Firstname = ""
    Surname = ""
    Email = ""
    Graduate = False
    Location = ""

    Products = []

class product():

    Name = ""
    Quantity = ""

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

def search(quantity, units, keywords, endRegion, usertype):

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


        
        #carrier query
        carriers = []
        query = ("SELECT Name, Email, Location FROM carrier")

        cursor.execute(query)

        for (Name, Email, Location) in cursor:
            individual = carrier()
            individual.Name = Name
            individual.Email = Email
            individual.Location = split(Location, ",").trim()
            carriers.append(individual)



        #Find carriers with end region in range
        viableCarriers = []

        for i in range(len(carriers)):
            for j in range(len(carriers[i].Location)):
                if carriers[i].Location[j].lower() == endRegion:
                    viableCarriers.append(viableCarriers[i])


        
        #Find sellers within the ranges of carriers

        #Get sellers
            
        sellers = []
        query = ("SELECT Firstname, Surname, Email, Graduate, Location FROM mentee")

        cursor.execute(query)

        for Firstname, Surname, Email, Graduate, Location in cursor:
            individual = seller()
            individual.Firstname = Firstname
            individual.Surname = Surname
            individual.Email = Email
            individual.Graduate = Graduate
            individual.Location = Location

            #Prevents non graduated accounts from being shown
            if individual.Graduate == True or (usertype == "mentee" or usertype == "mentor"):
            
                #Get products of user
                products = []
                query = ("SELECT Name, Quantity, MenteeEmail FROM products WHERE MenteeEmail = '" + str(individual.Email) + "'")

                cursor.execute(query)

                for Name, Quantity in cursor:
                    individualProduct = product()
                    individualProduct.Name = Name
                    individualProduct.Quantity = Quantity

                    products.append(individualProduct)

                individual.Products = products
                
            
            
            #Check for matching with keywords and their products
            #Check for region matching that of viable carriers

                    
        #Organise by quantity
        #find closest to required quantity

    #Return as JSON
    
