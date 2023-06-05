file1 = open('file1.txt', 'r')
data1 = file1.readlines()
d1 = [int(d.replace("\n","")) for d in data1]

file2 = open('file2.txt', 'r')
data2 = file2.readlines()
d2 = [int(d.replace("\n","")) for d in data2]

result = [n for n in d1 if n in d2]

# Write your code above 👆

print(result)