def sandwich_item(bun, meat, cheese, **toppings):
    assembled_sandwich = {}
    assembled_sandwich['bread_type'] = bun
    assembled_sandwich['meat'] = meat
    assembled_sandwich['cheese'] = cheese
    for key, value in toppings.items():
        assembled_sandwich[key] = value
    return assembled_sandwich

order1 = sandwich_item('brioche', 'hamburger', 'cheddar',
                      topping1 = 'lettuce',
                      topping2 = 'tomato')

print(order1)

order2 = sandwich_item('garlic bread', 'chicken', 'mozzerella',
                       topping1 = 'marinara sauce')

print(order2)
