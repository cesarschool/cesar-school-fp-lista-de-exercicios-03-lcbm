
def main():

    rot_in = input("Digite aqui a cifra rotacional ROT + <chave> + ' ' + mensagem: ").split(' ', 1)

    for item in rot_in:
        if not "ROT" in item:
            print("erro")
            return
        else:
            rot_message = rot_in[1]
            rot_key = int(rot_in[0].split('ROT')[1])
            alphabet_latin = 'abcdefghijklmnopqrstuvwxyz'
                
            def caesar_cypher(rot_message, rot_key):
                alphabet_caesar = alphabet_latin[rot_key:] + alphabet_latin[:rot_key]
                trans_ref = str.maketrans(alphabet_latin, alphabet_caesar)
                print(rot_message.translate(trans_ref))
            caesar_cypher(rot_message, rot_key)

if __name__ == '__main__':
    main()
