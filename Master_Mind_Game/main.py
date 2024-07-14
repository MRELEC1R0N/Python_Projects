import random

'5629'
'5555'
'5XXX'

num = random.randint(1000, 9999)

while True:
    try:
        n = int(input("[+]Enter the number of 4 digits: "))
        break

    except ValueError:
        print("[+]Enter the number of 4 digits only")
        continue

if n == num:
    print("[+] You became the Mastermind")

else:

    ctr = 0
    while(n != num):

        ctr += 1
        num = str(num)
        count = 0
        n = str(n)
        guess = ['X'] * 4

        for i in range(4):
            if num[i] == n[i]:
                guess[i] = num[i]
                count += 1
            
            else:
                continue
        
        if count > 0 :        
            print(f"[+] You got correct digits : {guess}\n" )

            while True:
                try:
                    n = int(input("[+]Enter the new number of 4 digits: "))
                    break
                except ValueError:
                    continue    
        
        else:
            print("[-] You got 0 guess correct \n[+] Correct Number was ", num, "\n")
            break

    if n == num:
        print("[+] You became the Mastermind in ", ctr, "guesses")        

    else:
        print("[-] You didn't become the Mastermind")