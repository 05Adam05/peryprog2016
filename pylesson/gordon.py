import json
menu = {
    'breakfast': {
        'time': 7.30,
        'item': ['яищница', "несквик"]
    },
    'lunch' : {
        'time': 12.00,
        'items': ["шаурма", "Лахмаджун", "напиток"]
    },
    'diner' : {
    'time': 20.30,
    'items': ['ролтон', 'соус с мясом']
    }

      
}

print(menu)

menu_json = json.dumps(menu)
print('_' * 50)
print(menu_json)
print('_' * 50)
menu2 = json.loads(menu_json)
print(menu2)

f1 = open('gandon.json', 'wt', encoding='utf-8')
f1.write(menu_json)
f1.close()

with open('gandon.json', 'rt', encoding='utf-8') as f2:
    menu3 = f2.read()
print(menu3)
menu3 = json.loads(menu3)
print(menu3)