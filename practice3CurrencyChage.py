with open("currencyData.txt") as f:
    lines = f.readlines()
    #print(lines)

print("Welcome to the money exchange converter.\nThis program will help you to convert the money rate.")
currencyDictionary = {}
for line in lines:
    parsed = line.split("\t")
    currencyDictionary[parsed[0]] = parsed[1]
    #print(parsed)
    #print(currencyDictionary)
#print(currencyDictionary)

totalAmount = float(input("Enter the desired Nepalese amount: "))
print("Give us the name of currency to which you want to convert??\n")
#print(item) for item in CurrencyDictionary
[print(item) for item in currencyDictionary.keys()]
currency = input("enter the currency: ")

result = totalAmount * float(currencyDictionary[currency])

print(f"{totalAmount} Nepalese rupees is equal to {result} {currency}")





