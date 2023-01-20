# num = 5

print(num.__add__(6))

class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __add__(self,x):
        temp=distance()
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)

d1=distance(3,10)
d2=distance(4,4)
print("d1= {} d2={}".format(d1, d2))

d3=d1+d2
print(d3)