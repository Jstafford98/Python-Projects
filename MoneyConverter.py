import csv

file_name = 'moneyconversion.csv'
currency_list = []
monetary_spacing = 13


#This data type is used to represent a currency and stores it's conversion rate from the USD and it's currency code
class coin:

    def __init__(self, code, rate, year):
        self.mCode = code
        self.data = {year: rate}
    def addAnnualValues(self, year, rate):
        self.data[len(self.data)] = {year : rate}

#This function loads currency data from a specified year, defined in the parameter. Loaded data is stored in the currency_list object
def loadAllCurrencyData():

    print("Attempting to open",file_name,". . .")
    with open(file_name, newline='') as csvfile:
        fileReader = csv.reader(csvfile, delimiter="\t")
        fileReader.__next__()
        print("File found!")
        for x in fileReader:
            code, year, rate = x
            if not currency_list:
                currency_list.append(coin(code, rate, year))
                #TODO come back cause you can probably optimize here
            elif any(t.mCode == code for t in currency_list):
                  for x in currency_list:
                    if x.mCode == code:
                      x.addAnnualValues(year,rate)      
            else:
               currency_list.append(coin(code, rate, year))

#This main function prompts the user for the year to retrieve currency data from using the loadCurrencyData function and a monetary amount in USD. The equivalent value of the specified amount
#in each currency is then printed to the console
def main():

    loadAllCurrencyData()
    amount = 100 #eval(input("Enter your amount in USD:")
    print("|","Code".center(5),"|","2014".center(monetary_spacing),"|","2015".center(monetary_spacing),"|","2016".center(monetary_spacing),"|","2017".center(monetary_spacing),"|","2018".center(monetary_spacing),"|","2019".center(monetary_spacing),"|")
    print("".center(105,'-'))
    for x in currency_list:
      print("|",x.mCode.center(6),end = '|')
      for i in range(2014,2020):
        temp = amount * x.data.get(str(i),1)
        print("${:,}".format(round(temp,2)).center(monetary_spacing+2) , end='|')
      print()
      print("".center(105,'-'))

main()
