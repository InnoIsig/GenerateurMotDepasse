import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



#liste pour le nombre de 0 à 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#liste pour les symboles
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenue sur le Générateur du mot de passe !")
nr_letters = int(input("Combien de lettre veux-tu pour le mot de pass ? 👇\n"))
nr_symbols = int(input(f"Combien de symboles veux-tu ? 👇\n"))
nr_numbers = int(input(f"Combien de nombre veux-tu ? 👇\n"))

Mot_de_passe_list = []

for char in range(1, nr_letters + 1):
    Mot_de_passe_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    Mot_de_passe_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    Mot_de_passe_list.append(random.choice(numbers))

print(Mot_de_passe_list)
random.shuffle(Mot_de_passe_list)
print(Mot_de_passe_list)

Mot_de_passe = ""
for char in Mot_de_passe_list:
    Mot_de_passe += char
print(f"Voici votre mot de passe 🧑🏿: {Mot_de_passe}")
