from collections import namedtuple

''' tuple object with names for each position which the ordinary tuples lack'''

Student= namedtuple('student',['name','age','DOB'])
s= Student("kd","22","02/02/2003")
print("the name using index:",s[0])
print("the name using keyname:",s.name)

li = ['Manjeet', '19', '411997' ] 

# di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
print("make nametupple from list:")
print(Student._make(li))

print("namedtupple to dict")
print(s._asdict())