'''Python Data Structures Assignment'''


## 1. Lists

# ### Create an empty list named `a`, then print its value and type.

a = []
print(a)
print(type(a))


# ### Create `languages`, count its elements, and iterate through it.

languages = ['R', 'Python', 'SAS', 'Scala', 42]
print(languages)

print(len(languages))

for language in languages:
    print(language)


# ### Select the second item and store it in `temp`; print its value and type.

temp = languages[1]
print(temp)
print(type(temp))


# ### Append `Java`, remove `42`, and print the updated list.

languages.append('Java')
print(languages)

languages.remove(42)
print(languages)


# ### Work with colors: append, insert, extend, count, and sort.

colors = ['Red', 'Blue', 'White']
print(colors)

colors.append('Black')
print(colors)

colors.insert(1, 'Orange')  # Insert at index 1 (second position)
print(colors)

print(colors)

colors2 = ['Grey', 'Sky Blue']
print(colors2)

colors.extend(colors2)
print(colors)

print("Number of colors:", len(colors))
for color in colors:
    print(color)

colors.sort()
print(colors)


# ### Split a sentence into words, convert words to lowercase, check membership, remove a word, slice, and join.  Note: The sentence does not contain the word `country`, so the membership test returns `False`.

sent = 'Coronavirus Caused Lockdowns Around The World.'
print(sent)

words = sent.split()
print(words)

words_lower = [word.lower() for word in words]
print(words_lower)

print('country' in words_lower)

# Remove 'the' if it is present
if 'the' in words_lower:
    words_lower.remove('the')
print(words_lower)

x4 = words_lower[:4]
print(x4)

sentence_again = ' '.join(words_lower)
print(sentence_again)


# ## 2. Sets


# ### Convert a list of grades into a set to remove duplicates.

stud_grades = ['A', 'A', 'B', 'C', 'C', 'F']
print(stud_grades)

print(len(stud_grades))

stud_grades_set = set(stud_grades)
print(stud_grades_set)

print(type(stud_grades))
print(type(stud_grades_set))
print("List elements:", stud_grades)
print("Set elements:", stud_grades_set)


# Sets remove duplicate values and do not guarantee display order.

stud_grades_set.add('G')
print(stud_grades_set)

stud_grades_set.add('F')  # F is already present, so the set stays unchanged
print(stud_grades_set)

stud_grades_set.discard('F')
print(stud_grades_set)

print("Elements:", stud_grades_set)
print("Length:", len(stud_grades_set))


# ### Set operations: union, intersection, and difference.

colors = ['red', 'blue', 'orange']
fruits = ['orange', 'grapes', 'apples']
print("Colors:", colors)
print("Fruits:", fruits)

colors_set = set(colors)
fruits_set = set(fruits)
print("Colors set:", colors_set)
print("Fruits set:", fruits_set)

print("Union:", colors_set.union(fruits_set))

print("Intersection:", colors_set.intersection(fruits_set))

print("Fruits but not colors:", fruits_set.difference(colors_set))


# ## 3. Tuples


# ### Create a list, iterate over it, and change its first element.

temp = [17, 'Virat', 50.0]
print(temp)

for item in temp:
    print(item)

temp[0] = 11
print(temp)


# ### Convert the list to a tuple and observe that tuples are immutable.

temp1 = tuple(temp)
print(temp1)

for item in temp1:
    print(item)

# Tuples cannot be modified after creation.
# Uncomment the next line to see the TypeError:
# temp1[0] = 17


# ### Create tuples for cities and combine them into a nested tuple.

city = ("Bangalore", 28.9949521, 72)
print(city)

print(city[0])

city2 = ("Chennai", 30.01, 74)
print(city2)

cities = (city, city2)
print(cities)

print(type(cities[0]))

print(type(cities))


# ## 4. Dictionaries


# ### Create a dictionary and access values using keys.

d = {
    "actor": "amir",
    "animal": "cat",
    "earth": 2,
    "list": [23, 32, 12]
}
print(d)


# A dictionary is accessed by keys, not numeric positions. `d[0]` raises a `KeyError` because key `0` is not present.

actor = d['actor']
print(actor)

print(type(actor))

List = d['list']
print(List)

print(type(List))


# ### Merge another dictionary into `d`, then print its keys and values.

d1 = {
    'singer': 'Kr$na',
    'album': 'Still here',
    'genre': 'hip-hop'
}
print(d1)

d.update(d1)
print(d)

print(d.keys())

print(d.values())

for key, value in d.items():
    print(f"{key} ----> {value}")


# ### Count the occurrences of each character in `sent` using a dictionary.

sent = "Coronavirus Caused Lockdowns Around The World."
char_count = {}

for char in sent:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)



