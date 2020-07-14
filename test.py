hash = []
for i in range(256) :
    k = i
    for _  in range(8) :
        if k % 2 != 0 :
            k = k ^ 0xdeadc0de
        k = k // 2
    hash.append(k)


def calc_hash(s):
    H = 0xffffffff
    for car in s :
        C = ord(car)
        H = (H >> 8) ^ hash[ (H & 0xff) ^ C]
    H = H ^ 0xffffffff
    return hex(H)
    
minuscules = [chr(i) for i in range(97,123)]
chiffres = [chr(i) for i in range(48,58)]
            
def brute():
    for a1 in chiffres :
        print(a1)
        for a2 in minuscules :
            for a3 in minuscules :
                for a4 in minuscules :
                    for a5 in minuscules :
                        for a6 in minuscules :
                            pwd = a1+a2+a3+a4+a5+a6
                            if calc_hash(pwd) == '0xbed3414a' :
                                print(pwd)
                                return None
    print("pas trouvé")
brute()
