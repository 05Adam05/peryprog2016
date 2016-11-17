import json

menu = {
	'breakfast': {
		'time': 7.00,
		'items': ['каша','чай']	
	},
	'lunch' : {
		'time': 13.00,
		'items': ['Суп','Плов','Кола']
	}
	
}

print(menu)
menu_json = json.dumps(menu)
print('-'*20)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

file = open('menu1.json','wt', encoding= 'utf-8')
file.write(menu_json)
file.close()


file = open('menu1.json','rt', encoding= 'utf-8')
menu3 = file.read()
file.close() 
menu3 = json.loads(menu3)
print(menu3)
