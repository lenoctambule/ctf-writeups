def tour1(password):
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    return [ord(c) for c in string]


def tour2(password):
    print(password)
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
        print(new)
    return new

def tour3(password):
    mdp =['a']*34
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i - 1 ] + i % 4),  chr(password[i] + i % 4)
        print([ ord(c) for c in mdp ] )
    return "".join(mdp)

mdp = tour3(tour2(tour1("abcdefghijklmnopq")))

print(mdp)

"""
mdp = input("Mot de passe : ")

if tour3(tour2(tour1(mdp))) == "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5":
    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
else :
    print("Désolé, le mot-de-passe n'est pas correct")
"""



