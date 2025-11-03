# exerccie 1 
my_fav_numbers={3,7,21}
my_fav_numbers.add(42)
my_fav_numbers.add(7)
my_fav_numbers.remove(42)
friend_fav_numbers={5,7,99}
our_fav_numbers= my_fav_numbers.union(friend_fav_numbers)
print(my_fav_numbers, friend_fav_numbers, our_fav_numbers)
# exercice 2
t=(1,2,3)
t=t+(4,)
print(t)
# exercice 3
basket=["Banana", "Apples", "Oranges", "Blueberries" ]
if "Banana" in basket:
    basket.remove("Banana")
if "Blueberries" in basket:
    basket.remove("Blueberries")  
basket.append("Kiwi") 
basket.insert(0,"Apples") 
count_apples= basket.count("Apples")
basket.clear()
print("Apples count:", count_apples)
print("Final basket:", basket)
# exercie 4
seq=[1.5+0.5*i for i in range(8)]
seq_alt=[i/2 for i in range(3,11)]
print(seq)
# exercice5
for i in range(1,21):
    print(i, end=' ')
print() 
nums=list(range(1,21)) 
even_indexed=[num for idx, num in enumerate(nums, start=1) if idx % 2 == 0]
print(even_indexed)
#Exercice 6
while True:
    name = input("Entrez votre nom : ").strip()
    if len(name) >= 3 and not any(ch.isdigit() for ch in name):
        print("merci")
        break
    else:
        print("Nom invalide — il doit contenir au moins 3 lettres et aucun chiffre. Réessayez.")
# exercice 7
fruits_input= input("Entrez vos fruits préférés ( séparés par des espaces) : ").strip()
fav_fruits= fruits_input.split()
chosen= input("Entrez le nom d'un fruit : ").strip()
if chosen in fav_fruits:
    print("you chose one of your favorite fruits! Enjoy!")
else:
    print("you chose a new fruit. I hope you enjoy it!")    
# exerccie 8
toppings=[] 
while True:
    top=input("Entrez un ingrédient('quit' pour arrêter) : ").strip() 
    if top.lower()=='quit':
        break
    toppings.append(top)
    print(f"Adding {top} to your pizza.")
print("\nListe finale des garnitures:", toppings)  
price=10+2.5*len(toppings)
print(f"prix total: ${price:.2f}") 
# exercice9
def calculate_cinema_price(ages):
    total=0
    for age in ages:
        if age<3:
            price=0
        elif 3<= age <=12:
            price=10
        else:
            price=15
        total+=price
    return total
sample_ages=[2,4,34,12,15] 
print("Total:", calculate_cinema_price(sample_ages))              
group = [14, 16, 18, 21, 22, 17]
allowed = [age for age in group if 16 <= age <= 21]
print("Allowed:", allowed)