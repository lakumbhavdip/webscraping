import myprice
city_name = input("enter city name ")

print("petrol price is ")
petrol_price = myprice.getpetrolprice(city_name)
print ('')
print("diesle price is ")
diesel_price = myprice.getdieselprice(city_name)
