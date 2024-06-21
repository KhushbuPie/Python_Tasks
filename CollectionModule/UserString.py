from collections import UserString

class mystring(UserString):
    def append(self,s):
        self.data +=s

    def remove(self, s):
        self.data=self.data.replace(s,"")

s1 = mystring("String")
print("original string:",s1.data)
s1.append("s")
print("after appending s:",s1.data)
s1.remove("n")
print("after remove n:",s1.data)