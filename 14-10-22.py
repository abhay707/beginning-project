str = '''hello this
  is multiline string'''
print(str)
name = ["rahul",122072440,"k22PF"]
name2 = ["anuj",122062290,"k22PJ"]
print(name+name2)
print(name*5)
print("Name of the student:",name[0])
print("roll number of the student:",name[1])
print("section of the student:",name[2])
print("Name of the student:",name[-3])
print("roll number of the student:",name[-2])
print("section of the student:",name[-1])
ls = [1,32,42,41,42,22,45,11,41,51,13]
print(len(ls))
print(ls[3:-4])#negative start from the end
print(ls[3:])#from third take the whole list
print(ls[:4])#from begining to 4th variable
print(ls[:2])
print(ls[2:])
print(ls[-1:])
print(ls[2:])
print(ls[-1:])
print(ls[-2:])
print(ls[2:-1])
l = [23,5.65,["A","India"]]#it is called nesting of list
print(l[1],l[2][1])#to print item in nested list
emp1 = ["rahul",[14470,"21l/m","delhi","35 block"],9389248322]#nesting is used to represent details like that
print("Name of the person:",emp1[0])
print("address of the person:",emp1[1])
print("pin code of person:",emp1[1][0])
student = ["Rahul",1222,"k22pf"]
student[0]="harsh"
print(student)
student.append("Pf5544677")#it is used to add items in the list
print(student)
myset= set()
print(myset)
print(type(myset))
myset.add(123)#used to add element in set
myset.add("hello")
print(myset)
myset1={1,2,3,42,24.4,"Hello",11/2}
print(myset1)
mytuple=(1,2,3,"hello")
print(mytuple)
print(type(mytuple))





















