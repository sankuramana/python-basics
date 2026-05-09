names_list=["sanku","ramana","babau","rupesh","sandeep"] #0,1,2 #index
print(names_list[0])
print(names_list[:])
print(names_list[0:1])
print( "last element in the names list is:",names_list[-1])
print("first element of the list is:",names_list[0])
print("leangth of the list is", len(names_list))
names_list[2]="rolex"
print("after value is upated:",names_list[:])
print("list of operations:", dir(names_list))
"""
list of operations: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
names_list.append("bangalore")
print("appened new value:",names_list)
print("fetching index:", names_list.index("sandeep"))
name_list_1=["rakesh","ramesh"]
#prinitng  two list at a time
print(name_list_1,names_list)