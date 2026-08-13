nums=[12,45,7,89,34,89,20]
largest=-1
second=-1
for i in nums:
   if i>largest:
       second=largest
       largest=i
   elif i>second and i!=largest:
        second=i
print(second)