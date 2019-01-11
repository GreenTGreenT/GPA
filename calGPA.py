import csv
import operator

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
        #data = sorted(data, key = operator.itemgetter(0))
 
def edit_csv():
    read_csv()
    term = input("Enter term that you want to edit: ")

    print("----------------------------------------------------------------------------------")
    #print("|order|", "|term|", "|                     subject                    |", "|credit|", "|grade|")
    for i in range(len(data)):
        if data[i][0] == term:
            print("|  ", i, "  |", data[i][0], "|", data[i][1], "|", data[i][2], "|", data[i][3], "|")
    print("----------------------------------------------------------------------------------")
    edit_point = int(input("What's number you want to edit: "))
    for i in range(len(data)):
        if edit_point == i:
            subject = input("Enter your subject: ")
            credit = input("Enter your credit: ")
            grade = input("Enter your grade: ").upper()
            data[int(i)][1] = subject
            data[int(i)][2] = credit
            data[int(i)][3] = grade
            save_csv(term)

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
    #print(data)
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
            #print(grade.get(data[i][3]))
            sum_multiple += int(data[i][2]) * grade.get(data[i][3])
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


    
