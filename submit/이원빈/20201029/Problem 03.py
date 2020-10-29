def func():
    return ['Harry', 'Ron', 'Hermione']

title=['Creature of Habit', 'Crewel Fate']
plots=['A turns into a mon ster', 'A haunted yarn shop']
movies = {title[i]:plots[i] for i in range(0, 2)}

title = ['Creature of Habit', 'Crewel Fate', 'Apple']
plots = ['A turns into a mon ster', 'A haunted yarn shop', '']
movies2 = {title[i]:plots[i] for i in range(0, 3)}
for key in movies2.keys():
    print(movies2[key])
