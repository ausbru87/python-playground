animals_orig = [['dogs', 'puppies'], ['cats', 'kittens']]



# Shallow Copy using slice operator -- can get confusing with mutation
animals_copy = animals_orig[:]

# Deep Copy using accumulation and nested iteration
animals_deep_copy = []
for lst in animals_orig:
	copied_inner_list = []
	animals_deep_copy.append(copied_inner_list)
	for animal in lst:
		copied_inner_list.append(animal)


print('---- prints same items as orig ----')
print('###shallow###')
print(animals_copy)
print('###deep###')
print(animals_deep_copy)
print('---- they are not the same object ----')
print('###shallow###')
print(animals_copy is animals_orig)
print('###deep###')
print(animals_deep_copy is animals_orig)
print('---- they do have the same values ----')
print('###shallow###')
print(animals_copy == animals_orig)
print('###deep###')
print(animals_deep_copy == animals_orig)
# mutate orignal
animals_orig[0].append(['canines'])
print('---- print mutated orig ----')
print(animals_orig)
print('---- print mutated copy due to shallow copy ---')
print(animals_copy)
print('---- unaltered deep copy ----')
print(animals_deep_copy)