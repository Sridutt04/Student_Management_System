std=[]
def accept_det():
    id_no=int(input("Enter ID number of the student: "))
    name=input("Enter name of student: ")
    cls=int(input("Enter class of the student: "))
    age=int(input("Enter age of student: "))
    std.append({"ID":id_no,"Name":name,"class":cls,"Age":age})


def display_det():
    print("STUDENT DETAILS")
    for i in std:
        print("----------------------------------------------------")
        print(i)
        print("----------------------------------------------------")


def search_det():
    n1 = int(input("Enter the ID number of the required student: "))
    for i in std:
        if i["ID"]==n1:
            print("----------------------------------------------------")
            print(i)
            print("----------------------------------------------------")


def delete_det():
    n1 = int(input("Enter the ID number of the required student: "))
    for i in std:
        if i["ID"]==n1:
            std.remove(i)

            
def update_det():
    n1=int(input("Enter the ID number of the required student: "))
    for i in std:
        if i["ID"]==n1:
            name=input("Enter name of student: ")
            cls = int(input("Enter class of the student: "))
            age=int(input("Enter age of student: "))
            i["Name"]=name
            i["Class"]=cls
            i["Age"]=age
            ("----------------------------------------------------")
            print(i)
            print("----------------------------------------------------")


while True:
    ID=int(input("""    1. Accept Details
    2. Display Details
    3. Search Details
    4. Delete Details
    5. Update Details  
    6. Exit
    Enter Choice: """))
    if ID==1:
        accept_det()
    elif ID==2:
        display_det()
    elif ID==3:
        search_det()
    elif ID==4:
        delete_det()
    elif ID==5:
        update_det()
    elif ID==6:
        print("Thank you")
        break
    else:
        print("Invalid Choice")
