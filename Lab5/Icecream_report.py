def main():
    salesData = readData(".\\icecream report\\icecream.txt")
    printReport(salesData)

def readData(filename):
    salesData = {}

    infile = open(filename, "r")

    for line in infile:
        fields = line.split(":")
        flavor = fields[0]
        salesData[flavor] = buildList(fields)

    infile.close()
    return salesData

def buildList(fields):
    storeSales = []
    for i in range (1, len(fields)):
        sales = float(fields[i])
        storeSales.append(sales)

    return storeSales


def printReport(salesData):
    numStores = 0
    for storeSales in salesData.values():
        if len(storeSales) > numStores:
            numStores = len(storeSales)

    storeTotals = [0.0] * numStores
    
    for flavor in sorted(salesData):
        print("%-15s" % flavor, end="")

        flavorTotal = 0.0
        storeSales = salesData[flavor]
        for i in range(len(storeSales)):
            sales = storeSales[i]
            flavorTotal = flavorTotal + sales
            storeTotals[i] = storeTotals[i] + sales
            print("%10.2f" % sales, end="")

        print("%15.2f" % flavorTotal)

    print("%15s" % "", end="")
    for i in range(numStores):
        print("%10.2f" % storeTotals[i], end="")
    print()

main()