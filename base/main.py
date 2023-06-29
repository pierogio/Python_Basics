def sum(a, b):
    return a + b

def mult(a, b):
    return a * b

def range_numeros(n):
    numeros = []
    for i in range(n):
        numeros.append(i)
    return numeros

if __name__ == '__main__':
    print(sum(2, 3))
    print(mult(4, 5))
    print(range_numeros(15))


