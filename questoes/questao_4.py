def main():

    tuple_out =[]
    while True:
        user_data = input('Nome, idade e altura, separados por virgula: ')
        if user_data == '':
            print(sorted(list(zip(tuple_out))))
            break
        else:
            tuple_out.append(user_data)

if __name__ == '__main__':
    main()
