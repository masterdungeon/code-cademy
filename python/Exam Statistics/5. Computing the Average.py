grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    sum=0
    for score in scores:
        sum=sum+score
    return sum

#grades_sum(grades)
 
def grades_average(grades):
    sum=0
    sum=grades_sum(grades)
    avg=sum/float(len(grades))
    return avg
    
print grades_average(grades)