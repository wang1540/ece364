
#string
var="h e aef ewaf e e"
var=var.split(" ",4)
print var
print len(var)
print var[0]
new=",".join(var)
print new

#list
a=[1,2,3,"afe",[1,4]]
a[2]=10
print a[2:3]

#type conversion
b=8
c=complex(4,8)

print ("{%d} {%complex}".format(b,c))
