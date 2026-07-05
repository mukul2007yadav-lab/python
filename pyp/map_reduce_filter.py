l=[34,4,56,7,8]
# squrdlist=[]
# for item in l:
#     squrdlist.append(item*item)
square=lambda x:x*x
squrdlist=map(square,l)
print(list(squrdlist))