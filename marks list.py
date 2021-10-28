def status(marks):
    if marks>=35:
        s="P"
    else:
        s="F"
    return s
def find_grade(marks):
    if marks>=75:
        g="A+"
    elif marks>=60:
        g="A"
    elif marks>=50:
        g="B"
    else:
        if status(marks)=="F":
            g="F"
        else:
            "C"
    return g
s1,s2,s3,s4,s5,s6=map(int,input().split())
print("english",s1,100,status(s1),find_grade(s1))
print("Telugu",s2,100,status(s2),find_grade(s2))
print("Hindi",s3,100,status(s3),find_grade(s3))
print("Science",s4,100,status(s4),find_grade(s4))
print("Maths",s5,100,status(s5),find_grade(s5))
print("social",s6,100,status(s6),find_grade(s6))
        
        
        
        
    
