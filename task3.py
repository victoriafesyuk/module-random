import random
result = random.choice(["орел", "решка"])
print(result)


orel = 0
reshka = 0

for i in range(100):
    result = random.choice(["орел", "решка"])

    if result == "орел":
        orel += 1
    else:
        reshka += 1

print("Кількість орлів:", orel)
print("Кількість решок:", reshka)

for i in range(1000):
    result = random.choice(["орел", "решка"])

    if result == "орел":
        orel += 1
    else:
        reshka += 1

print("Кількість орлів:", orel)
print("Кількість решок:", reshka)