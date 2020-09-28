L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

#count how many letters of each

d = {}
for x in L:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1

print("--- no sort ---")
for x in d.keys():
	print("{} appears {} times".format(x, d[x]))

print("--- sorted by key std ---")
for x in sorted(d.keys()):
	print("{} appears {} times".format(x, d[x]))

print("--- sorted by key value low to high ---")
for x in sorted(d.keys(), key=lambda k:d[k]):
    print("{} appears {} times".format(x, d[x]))

print("--- sorted by key value high to low ---")
for x in sorted(d.keys(), key=lambda k:d[k], reverse=True):
    print("{} appears {} times".format(x, d[x]))


# Breaking Ties
print("##### BREAKING TIES #####")


fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

# order by len of the fruit_name str (low to high) and then by alpha of the fruit_name
print("--- sorted by len: low to high, then alpha ---")
new_order = sorted(fruits, key=lambda fruit_name:(len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# order by len of the fruit_name str (high to low) and then by alpha of the fruit_name
print("--- sorted by len: high to low, then alpha ---")
new_order = sorted(fruits, key=lambda fruit_name:(-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# order by len of the fruit_name str (high to low) and then by reverse alpha order of the fruit_name
print("--- sorted by len: high to low, then reverse alpha ---")
new_order = sorted(fruits, key=lambda fruit_name:(-len(fruit_name), fruit_name), reverse = True)
for fruit in new_order:
    print(fruit)

# weather and dict example
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

print("--- weather locations ---")
sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
for location in sorted_weather:
    print(location)


#outer limits of lambda complexity to read

states = {"Colorado": ["Denver", "Aurora", "Littleton"],
			"Arizona": ["Phoenix", "Tuscon", "Prescot"],
			"Whyoming": ["Casper", "Cheyenne", "Jackson Hole"]}
print("--- states sorted with lambda ---")
print(sorted(states, key=lambda state: len(states[state][0])))


# use a named func
states = {"Colorado": ["Denver", "Aurora", "Littleton", "Arvada"],
            "Arizona": ["Phoenix", "Tuscon", "Prescot", "Avon"],
            "Whyoming": ["Casper", "Cheyenne", "Jackson Hole"]}
def a_cities_count(city_list):
	count = 0
	for city in city_list:
		if city[0].lower() == 'a':
			count += 1
			print(city)
			print(count)
	return count
		

print("--- states sorted with lambda ---")
print(sorted(states, key = lambda state: a_cities_count(states[state])))