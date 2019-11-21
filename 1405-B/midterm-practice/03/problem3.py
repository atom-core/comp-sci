x = input("Enter an array: ")
y = input("Enter an array: ")

def jaccard(a, b):
    intersection = []
    union = []
    for i in a:
        if i not in union:
            union.append(i)
        if i in b and i not in intersection:
            intersection.append(i)
    for i in b:
        if i not in union:
            union.append(i)
        if i in a and i not in intersection:
            intersection.append(i)
    print(intersection)
    print(union)
    return len(intersection) / len(union)



print(jaccard(x, y))
