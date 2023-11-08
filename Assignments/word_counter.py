search_words = ["Python", "C", "OOP", "Hello", "Java"]
path = 'Assignments/input.txt'

#opening the file and sorting the lines in a list
with open(path, 'r') as file:
    word_list = file.read().splitlines()

#creating a list of words from input file which are all in lowercase
word_list_lower = []
for word in word_list:
    word_list_lower.append(word.lower())

#create dictionary the store the count of individual word
word_count_dic = {}

#counting the occurance of certain word in the list
for word in search_words:
    word_count_dic[word] = word_list_lower.count(word.lower())


for word in word_count_dic:
    print("{} -> {}".format(word, word_count_dic[word]))
