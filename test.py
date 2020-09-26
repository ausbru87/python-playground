import requests
import json
import random

## Transformation/Mapping Example ##

things = [2,5,9]

yourlist = [value * 2 for value in things]
print(yourlist)

# these are equal statements

yourlist = map(lambda value: value*2, things)

## Filter Example ##
def keep_evens(nums):
	new_list = [num for num in nums if num % 2 == 0]
	return new_list

def keep_evens_filt(nums):
	new_list = filter(lambda num: num % 2 == 0, nums)
	return list(new_list)



print(keep_evens([3,4,6,7,0,1]))
print(keep_evens_filt([3,4,6,7,0,1]))


L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [x for x in L if x > 10]

print(lst2)


import json


tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

print(json.dumps(tester['info'], indent=2))


compri = [d['name'] for d in tester['info']]
print(compri)


seq1 = [1,2,4,7]
seq2 = [1,2,3,4]
seq3 = [] #acum
seq4 = []

for i in range(len(seq1)):
	seq3.append(seq1[i] + seq2[i])

print(seq3)

# Zip
print(list(zip(seq1, seq2)))

# remember unpacking a tuple
for (x1, x2) in list(zip(seq1, seq2)):
	seq4.append(x1 + x2)

print(seq4)

# Zip w/ List Comp
print([x1 + x2 for (x1, x2) in list(zip(seq1, seq2))])

# hangman blanked
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

def possible_zip(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible_zip("wonderwall", "_on__r__ll", "otnqurl"))
print(possible_zip("wonderwall", "_on__r__ll", "wotnqurl"))


## EX

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

# if L1[i] > 10
# if L2[i] < 5

print([num_l1 + num_l2 for (num_l1, num_l2) in zip(L1, L2) if num_l1 > 10 and num_l2 < 5])


print("############# NEW SECTION ###################")


l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

def flt_3(lst):
    return list(filter(lambda elem: len(elem[0]) > 3 and len(elem[1]) > 3, lst))

combo_lst = zip(l1,l2)

opposites = flt_3(combo_lst)



'''
opposites = [(el1, el2) for (el1, el2) in zip(l1,l2) if len(el1) > 3 and len(el2) > 3]




print(opposites)

'''
correct = [('left', 'right'), ('front', 'back')]

print(correct)

if opposites == correct:
    print(True)
else:
    print(False)



d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)


def get_translate(word):
    baseurl = "https://api.datamuse.com/words"
    params_dict = {}
    #params_dict["v"] = "es"
    #params_dict["topics"] = "love"
    params_dict["rel_rhy"] = word
    params_dict["max"] = "10"
    resp = requests.get(baseurl, params_dict)
    word_resp = resp.json()
    #print(resp.url)
    print("... loading")
    if word_resp == []:
        return word
    else:
        return word_resp[random.randrange(len(word_resp))]['word']

def translate_paragraph(paragraph):
    return " ".join([get_translate(word) for word in paragraph.split()])


old_text = "Sunset is the time of day when our sky meets the outer space solar winds. There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons caught in a whirlwind. The sun moves slowly to hide behind the line of horizon, while the moon races to take its place in prominence atop the night sky. People slow to a crawl, entranced, fully forgetting the deeds that must still be done. There is a coolness, a calmness, when the sun does set."

print(translate_paragraph(old_text))






