def main():

    up, down, left, right = (int (x) for x in (0,0,0,0))
    
    while True:
        movimento = input('Digite os movimentos cima, baixo, esquerda, direta (do robo), separdos por virgula').split(',')
        if movimento == '':
            break
        else:
            continue
        def calc_dis(movimento):
            distancia =
            rounded = ((down - up)**2 + (left - right)**2 )**(1/2)
            print(round(rounded))

if __name__ == '__main__':
    main()
