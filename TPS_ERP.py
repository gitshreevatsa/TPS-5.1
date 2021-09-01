dict = {}
stud_dict = {}
for i in range(2019, 2022):
    print("Year- " + str(i))
    Year = i
    u1 = int(input("Number of students in UG 2nd year: "))
    u2 = int(input("Number of students in UG 3rd year: "))
    u3 = int(input("Number of students in UG 4th year: "))
    p1 = int(input("Number of students in PG 1st year: "))
    p2 = int(input("Number of students in PG 2nd year: "))
    F = int(input("Total number of faculty in the department: "))
    S= u1 + u2 + u3 + p1 + p2
    SFR = S/F
    SFR = "{:.2f}".format(SFR)
    print("Number of Students in the Department: " + str(S))
    print("Student Faculty Ratio: " + str(SFR))
    dict[Year] = float(SFR)
    stud_dict[Year] = {}
    stud_dict[Year]['u2'] = u1
    stud_dict[Year]['u3'] = u2
    stud_dict[Year]['u4'] = u3
    stud_dict[Year]['p1'] = p1
    stud_dict[Year]['p2'] = p2
    stud_dict[Year]['F'] = F
    stud_dict[Year]['S'] = S
    stud_dict[Year]['SFR'] = SFR 

print(dict)
print(stud_dict)
Average_SFR = dict[2019]+ dict[2020]+ dict[2021]
Average_SFR = Average_SFR/3
Average_SFR = "{:.2f}".format(Average_SFR)
print("Average SFR = " + str(Average_SFR))

if(float(Average_SFR) <= 15):
    Score = 20
    print("Score= " + str(Score) + " Marks")
elif(float(Average_SFR) <= 17):
    Score = 18 
    print("Score= " + str(Score) + " Marks")
elif(float(Average_SFR) <= 19):
    Score = 16 
    print("Score= " + str(Score) + " Marks")
elif(float(Average_SFR) <= 21):
    Score = 14
    print("Score= " + str(Score) + " Marks")
elif(float(Average_SFR) <= 23):
    Score = 12
    print("Score= " + str(Score) + " Marks")
elif(float(Average_SFR) <= 25):
    Score = 10
    print("Score= " + str(Score) + " Marks")
else:
    Score = 0
    print("Score= " + str(Score) + " Marks")
