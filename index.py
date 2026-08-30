import threading

resultado1 = 0
resultado2 = 0
def parte1(x):
    global resultado1
    resultado1 = (x ** 2 + 3) * 7
    # return resultado1

def parte2():
    global resultado2
    resultado2 = 36 / 4
    # return resultado2

x = 5

t1 = threading.Thread(target=parte1, args = (x,))
t2 = threading.Thread(target=parte2)

t1.start()
t2.start()

t1.join()
t2.join()

final = resultado1 - resultado2
print(f"Resultado Final para x = {x} : {final}")