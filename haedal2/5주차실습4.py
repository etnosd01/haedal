import csv

with open("pokemon.csv", 'w') as c:
    wr = csv.writer(c)
    wr.writerow(['Name', 'skill 1', 'skill 2', 'skill 3'])
    