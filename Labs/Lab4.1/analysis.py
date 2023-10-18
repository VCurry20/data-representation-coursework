# Analyise the date
# looking for the area of all hairdressers

from valoffdao import getAnalysis

data = getAnalysis()
# print (data)

totalArea = 0

for entry in data:
    # print (entry)
    valuationReports = entry["ValuationReport"]  # valuation reports is where the area is listed
    # print (valuationReports) # ck this works
    for valuationReport in valuationReports:
        # print(valuationReport)
        if valuationReport["FloorUse"] == "HAIR SALON":
            print (valuationReport["Area"], "+", totalArea, "=", end="") # print out how the answer worked out
            totalArea += valuationReport["Area"]
            print(totalArea)

print(totalArea)


# floating points are not accurate - DO NOT USE FOR MONEY / CURRENCY - do not use in PYTHON
# I double checked against the site 
# be aware the data might not be accurate
