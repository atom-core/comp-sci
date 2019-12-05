def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        max_len = len(max(words, key=len))
        max_list = []
        for word in words:
            if len(word) == max_len and word not in max_list:
                max_list.append(word)
    return max_list

def shortest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        min_len = len(min(words, key=len))
        min_list = []
        for word in words:
            if len(word) == min_len and word not in min_list:
                min_list.append(word)
    return min_list

filename = input("Enter filename: ")
infile = open(filename, 'r')
data = infile.read()
char = len(data)
numwords = len(data.split(" "))
word_avg =  char / numwords

print("Number of words: " + str(numwords))
print("Longest word list: " + str(longest_words(filename)))
print("Shortest word list: " + str(shortest_words(filename)))
print("Average word length: " + str(word_avg))

infile.close()
