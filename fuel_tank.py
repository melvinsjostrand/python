sek = 21.5
currency = input("Pick an currency, USD or SEK: ").lower()
litres = int(input("input amount of petrol in liters: "))

match currency:
    case "sek":
        print("Total cost in SEK: ", sek * litres)
        print(litres)
    case "usd":
        gallon = litres * 3.78541
        usd = (sek * litres) / 10.53
        print("Total cost in USD", usd)
        print(gallon)
    case _:
        print("invalid")