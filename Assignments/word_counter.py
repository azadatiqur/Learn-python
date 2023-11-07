search_words = ["Python", "C", "OOP", "Hello", "Java"]
path = 'Assignments/input.txt'

#opening the file and sorting the lines in a list
with open(path, 'r') as file:
    word_list = file.read().splitlines()

#create a list where the search_words items are in lowercase
search_words_lower = []
for word in search_words:
    search_words_lower.append(word.lower())

#create dictionary the store the count of individual word
word_count_dic = {}

#initially making the count 0
for word in search_words:
    word_count_dic[word] = 0

for word in word_list:
    if word.lower() in search_words_lower:
        word_count_dic[word] += 1

for word in word_count_dic:
    print("{} -> {}".format(word, word_count_dic[word]))
