#==========================================
# exercice 1
#==========================================
keys=['Ten','Twenty','Thirty']
values=[10,20,30]
my_dict= dict(zip(keys,values))
print(my_dict)
#=============================================
#exercice2
#=============================================
family={"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost=0
for name, age in family.items():
    if age<3:
        price=0
    elif 3<= age <= 12:
        price=10
    else:
        price=15
    print(f"{name} doit payer {price}")
    total_cost+=price
print("Coût total :", total_cost)    
#==============================================
# exercice 3
# ===============================================
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"]=2
print(f"Les clients de zara sont : {', '.join(brand['type_of_clothes'])}")  
brand["country_creation"]="Spain"  
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
brand.pop("creation_date")
print("Dernier concurrent :", brand["international_competitors"][-1])
print("Couleurs anx us :", brand["major_color"]["US"])
print("Nombre de clés :", len(brand))
#prime
more_on_zara={"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print(brand)
#=============================================
# exercice 4
# ===========================================
users=["Mickey", "Minnie", "Donald", "Ariel", "pluto"] 
disney_users_A={name: i for i, name in enumerate(users)}
print(disney_users_A)
disney_users_B = {i: name for i, name in enumerate(users)}
print(disney_users_B)
sorted_users = sorted(users)
disney_users_C = {name: i for i, name in enumerate(sorted_users)}
print(disney_users_C)