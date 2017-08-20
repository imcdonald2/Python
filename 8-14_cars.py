def cars(name, manufacturer, **additional_info):
    car_info = {}
    car_info['name_of_car'] = name
    car_info['manufacturer'] = manufacturer
    for key,value in additional_info.items():
        car_info[key] = value
    return car_info

car_input = cars('accent', 'hyundai',
                 color = 'grey',
                 year = '2003',
                 no_of_doors = '4')

print(car_input)
