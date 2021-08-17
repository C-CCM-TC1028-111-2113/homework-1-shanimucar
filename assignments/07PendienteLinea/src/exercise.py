def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
    import math
    
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    
    a = (x1, y1)
    b = (x2, y2)
    
    pendiente = math.dist(a,b)
    
    print("Pendiente:", pendiente)


if __name__ == '__main__':
    main()
