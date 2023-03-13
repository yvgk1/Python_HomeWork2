# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak
# kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

print("             Student Register System         ")

students=[]
studentsList=["a"]
students=studentsList


# Aldığı isim soy isim ile listeye öğrenci ekleyen
def addStudents():
    nameAndSurname=str(input("Enter the student name and surname : "))
    students.append(nameAndSurname)
addStudents()
print(studentsList)

# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def removeList():
    studentsList=str(input("Enter the name and surname to be removed : "))
    students.remove(studentsList)
removeList()
print(studentsList)

# Listeye birden fazla öğrenci eklemeyi mümkün kılan
def  addMultiple():
    multiple=int(input(f"Enter the student to be added : "))
    for i in range(multiple):
        addStudents()
addMultiple()
print(studentsList)

# Listedeki tüm öğrencileri tek tek ekrana yazdıran
def printAllStudent():
    for students in studentsList:
        print(students)
printAllStudent()

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def indexNumberOfStudent():
    studentsList=input("Enter the student name and surname for number : ")
    print("Number of student: "+str(students.index(studentsList)))
indexNumberOfStudent()

# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def multipleStudentsRemove():
   removeMultiple=[]
   removeMultiple=input("Multiple removed for  number of student: ")
   i=0
   while i<len(removeMultiple):
       studentsList.pop(int(removeMultiple[i]))
       i=i+1
       print(studentsList)
multipleStudentsRemove()

