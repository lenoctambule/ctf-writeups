# ------- Réécrit à partir de l'asm--------

key = "d1j#H(&Ja1_2 61fG&"

def code(l):
	match list(l) :
		case []:
			return[]
		case [el, *rest]:
			return [( 5 * el) ^ ord(key[len(rest) % len(key)])] + code(rest)
    
#-------- Réécrit en itératif-------

def code_ite(l):
	res = []
	for i in range(len(l)) :
		res = res + [ (5 * l[i]) ^ ord(key[(len(l) - i - 1 ) % len(key)])]
	return res

#-------Fonction inverse--------
def code_rev(to_rev):
	res = []
	for i in range(len(to_rev)) :
		a = to_rev[i] ^ ord(key[(len(to_rev) - i - 1) % len(key)])
		res = res + [int(a/5)]
	return res
        
to_rev = [292,194,347,382,453,276,577,434,183,295,318,196,482,325,412,502,396,402,328,194,473,490,299,503,386,215,263,211,318,206,533]
#user_input = [ord(i) for i in "404CTF{" ]
user_input = to_rev
reversed = code_rev(user_input)
print(''.join([chr(i) for i in reversed]))
    

