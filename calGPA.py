import csv

data = []

def read_csv():
    with open('GPA.csv', 'r') as f:
        read = csv.reader(f)
        for i in read:
            data.append(i) 
          
def grade_num():
    grade = {'A': 4,
             'B+': 3.5,
             'B': 3,
             'C+': 2.5,
             'C': 2,
             'D+': 1.5,
             'D': 1,
             'F': 0}

def edit_csv():
    print("Toy e")

def insert_csv():
    read_csv()
    term = input("Enter your term number: ")
    subject = input("Enter your subject: ")
    credit = input("Enter your credit: ")
    grade = input("Enter your grade: ")
    data.append([])
    for i in range(len(data)):
        data[i].extend((term, subject, credit, grade))
    #print(data[i])

        

def save_csv():
    print("Toy s")

def main():
    print("Please choose your mode \n Edit(E) Insert(I) Save(s)")
    mode = input("Enter your mode: ")
    if mode == "E" or "e":
        insert_csv()
    elif mode == "I" or "i":
        insert_csv()
    elif mode == "S" or "s":
        save_csv()
    else:
        print("Please try again")
        main()
main()


    
