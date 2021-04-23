import pathlib

var_list1=["py","TXT"]
var_list2=["python", "text"]

filename = input("Input the Filename: ")
f_extns = filename.split(".")
x = var_list1.index(f_extns[-1])
print(var_list2[x])






