def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        sortedwords = sorted(words, key=len) 
    return sortedwords[0]

def shortest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        sortedwords = sorted(words, key=len) 
    return sortedwords[-1]

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
