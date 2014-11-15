#Scripts for the search

import mysql.connector
import json

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

    menteeName = ""   
    menteeGraduate = False
    menteeLocation = ""


    menteeEmail = ""
    Quantity = ""
    MenteeEmail = ""
    Matchs = False

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
        unitFamily="liters"
        convertToLiters(quantity, units)
        
    elif units in ["kilograms", "grams", "tonnes", "stone", "pounds", "ounces"]:
        unitFamily="kilograms"
        convertToKilograms(quantity, units)
    else:
        unitFamily = "pieces"

        
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
                query = ("SELECT Name, Quantity, Email FROM products WHERE MenteeEmail = '" + str(individual.Email) + "'")

                cursor.execute(query)

                #
                #
                #
                #HERE 
                #
                #
                #
                #

                for Name, Quantity, Email in cursor:
                    individualProduct = product()
                    individualProduct.Name = Name
                    individualProduct.MenteeEmail = Email
                    individualProduct.Quantity = Quantity
                    individualProduct.menteeName = (individual.Firstname + individual.Lastname)
                    individualProduct.menteeGraduate = individual.Graduate
                    individualProduct.menteeLocation = individual.Location

                    products.append(individualProduct)

                individual.Products = products
                
            
            
    #Check for matching with keywords and their products

    keywordList = split(keywords, " ")

    for i in range[len(sellers)]:
        for j in range[len(sellers[i].Products)]:
            for k in range[len(keywordList)]:
                if keywordList[k] in sellers[i].Products[j].Name:
                    sellers[i].Products[j].Matchs = True


    #Check for region matching that of viable carriers
    finalListProducts = []

    for i in range[len(sellers)]:
        for j in range[len(sellers[i].Products)]:
            for k in range[len(viableCarriers)]:
                if sellers[i].Products[j].Matchs == True:
                    if sellers[i].Location in viableCarriers.Location:
                        finalListProducts.append(sellers[i].Products[k])
                    
    #Organise by quantity

    finalListProducts.sort()

    finalListProducts[::-1]
                
    #find closest to required quantity

    targetSum = Quantity
    suggestList = []
    for i in range[len(finalListProducts)]:

        if finalListProducts[i].Quantity < targetSum:
            targetSum = targetSum - finalListProducts[i].Quantity
            suggestList.append(finalListProducts[i])

    #Return as JSON
    

        #JSON suggestList

        #JSONfinalListProducts



#iterate
    for i in range[len(suggestList)]:
        suggestDict = {'unitvalue': suggestList[i].Quantity, 'unit': unitFamily, 'keyword' : suggestList[i].Name, 'meName' : suggestList[i].menteeName, 'region' : suggestList[i].Location, 'carrier' : viableCarrier[0], 'qualitymatch' : 0}

    for i in range[len(finalListProducts)]:
        finalDict = {'unitvalue': finalListProducts[i].Quantity, 'unit': unitFamily, 'keyword' : finalListProducts[i].Name, 'meName' : finalListProducts[i].menteeName, 'region' : finalListProducts[i].Location, 'carrier' : viableCarrier[0], 'qualitymatch' : 1}
                               
    JSONDICT = {'success' : 1, 'data' : [suggestDict + finalDict]}

    return HttpResponse(json.dump(JSONDICT))
    
