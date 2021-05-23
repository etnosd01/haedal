import csv

...

for j in range(3):
    name = input("Name: ")
    skills = ['', '', '']
    for i in range(3):
        print(f"skill {i+1}: ", end='')
        skills[i] = input("")

    with open("pokemon.csv", 'a') as c:
        wr = csv.writer(c)
        wr.writerow([name, skills[0], skills[1], skills[2]])
