file = input("Enter a filename: ")
key = input("Enter a keyword to search for: ")

def search_employees(filename,keyword):
    names_list = []
    for line in open(filename):
        name = (line.strip().split(",")[1])
        if keyword.lower() in name.lower():
            names_list.append(name)
    return names_list

def analyze_pay(filename):
    pay_array = []
    total_pay = 0
    count = 0
    f = open(filename)
    for lines in filename:
        line = f.readline()
        while line != "":
            pay = line.split(",")[2]
            total_pay += float(pay)
            pay_array.append(float(pay))
            count += 1
            line = f.readline()
    average_pay = total_pay / count
    pays_list = [average_pay, max(pay_array), min(pay_array)]
    return pays_list

print(search_employees(file, key))
print(analyze_pay(file))
