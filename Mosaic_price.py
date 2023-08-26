from math import ceil

length_yard = int(input("enter length of yard:")) 
width_yard = int(input("enter width of yard :")) 
length_mosaic = int(input("enter length of mosaic:")) / 100
width_mosaic = int(input("enter width of mosaic:")) / 100

prise = int(input("enter prise:"))

area_yard = length_yard * width_yard * 2
area_mosaic = length_mosaic * width_mosaic * 2

amount_mosaic = ceil(area_yard / area_mosaic) 
total_prise = amount_mosaic * prise

print('you need {0} mosaic'.format(amount_mosaic))
print("total prise is : {0}".format(total_prise))


