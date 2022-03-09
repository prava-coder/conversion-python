#write a python program which accepts the numbers which are separated by commas and generate a list and tuple
#with those numbers

enter_num=input("enter a number which are separated by commas:")
list=enter_num.split(",")
print("list is:",list)
tuple=tuple(list)
print("tuple is:",tuple)

# expected output
#enter a number which are separated by commas:1,2,3,4
#['1','2','3','4']=list
#('1','2','3','4')=tuple