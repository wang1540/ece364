#! /usr/bin/env python2.6
#
#$Author: ee364f06 $
#$Date: 2014-03-06 11:29:00 -0500 (Thu, 06 Mar 2014) $
#$Revision: 66235 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S14/students/ee364f06/Lab07/Vectors.py $

class Vector:
    def __init__(self,elements):
        if len(elements == 0):
            raise ValueError("No elements\n")
        else:
            self.elements = float(elements)
        pass

    def add(self,other):
        elements=[]
        if (len(self.elments) == len(other.elements)):
            for i in range(len(self.elements)): 
                #self.elements[i] + other.elements[i]
                elements.append(self.elements[i] + other.elements[i])

        else:
            raise ValueError('The lengths are different for add\n')
                

        return Vector(elements)
        pass

    def sub(self,other):
        elements=[]
        if(len(self.elements) == len(other.elements)):

            for i in range(len(self.elements)):
                temp = self.elements[i] - other.elements[i]
                elements.append(temp)
            
        else:
            raise ValueError("The lengths are different for sub\n")
                                                                                                     
        return Vector(elements)
        pass
    
    def dot(self,other):
        if(len(self.elements) == len(other.elements)):
            for i in range(len(self.elements)):
                sum = self.elements[i] * other.elements[i] + sum
        else:
            raise ValueError("The lengths are different for dot\n")

        return sum
        pass

    def scale(self,by):
        elements=[]
        for i in range(len(self.elements)):
            temp = self.elements[i] * by
            elements.append(temp)
        return Vector(elements)
        pass

    def extend(self,other):
        elements=[]
        for i in range(len(self.elements)):
            elements.append(self.elements[i])

        for j in range(len(other.elements)):
            elements.append(other.elements[j])

        return Vector(elements)
        pass

    def length(self):
        return len(self.elements)
        pass

    def distance(self, other):
        if (len(self.elements) == len(other.elements)):
            for i in range(len(self.elements)):
                sum = math.pow((self.elements[i]-other.elements[i]), 2) + temp

            temp = math.sqrt(sum)

        else:
            raise ValueError("The lengths are different\n")

        return temp
        pass

    def at(self,i):
        return (self.elements[i])
        pass

    def __str__(self):
        leng = len(self.elements)
        T = tuple(self.elements) 
        return "Vector[%d]: %s\n" % (leng ,T)
        pass


class Vectors3D(Vector):
    def __init__(self,elements):
        if (len(elements) == 3):
            Vector.__init__(self,elements)
        #if len(elements == 0):
        #    raise ValueError("No elements\n")
        else:
            raise ValueError("Not exact three elements\n")
        #    self.elements = float(elements)
        #pass

        #self.elements = elements

    def add(self,other):
        elements = Vector.add(self,other)
        #elements=[]
        #if (len(self.elments) == len(other.elements)):
        #for i in range(len(self.elements)):
                                                            #self.elements[i] + other.elements[i]
        #    elements.append(self.elements[i] + other.elements[i])
        #else:
        #    raise ValueError('The lengths are different for add\n')


        return Vector3D(elements)
        pass

    def sub(self,other):
        elements = Vector.sub(self,other)

        return Vector3D(elements)

    def dot(self,other):
        elements = Vector.dot(self,other)
        return elements

    def length(self):
        return 3

    def scale(self,by):
        elements = Vector.scale(self,by)
        return Vector3D(elements)

    def extend(self,other):
        raise NotImplementedError("Can't implement")
        pass

    def distance(self,other):
        return(Vector.distance(self,other))
        #return 

    def at(self,i):
        return(Vector.at(self,i))

    def __str__(self):
        T = tuple(self.elements)
        return "Vector3D: %s\n" % T        
        



if __name__ == "main":
    vec_a = Vector([2,6,1,-9.1])
    vec_b = Vector([3,2.7,0,18])

    vec_result = vec_a.add(vec_b)
    print ("vec_result = %s" % vec_result)
    vec_a = Vector3D([7.2,4.13,5])
    scalar = 3.1415

    vec_result = vec_a.scale(scale)
    print ("vec_result = %s" % vec_result)

