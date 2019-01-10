import csv

data = []
grade = {"A": 4,
         "B+": 3.5,
         "B": 3,
         "C+": 2.5,
         "C": 2,
         "D+": 1.5,
         "D": 1,
         "F": 0}

def read_csv():
    with open('GPA.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            data.append(i) 
                  
'''def grade_num(num):
    grade = {"A": 4,
             "B+": 3.5,
             "B": 3,
             "C+": 2.5,
             "C": 2,
             "D+": 1.5,
             "D": 1,
             "F": 0}
    return grade[num]'''

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
    #print(data)
    print("Please enter Q when you finish")
    while True:
        
        term = input("Enter your term number: ").upper()
        subject = input("Enter your subject: ").upper()
        credit = input("Enter your credit: ").upper()
        grade = input("Enter your grade: ").upper()
       
        '''if term == "Q":
            break
        elif subject == "Q":
            break
        elif credit == "Q":
            break
        elif grade == "Q":
            break'''
        data.append([term, subject, credit, grade])
       
        break         
    #print(data)   
    save = input("If you want to save, please enter S: ").upper 
    if save == "S":
        save_csv()

def save_csv():
    with open('GPA.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data) 

def calculation():
    read_csv()
    term = input("Please enter you term: ")
    sum_multiple = 0
    sum_credit = 0
    for i in range(len(data)):
        if data[i][0] == term:
            if data[i][2].isnumeric():
                sum_multiple += int(data[i][2]) * grade.get(data[i][3])
                sum_credit += int(data[i][2]) 
                result = sum_multiple / sum_credit
    #print(sum_multiple)
    print(result)
        
def main():
    print("Please choose your mode \n Edit(E) Insert(I)")
    mode = input("Enter your mode: ").upper()
    if mode == "E":
        edit_csv()
    elif mode == "I":
        insert_csv()
    elif mode == "C":
        calculation()
    else:
        print("Please try again")
        main()
main()


    
