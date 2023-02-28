kogus = input("Sisesta toode kogus: ")
hind = input("Sisesta toote hind: ")
Estonian_sales_tax = 0.2 # 20% on Eesti käibemaks

print("Kokkus: " + kogus)
print("Hind: " + hind)
print("Kokku: " + str(int(kogus) * int(hind) * (1 + Estonian_sales_tax)))