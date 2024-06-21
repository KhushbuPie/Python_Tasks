from collections import UserList

class mylist(UserList):
    def remove(self,s=None):
        raise RuntimeError("Deleteion not allowed")

    def pop(self, s=None):
        raise RuntimeError("Deleteion not allowed")

l=mylist([1,2,3])

print("Original List",l)
l.append(5)
print("after append",l)
# l.remove()

# error:
# raise RuntimeError("Deleteion not allowed")
# RuntimeError: Deleteion not allowed