def main():
    #escribe tu código abajo de esta línea
    import math
    num_palabras = int(input("Dame el número de palabras: "))
    
    páginas = math.ceil(num_palabras/475)
    costo = páginas*60 - .1(páginas*60)
    
    print("El costo de la publicación es:", costo)



if __name__ == '__main__':
    main()
