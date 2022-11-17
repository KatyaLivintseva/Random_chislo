while True:
    print('')
    try:
        
        N=int(input('До какого числа можно загадать цифру? (Введите и нажмите ENTER) ')) 
        k=int(input('Количество попыток (Введите и нажмите ENTER) '))
        randomm=random.randint(1,N)
        m=1
        while m<=k: #отсчет количества попыток    
            chislo=int(input('Ваше число (Введите и нажмите ENTER) ')) #загадываем число
            print('попытка', m, 'из', k)

            if chislo>randomm:
                print('Загаданное число меньше введенного')

                if m==k:
                    print('Попытки закончились')
                    print('Загаданное число компьютера: ',randomm) #показываем, какую цифру загадала программа

            if chislo<randomm:
                print('Загаданное число больше введенного')

                if m==k:
                    print('Попытки закончились')
                    print('Загаданное число компьютера: ',randomm)

            if chislo==randomm:
                print('Вы угадали число!')
                break
            m=m+1

    except ValueError:
        print("Нужно ввести целое положительное число")
