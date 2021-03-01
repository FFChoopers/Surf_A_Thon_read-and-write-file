#Read froma file and display one line at a time.
result_f = open("results.txt")
for line in result_f:
    print(line)
result_f.close()
#Find the top three scores by sorting data in a list.
scores = []
result_f = open("results.txt")
for line in result_f:
  #Split() method to cut the line in two, creating the name and score variables
  (name, score) = line.split()
  print(score)
  scores.append(float(score))
result_f.close()

print(scores)
scores.sort()
scores.reverse()
print(scores)
print(scores[0])
print(scores[1])
print(scores[2])




# #Testing split() method to cut the string 
# rock_band = "Al Carl Mike Brian"
# (a, b, c, d)= rock_band.split()
# print(a)
# print(d)