import random 
def main():
    lower_number = int(input("Enter lower number: "))
    upper_number = int(input("Enter upper number: "))

    guss_number = random.randint(lower_number, upper_number)

    total_chances = 10
    current_status = 0
    flag = False

    while total_chances > current_status:
        current_status += 1
        user_number = int(input("Enter number: "))

        if user_number == guss_number:
            flag = True
            break

        elif user_number > guss_number:
            print("Lower number please")
        
        elif user_number < guss_number:
            print("Higher number please")
        
    if flag == True:
        print("You won")
    else:
        print("You lost. The number was", guss_number)

main()