#Scripts for the search

def convertToLiters(quantity, units):

def convertToKilograms(quantity, units)

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
    
