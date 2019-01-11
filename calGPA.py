import csv

data = []
result = []
total_credit = []
grade = {"A": 4,
         "B+": 3.5,
         "B": 3,
         "C+": 2.5,
         "C": 2,
         "D+": 1.5,
         "D": 1,
         "F": 0}

def read_csv():
    with open('grade.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            data.append(i) 
                  
def grade_num(num):
    grade = {"A": 4,
             "B+": 3.5,
             "B": 3,
             "C+": 2.5,
             "C": 2,
             "D+": 1.5,
             "D": 1,
             "F": 0}
    return grade[num]

def edit_csv():
    read_csv()
    ask = int(input("Enter term that you want to edit: "))
    subject = input("Enter your subject: ")
    credit = input("Enter your credit: ")
    grade = input("Enter your grade: ")
    for i in range(len(data)):
        if data[ask] == data[0]:
            data[ask][1] = subject
            data[ask][2] = credit
            data[ask][3] = grade
            print(data[ask][3])

def insert_csv():
    read_csv()
    print("If you want to save, please enter S \n if you want to exit, please enter Q")
    num_subject = int(input("Enter total number of your subjects: "))
    for i in range(num_subject):        
        term = input("Enter your term number: ")
           
        subject = input("Enter your subject: ")
           

        credit = input("Enter your credit: ")
        


        grade = input("Enter your grade: ").upper()
        data.append([term, subject, credit, grade])
              
    save = input("Do you want to save?: ").upper()
    if save == "S":
        save_csv(term)
    elif save == "Q":
        exit()

    
def save_csv(term):
    with open('grade.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    calculation(term)
    
def calculation(term):
    sum_multiple = 0
    sum_credit = 0
    to_result = 0
    
    for i in range(len(data)):
        if data[i][0] == term:
            if data[i][2] is not None or data[i][3] is not None:
                sum_multiple += int(data[i][2]) * grade_num(data[i][3])
                sum_credit += int(data[i][2]) 
                to_result = sum_multiple / sum_credit
    print("You GPA is ", "%.2f " % to_result)
                 
        
def main():
    print("Please choose your mode \n Edit(E) Insert(I)")
    mode = input("Enter your mode: ").upper()
    if mode == "E":
        edit_csv()
    elif mode == "I":
        insert_csv()
    elif mode == "C":
        calculation()
    elif mode == "S":
        save_csv()
    else:
        print("Please try again")
        main()
main()


    
