menu = {
	"breakfast": {
		'hours': '8:00',
		'items': [ 'Яихница','Чай']
	},
	'lunch': {
		'hours': '12:00',
		'items': ['Шамбургер', 'Суп', 'Компот']
	}
}
print(menu)
import json
menu_json = json.dumps(menu)
print(menu_json)
with open('menu.json','wt',encoding='utf-8') as f1:
	f1.write(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

with open('menu.json', 'rt',encoding='utf-8') as f2:
	menu3 = f2.read()

menu3 = json.loads(menu3) 
print(menu3)
