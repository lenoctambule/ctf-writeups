#!/usr/bin/python3.10

#---------Fonctions de bases---------
import random as rd

s = [16, 3, 12, 9, 1, 60, 1, 3, 14, 39, 13, 16, 16, 1, 9, 13, 3, 39, 60,
    16, 16, 1, 60, 7, 39, 13, 3, 13, 18, 3, 13, 25, 14, 3, 1, 14, 60,
    13, 32, 13, 3, 39, 16, 18, 18, 3, 43, 16, 18, 3, 1, 43, 18, 16,
    13, 16, 1, 3, 1, 16, 13, 18, 60, 16, 3, 3, 14, 18, 13, 14, 16, 18,
    7, 3, 7, 25, 7, 7, 13, 13, 13, 3, 60, 1, 3, 13, 1, 25, 18, 16, 32,
    16, 60, 1, 7, 44, 18, 39, 39, 39, 60, 3, 1, 60, 3, 16, 13, 13, 14,
    1, 3, 39, 39, 31, 32, 39, 32, 18, 39, 3, 13, 32, 60, 7, 7, 39, 14,
    3, 18, 14, 60, 39, 18, 7, 1, 32, 13, 3, 14, 39, 39, 7, 1, 1, 13,
    29, 60, 13, 39, 14, 14, 16, 60, 1, 3, 44, 14, 3, 1, 1, 1, 39, 13,
    14, 39, 18, 3, 7, 13, 39, 32, 1, 43, 1, 16, 1, 3, 18, 14, 25, 32,
    7, 13, 39, 7, 1, 3, 60, 13, 13, 7, 18, 1, 3, 18, 1, 60, 7, 1, 39,
    14, 3, 39, 7, 31, 1, 7, 18, 7, 32, 3, 3, 14, 32, 14, 1, 32, 12,
    18, 31, 39, 1, 13, 13, 43, 44, 32, 3, 32, 60, 14, 60, 60, 7, 3, 1,
    3, 3, 14, 1, 60, 16, 44, 3, 1, 32, 13, 5, 16, 39, 3, 60, 7, 14, 3,
    13, 7, 31, 13, 39, 9, 3, 44, 13, 16, 14, 18, 18, 3, 7, 3, 3, 3, 7,
    3, 3, 16, 39, 3, 3, 13, 32, 13, 3, 18, 7, 10, 3, 18, 1, 7, 7, 18,
    13, 43, 18, 3, 32, 39, 32, 13, 1, 18, 10, 1, 32, 1, 16, 32, 3, 44,
    3, 18, 1, 1, 1, 16, 18, 25, 60, 1, 39, 1, 18, 60, 16, 1, 7, 3, 13,
    16, 18, 39, 14, 7, 14, 3, 14, 13, 7, 16, 10, 18, 13, 3, 16, 13, 3,
    32, 43, 13, 14, 1, 13, 1, 14, 18, 60, 7, 3, 7, 31, 1, 18, 26, 7,
    3, 3, 32, 1, 7, 18, 7, 1, 16, 18, 39, 14, 7, 3
]

##
def a(c, r=True):
    n = ord(c)
    if r: rd.seed(n)
    match n:
        case 0:
            return dict.fromkeys(range(10), 0)
        case _:
            return ( d := a(chr(n - 1), False) ) | {( m := rd.randint(0, 9)) : d[m] + rd.randint(0,2)}

##

def b(p, n):
    print(p)
    match list(p):
        case []:
            return []
        case [f, *rest]:
            l = list(a(f).values()) + b(''.join(rest), n*2)
            rd.seed(n)
            rd.shuffle(l)
            print(l)
            print(n)
            return l

# f = first
# *rest = reste

##
def c(p, n=0):
    match p:
        case []:
            return n!=0
        case [f, *rest]:
            rd.seed(s[n])
            return rd.randint(0,30) == f and c(rest, n + 1)
##

#---------Fonctions iteratives---------

def a_it(c) :
    n = ord(c)
    rd.seed(n)
    d = dict.fromkeys(range(10),0)
    for i in range (n, 0, -1):
        m = rd.randint(0,9)
        #print(m)
        d[m] = d[m] + rd.randint(0,2)
        #print(d)
    return d
    
def b_it(p):
    res = []
    for i in range(len(p)-1, -1 , -1) :
        res = ( list(a(p[i]).values()) ) + res
        pwr = pow(2, i)
        rd.seed(pwr)
        rd.shuffle(res)
        print(res)
        print(pwr)
    return res
    
def c_it(p):
    for i in range(len(p)) :
        rd.seed(s[i])
        if p[i] == rd.randint(0,30) :
            return false
    return true
    

"""
print(a("4"))
print(a_it("4"))

print("Recursive : ")
print(b("404CTF",1))
print("Iterative :")
print(b_it("404CTF"))
"""

#---------Fonctions inverses---------

def c_rev() :
    res = []
    for i in range(len(s)) :
        rd.seed(s[i])
        res.append(rd.randint(0,30))
    return res
    
def shuffle_back(l,order):
    l_out = [0] * len(l)
    for i, j in enumerate(order):
        l_out[j] = l[i]
    return l_out
    
def b_rev(p) :
    passwd = []
    res = p
    n_iteration = int(len(res)/10)
    for i in range(n_iteration):
        #print("--------")
        #print(res)
        rd.seed(pow(2,i))
        order = [i for i in range(len(res))]
        rd.shuffle(order)
        res = shuffle_back(res, order)
        passwd.append(a_rev(res[:10]))
        print(res[:10])
        del res[:10]
    return [chr(i) for i in passwd]
    
        
def a_rev(p):
    
    c = 0
    for i in range(128) :
        #print(type(p))
        test = list(a_it(chr(i)).values())
        #print(type(test))
        if test == p :
            c = i
            break
    return c



#print(b_rev(b_it("404")))

print("Password : ", ''.join(b_rev(c_rev())))

"""
    
l_test = [45,53,3,8,5,98]
rd.seed(1) 
rd.shuffle(l_test)
rd.seed(1)

print(l_test)
order = [i for i in range(len(l_test))]
rd.shuffle(order)
print(shuffle_back(l_test, order))
        
#print(c(b("404CTF",1)))
#print(a("b"))
"""
"""
if c(b(input("password:"), 1)):
    print("Utilise ce mot de passe pour valider le challenge!")
else:
    print("Essaye Encore!")
"""