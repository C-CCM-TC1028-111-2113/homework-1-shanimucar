def main():
    #escribe tu código abajo de esta línea
    import math
    
    minutos = float(input("Dame los minutos: "))
    
    cm = minutos * (5.7*0.1*60)
    redondeado = round(cm,1)
    
    print("Centímetros recorridos:", redondeado)
    

if __name__ == '__main__':
    main()
