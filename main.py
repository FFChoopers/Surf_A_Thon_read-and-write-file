#Read froma file and display one line at a time.
result_f = open("results.txt")
for line in result_f:
    print(line)
result_f.close()
#Find the highest score and convert data type from the Loop.
highest_score = 0
result_f = open("results.txt")
for line in result_f:
  #Split() method to cut the line in two, creating the name and score variables
  (name, score) = line.split()
  if float(score) > highest_score :
       highest_score = float(score) 
result_f.close()
#Display the result 
print("The highest score is: ")
print(highest_score)



# #Testing split() method to cut the string 
# rock_band = "Al Carl Mike Brian"
# (a, b, c, d)= rock_band.split()
# print(a)
# print(d)