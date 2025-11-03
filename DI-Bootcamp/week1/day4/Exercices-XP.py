
#exercice1
my_fav_numbers={5,2,9}
my_fav_numbers.add(6)
my_fav_numbers.add(2)
my_fav_numbers.remove(6)
friend_fav_numbers={10,15,20}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
# exercice 2
t=(1,2,3,4)
t=t+(5,)
print(t)
# exercice 3
basket=["Banana", "Apples", "Oranges", "Blueberries"]
if "Banana" in basket:
    basket.remove("Banana")
if "Blueberries" in basket:
    basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples") 
count_apples=basket.count("Apples")  
basket.clear()     
print(basket)
# exercciece 4
seq=[1.5+0.5*i for i in range(8)]
seq_alt=[i/2 for i in range(3,11)]
print(seq)
print(seq_alt)
# exercice5
for i in range(1,21):
    print(i,end=' ')
print()
nums=list(range(1,21)) 
even_indexed=[num for idx, num in enumerate(nums, start=1) if idx % 2 == 0]
print(even_indexed)  
# exercice6  