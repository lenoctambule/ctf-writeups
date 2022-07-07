def tour1(password):
    string = str("".join(password[::-1]))
    return [ord(c) for c in string]


def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
        #print(new)
    return new

def tour3(password):
    mdp = ['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
         mdp[i] = chr(password[len(password) - i -1 ] + i % 4)
         mdp[len(password) - i -1 ] = chr(password[i] + i % 4)
         #print(mdp)
    return "".join(mdp)

"""
test1 = "abcdefgh"
print(tour1(test1))
print(int('qkdj', base=27) - int('QKDJ', base=31) + 267500)
print(tour2(tour1(test1)))


mdp = input("Mot de passe : ")

if tour3(tour2(tour1(mdp))) == "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5":
    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
else :
    print("Désolé, le mot-de-passe n'est pas correct")

"""

mdp_rev = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"

def tour3_rev(passwd):
    res = ['a']*34
    pwd = [ c for c in passwd ]
    for i in range(len(pwd)):
        res[i] = chr(ord(pwd[len(pwd) - i - 1]) - i % 4 )
        res[len(pwd) - i - 1] = chr(ord(pwd[i]) - i % 4 )
        print([ ord(c) for c in res])
    return res

def tour2_rev(passwd):
    res = []
    for i in range(0,len(passwd),2):
        res.append(passwd[i])
        print(res)
    return res
    
def tour1_rev(passwd):
    passwd_chr = [ c for c in passwd ]
    res = str("".join(passwd_chr[::-1]))
    print(res)
    return res

print([ ord(c) for c in mdp_rev])
print(tour1_rev(tour2_rev(tour3_rev(mdp_rev))))


