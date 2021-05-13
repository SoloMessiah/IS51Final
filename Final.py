"""
This program will display and calculate the number of grades, the average grade, and the 
percentage of grades that are the above the average grade. We will utilize two functions.
The first function will calculate the percentage that are above the average grade using loop.
The second function, the main function, will open the Final.txt file. This is where we will
comptute the average grade and the number of grades total. We will also display them to the
user using the following:

Number of grades:
Average grade:
Percentage of grades above average:
"""




"""
First function
calculate_percent_above_average()
    Set count = 0
    Use for loop to compare score in total_grades
        if score > average_grade
            increase count by 1
    return (count * 100) / len(total_grades)

Second function
main()
    Open Final.txt
    Set total_grades to a list

    print(Number of grades)

Calculate average grade next, still within main()
    Start average_grade off at 0
    for score in total_grades
        average_grade += score
    average_grade /= len(total_grades)

    print(Average grade)
    print(Percentage of grades above average)

    Close Final.txt

main()
"""





def calculate_percent_above_average(total_grades, average_grade):
    count = 0

    for score in total_grades:
        if score > average_grade:
            count += 1
    return (count * 100) / len(total_grades)


def main():
    open_final_txt = open("Final.txt")
    total_grades = []

    for line in open_final_txt:
        total_grades.append(int(line.strip()))
    
    print("Number of grades:", len(total_grades))

    average_grade = 0
    for score in total_grades:
        average_grade += score
    average_grade /= len(total_grades)

    print("Average grade:", average_grade)
    print("Percentage of grades above average:", round(calculate_percent_above_average(total_grades, average_grade),2),"%")

    open_final_txt.close()

main()