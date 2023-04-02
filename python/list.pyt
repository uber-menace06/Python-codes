from operator import le


marks= [95,98,97,"maths"]
print(marks[2])
print(marks)
print(marks[-1])#started from last
print(marks[0:2])
print(marks[1:2])
print(marks[1:6])


#to print all
for score in marks:
    print(score)


#to add at last
marks.append("physics")
marks.append(97)
print(marks)


#to insert in between
marks.insert(0, "math")
marks.insert(1, 99)
print(marks)

#to check whether available
print(99 in marks)

#calculate length
print(len(marks))


#now using while
mark=[1,5,9,67]
i=0
while i<len(mark):
    print(mark[i])
    i+=1

#to clear
mark.clear()
marks.clear()
print(mark)
print(marks)