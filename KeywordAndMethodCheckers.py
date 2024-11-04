import keyword
import inspect

x = ['not', 'False', 'True', 'None', 'blane']


for i in x:
    print(True if (keyword.iskeyword(i)) else False)


class findMethod:
    def normalMethod(a, b, c):
        return None

obj = findMethod()

print(inspect.ismethod(obj.normalMethod))
print(inspect.signature(obj.normalMethod))