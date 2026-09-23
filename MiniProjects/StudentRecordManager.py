
# conditional - logic
# loops - menu system
# dictionary - store data

# what we can do 

# teacher:
# 1) add student
# 2) remove student
# 3) search the stundent 
# 4) view all students
# 5) check result
# 6) exit


students = {}

while True:

    print("=====================STUDENT RECORD MANAGER==============")

    print("1) Add ")
    print("2) Remove ")
    print("3) Search ")
    print("4) Display")
    print("5) Check result")
    print("6) Exit")


    choice = input("ente your choice:")

    if choice == "1":
         sid = int(input("enter the id :"))
         n = input("enter the name:")
         std = input("enter the standard:")

         m = []

         l1 = int(input("Emter Marathi marks:"))
         m.append(l1)
         h = int(input("enter Hindi marks:"))
         m.append(h)
         e = int(input("enter english marks:"))
         m.append(e)
         maths =int(input("enter maths marks:"))
         m.append(maths)
         s1 =int(input("enter science marks:"))
         m.append(s1)
         s2 = int(input("enter social science marks:"))
         m.append(s2)

         students[sid] = {
              "name":n,
              "class": std,
              "marks":m
         }

         print("Record inserted successfully")


    elif choice == "2":
         sid = int(input("enter the sid for remove:"))

         if sid in students:
              del students[sid]
              print("Record deleted successfully")
         else:
              print("record not found")

    elif choice =="3":

          sid = int(input("enter the sid for search:"))
         
          if sid in students:
                print(" record found successfully")
                for sid in students.keys(): # here students.keys() retuns the [key1,key2,...] as like
                              print("Student ID:", sid)
                              print("Name:", students[sid]["name"])
                              print("Class:", students[sid]["class"])
                              print("Marks:", students[sid]["marks"])
                              print()
          else:
               print("record not found")
             
    elif choice == "4":

         for sid, student in students.items(): # here sid:101 and student have the nested dictionary key value
                print("Student ID:", sid)
                print("Name:", student["name"])
                print("Class:", student["class"])
                print("Marks:", student["marks"])
                print()


    elif choice == "5":
         sid = int(input("enter the sid for check result:"))

         if sid in students:
              print("=======================================================================")
              print("result")
              print("studentId:",sid)
              print("name:",students[sid]["name"])
              print("class:",students[sid]["class"])
              print("marks:")
              print("firstlanguage:",students[sid]["marks"][0])
              print("Secondlanguage:",students[sid]["marks"][1])
              print("English:",students[sid]["marks"][2])
              print("Maths:",students[sid]["marks"][3])
              print("Science:",students[sid]["marks"][4])
              print("Social Science:",students[sid]["marks"][5])
              total = sum(students[sid]["marks"])
              percentage = (600/total)*100

              if percentage > 35:
                   print("percentage:",percentage)
                   print("Grade:Pass")
              else:
                   print("percentage:",percentage)
                   print("Grade:Fail")
         else:
              print("record not found")

    elif choice == "6":
         print("exit...")
         break


              
