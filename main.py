import codeChallenge
if __name__ == '__main__':
    # usando https://codebeautify.org/md5-hash-generator coloque mi nombre completo
    # Juan Diego Becerra Peña y el hash resultante es el que vemos a continuacion
    hash = "f40c6ea22d3ea3e398f1098b5bc03871"
    s = ""
    testList = input("ingrese los numeros separados por , : ").split(",")
    for i in range(len(hash)):
        try:
            if int(hash[i]):
                s = int(hash[i])
                print("S = ", s)
                break
        except ValueError:
            print("no puedo convertirlo a entero")
    if s == "":
        print("reapply the hash")
    else:
        print("Respuesta Challenge 1: ", codeChallenge.challengeOne(s, testList))
        print("Respuesta Challenge 2: ", codeChallenge.challengeTwo(s, testList))
    testList = input("ingrese los numeros separados por , para el 3er challenge: ").split(",")
    testList = list(map(int, testList))
    print("Respuesta Challenge 3: ", codeChallenge.challengeThree(testList))

