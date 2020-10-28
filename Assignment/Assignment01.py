# Problem 01
seconds_per_hour = 3600
seconds_per_day = 24 * seconds_per_hour
result = seconds_per_day / seconds_per_hour
print(result)

# Problem 02
year_lists = []
year_lists.append(1980)
for i in range(1, 5):
    year_lists.append(year_lists[i-1] + 1)

print(year_lists[3])

# Problem 03
f2e = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print(f2e['dog'])
keys = list(f2e.keys())
for i, value in enumerate(f2e.values()):
    if value == 'chien':
        print(keys[i])

# Problem 04
result = [i for i in range(11) if i%2 == 0]
print(result)
result2 = {i: i*i for i in range(10)}
print(result2)