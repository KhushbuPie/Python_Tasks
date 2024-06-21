from collections import UserDict

class mydict(UserDict):
    def _del_(self):
        raise RuntimeError("Deleteion not allowed")

    def pop(self,s=None):
        raise RuntimeError("Deleteion not allowed")

    def popitem(self,s=None):
        raise RuntimeError("Deleteion not allowed")

d = mydict({'a':1,'b':2,'c':3})
# d.pop()

# if uncomment d.pop()
# error:raise RuntimeError("Deleteion not allowed")
# RuntimeError: Deleteion not allowed