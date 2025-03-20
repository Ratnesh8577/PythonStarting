'''def add(*args):
    print(args)# tuple aayega sabh
add(1,2,3)
add(200,3958,6,4,74,5)
add(23,45)

'''
'''
def add(*args):
    print(sum(args))# sukar sakte hai
add(1,2,3)
add(200,3958,6,4,74,5)
add(23,45)'''

"""
def add(*args,**kwargs): # Dictionary 
    print(kwargs)# sukar sakte hai
    for k,v in kwargs.items():
        print(k,v)

add(name="amit",age="23",gender="Male")"""



def add(n1,n2,n3,*args,**kwargs): # Dictionary 
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")
    #print(kwargs)# sukar sakte hai
    for k,v in kwargs.items():
        print(k,v)

add(5,10,15)


def add(n1,n2,n3,*args,**kwargs): # Dictionary 
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")
    #print(kwargs)# sukar sakte hai
    for k,v in kwargs.items():
        print(k,v)

add(5,10,15,100,200,300,name="Ratnesh")
