year_birth = 1980
years_list = [num for num in range(year_birth, year_birth + 5, 1)]
print(years_list[3])
max = 0
for i in range (0, 5):
    if years_list[i] > max:
        max = years_list[i]
print(max)
