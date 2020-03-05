def test_kwargs(arg, **kwargs):
    print(arg)
    print(kwargs)
test_kwargs(2, a=1, b=3, c=4) 

def hiName(name='everybody'):
    print('Hello, '+name+'!!')

class BusinessCard:
    
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def bCard(self):
        print('-'*20)
        print('Name : ', self.name)
        print('Email : ', self.email)
        print('Address : ', self.address)
        print('-'*20) 
class fourCal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def suma(self):
        return self.a+self.b
    def mina(self):
        return self.a-self.b
    def mula(self):
        return self.a*self.b
    def diva(self):
        return self.a/self.b
class celToFa:
    def __init__(self, a):
        self.a = a

    def chan(self):
        return (self.a*1.8) +32
def chan():
    a = float(input('섭씨온도 입력'))
    return (a*1.8) +32
def howOld():
    age = 2020 - int(input().split('-')[0]) +1
    return age
def gugudan():
    
    dan = int(input('단 입력'))
    for j in range(2,10):
        print('{}x{}={:>2}'.format(dan,j,dan*j),end=' ')
    print()    
def avgScore(**a):    
    b = a.values()
    
    return sum(b)/len(b)
class MyClass:
    var = '안녕하세요' #클래스 변수 - 모든 객체에서 접근
    ok = '땡큐!'
    def sayHello(self,x):
        self.ok = x
        print(self.var) #인스턴스 변수 - 특정객체에서만 공유
        print(self.ok)
class asdf:
    def sayHi(self):
        print('안녕하세요')
    def sayBye(self, name):
        print('{}다음에 보자'.format(name))