შუალედური_გამოცდის_ქულა=int(input('შეიყვანე შენი შუალედური გამოცდის ქულა /20: '))
დასკვნითი_გამოცდის_ქულა=int(input('შეიყვანე შენი დასკვნითი გამოცდის ქულა /40: '))
პროექტის_ქულა=int(input('შეიყვანე შენი პროექტის ქულა /40: '))
if შუალედური_გამოცდის_ქულა + დასკვნითი_გამოცდის_ქულა + პროექტის_ქულა >= 70:
    print('გილოცავ! თქვენ გადალახე კურსი! თქვენი ჯამური ქულების რაოდენობა=' )
    print(შუალედური_გამოცდის_ქულა + დასკვნითი_გამოცდის_ქულა + პროექტის_ქულა)
else:
    print('სამწუხაროდ თქვენ ვერ გადალახეთ კურსი! თქვენი ჯამური ქულების რაოდენობა=')
    print(შუალედური_გამოცდის_ქულა + დასკვნითი_გამოცდის_ქულა + პროექტის_ქულა)
     
