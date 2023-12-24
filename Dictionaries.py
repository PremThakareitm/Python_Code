d={1:'Prem',"roll":36,"stu":[36,"prem.thakare",15011]}
print(d)

print(d["stu"])

#add/modify
print("#add/modify")
d["stu"].append("ITM")

print(d["stu"])
print(d)

#remove 
d["stu"].remove("ITM")

#delete
print("#delete")
del(d['roll'])
print(d)

#dictonaries i dictonaries
p={}
d={'p':{1:'prem',"roll":36,"stu":[36,"prem.thakare",]}}
print()
