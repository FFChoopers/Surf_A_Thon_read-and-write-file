#Read froma file and display one line at a time.
result_f = open("results.txt")
for line in result_f:
    print(line)
result_f.close()
#Find the highest score and convert data type from the Loop.
highest_score = 0
result_f = open("results.txt")
for line in result_f:
    if float(line) > highest_score :
       highest_score = float(line) 
result_f.close()
print("The highest score is: ")
print(highest_score)



#Testing split() method to cut the string 
rock_band = "Al Carl Mike Brian"
(a, b, c, d)= rock_band.split()
print(a)
print(d)