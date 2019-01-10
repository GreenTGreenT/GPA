import csv

data = []

def read_csv():
    with open('GPA.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            data.append(i) 
'''def write_csv():
    with open('GPA.csv', 'w') as f:
        writer = csv.writer(f) '''
        
          
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
    #print(data)
    term = input("Enter your term number: ")
    subject = input("Enter your subject: ")
    credit = input("Enter your credit: ")
    grade = input("Enter your grade: ")
    data.extend(([[term, subject, credit, grade]]))
    
    with open('GPA.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data) 
    #print(data)     

def save_csv():
    print("Toy s")

def main():
    print("Please choose your mode \n Edit(E) Insert(I) Save(s)")
    mode = input("Enter your mode: ").upper()
    if mode == "E":
        edit_csv()
    elif mode == "I":
        insert_csv()
    elif mode == "S":
        save_csv()
    else:
        print("Please try again")
        main()
main()


    
