quote = ["le vrai malheur c'est d'être en valeur ", "l'or c'est toujour gagnant","le danger reste une condition",""
																												 "la santé est degradable", "le machinism est une philosophie"]

reponse_utilisater = input( " entrer un caractere : 	")


def show_random_quote(my_list):
	quote = my_list[1]
	return  quote

while (reponse_utilisater != "B"):
	print(show_random_quote(quote))
	reponse_utilisater = input(" entrer un caractere : 	")


for item in quote:
	item_c = item.capitalize()
	print(item_c)









