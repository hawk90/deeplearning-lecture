things = ["mozzarella", "cinderella", "salomonella"]

print([word.capitalize() for word in things])
print([word.upper() for word in things])

del things[len(things) - 1]
print(things)

suprise = ["Groucho", "Chico", "Harpo"]

suprise[len(suprise) - 1] = suprise[len(suprise) - 1].lower()
suprise[len(suprise) - 1] = suprise[len(suprise) - 1][::-1]
suprise[len(suprise) - 1] = suprise[len(suprise) - 1].capitalize()

print(suprise)
