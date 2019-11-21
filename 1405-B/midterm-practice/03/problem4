str_arg = input("Enter a string: ")
int_arg = input("Enter an integer: ")

def x_most_frequent(s, x):
    frequency = {}
    for word in s.split():
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    frequency_list = []
    while len(frequency_list) < int(x):
        largest = 0
        largest_word = ""
        for word in frequency:
            if frequency[word] > largest:
                largest = frequency[word]
                largest_word = word
        del frequency[largest_word]
        frequency_list.append(largest_word)
    return frequency_list

print(x_most_frequent(str_arg, int_arg))
