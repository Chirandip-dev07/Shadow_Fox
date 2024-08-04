Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

city = input("Enter the name of the city : ")

if city in Australia:
    print(city,"is in Australia")
elif city in UAE:
    print(city,"is in UAE")
elif city in India:
    print(city,"is in India")
else:
    print("Wrong city entered")