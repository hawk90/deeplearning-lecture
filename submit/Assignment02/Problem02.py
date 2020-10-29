things = ["mozzarella", "cinderella", "salomonella"]

answer2 = []
answer3 = []

for word in things:
    word = word[0].upper() + word[1:]
    answer2.append(word)
    answer3.append(word.upper())

print(answer2, '\n', answer3)

things.pop()
print(things)

suprise = ["Groucho", "Chico", "Harpo"]
tmp = suprise[-1].lower()[::-1]
result = tmp[0].upper() + tmp[1:]
print(result)

def f1():
    return ["Harry", "Ron", "Hermione"]

titles = ["Creature of Habit", "Crewel Fate"]
plots = ["A turns into a mom ster", "A haunted yarn shop"]
movies = {title : plot for title in titles for plot in plots}
print(movies)

titles = ["Creature of Habit", "Crewel Fate", "Apple"]
plots = ["A turns into a mom ster", "A haunted yarn shop"]

movies2 = {title : plot for title in titles for plot in plots if plot != ''}
print(movies2)

for i in range(len(titles)):
    try:
        plots[i] != ''
        movies2[titles[i]] = plots[i]
    except:
        movies2[titles[i]] = ''
print(movies2)

for key in movies2.keys():
    print(movies2[key])
