#Scripts for the search

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
    if units in ["liters", "milliliters", "gallons", "pints"]:
        unitFamily="liquids"
        convertToLiters(quantity, units)
        
    elif units in ["kilograms", "grams", "tonnes", "stone", "pounds", "ounces"]:
        unitFamily="solids"
        convertToKilograms(quantity, units)
    else:
        unitFamily = "loose"

    #Convert to corresponding standard measure(liters, kilograms, pieces)
    #function convertToLiters
    #function convertToKilograms

    
    #Access database
        #Find carriers with end region in range
        #Find sellers within the ranges of carriers
        #Organise by quantity
        #find closest to required quantity

    #Return as JSON
    
