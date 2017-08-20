def city_country(name, country):
    city_info = name.title() + ", " + country.title()
    return city_info

print(city_country('baltimore','united states'))
print(city_country('satiago', 'chile'))
print(city_country('tokyo', 'japan'))
