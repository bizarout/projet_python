import random
import json

quote = ["le vrai malheur c'est d'être en valeur ", "l'or c'est toujour gagnant","le danger reste une condition",""
																												 "la santé est degradable", "le machinism est une philosophie"]

reponse_utilisater = input( " entrer un caractere : 	")

def read_vaue_from_json():
	values = []
	with open('characters.json') as f:
		data =json.load(f)
		for entry in data :
			values.append(entry['quote'])
	return values

def random_character():
	all_values = read_vaue_from_json()
	return show_random_quote(all_values)



def show_random_quote(my_list):
	rand_num = random.randint(0, len(my_list)-1)
	quote = my_list[rand_num]
	return  quote

while (reponse_utilisater != "B"):
	print(show_random_quote(quote),random_character())
	reponse_utilisater = input(" entrer un caractere : 	")













