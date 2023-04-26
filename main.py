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
        dictTest = input("ingrese el diccionario respectivo , para el 2er challenge: ")
        dictTest = eval(dictTest)
        testList = dictTest["array"]
        print("Respuesta Challenge 2: ", codeChallenge.challengeTwo(s, testList))
        dictTest = input("ingrese diccionario respectivo , para el 3er challenge: ")
        dictTest = eval(dictTest)
        testList = dictTest["coins"]
        print("Respuesta Challenge 3: ", codeChallenge.challengeThree(testList))

