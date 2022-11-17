import random
from logger import LogLevel, log_message  
while True:
    print('')
    try:   
        log_message(LogLevel.INFO,"Включение программы")
        N=int(input('До какого числа можно загадать цифру? (Введите и нажмите ENTER) ')) 
        log_message(LogLevel.INFO,f'Пользователь ввел максимальное число {N}')
        k=int(input('Количество попыток (Введите и нажмите ENTER) '))
        log_message(LogLevel.INFO,f'Пользователь ввел количество попыток {k}')
        randomik=random.randint(1,N)
        m=1
        while m<=k: #отсчет количества попыток    
            chislo=int(input('Ваше число (Введите и нажмите ENTER) ')) #загадываем число
            log_message(LogLevel.INFO,f'Пользователь ввел число {chislo}')
            print('попытка', m, 'из', k)

            if chislo>randomik:
                print('Загаданное число меньше введенного')
                log_message(LogLevel.INFO,'Загаданное число меньше введенного')

                if m==k:
                    print('Попытки закончились')
                    log_message(LogLevel.INFO,'Попытки закончились')
                    print('Загаданное число компьютера: ',randomik) #показываем, какую цифру загадала программа
                    log_message(LogLevel.INFO,f'Загаданное число компьютера: {randomik}')

            if chislo<randomik:
                print('Загаданное число больше введенного')
                log_message(LogLevel.INFO,'Загаданное число больше введенного')

                if m==k:
                    print('Попытки закончились')
                    log_message(LogLevel.INFO,'Попытки закончились')
                    print('Загаданное число компьютера: ',randomik)
                    log_message(LogLevel.INFO,f'Загаданное число компьютера: {randomik}')

            if chislo==randomik:
                print('Вы угадали число!')
                log_message(LogLevel.INFO,'Пользователь угадал число')
                break
            m=m+1

    except ValueError:
        print("Нужно ввести целое положительное число")
        log_message(LogLevel.ERROR,"Неправильное число")
        continue
if __name__ == "__main__":
    main()
