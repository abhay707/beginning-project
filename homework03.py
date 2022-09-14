#Nested list of a university
l = ["Lovely Professional University",["Agriculture","Bioengineering","Business","Civil Engineering"],["Computer Science and Engineering","Mechanical Engineering","Aerospace Engineering"]]
print("Name of the university:",l[0])
print("School in college:",l[1])
print("Department in college:",l[2])
#Nested list of a political party
l1 = ["BJP",["Narendra Modi","Syama Prasad Mukherjee","Atal Bihari Vajpayee","Amit Shah","L. K. Advani","Rajnath Singh","Ram Nath Kovind","Nitin Gadkari"]]
print("Name:",l1[0])
print("Member name:",l1[1])
print("Prime minister of india:",l1[1][0])
print("President of india:",l1[1][-2])
print("Founding member:",l1[1][2])
#Nested list of a student in school
l2 = ["Anuj",[471001,"delhi","block 68","near mobile tower"],"K22PF",12206689,]
print("Name:",l2[0])
print("Address:",l2[1])
print("Pin code:",l2[1][0])
print("Roll number:",l2[-1])
print("Section:",l2[-2])