import random




import random

def main():
    
    words = [
        'computer' ,
        'python' , 
        'java' , 
        'javascript' ,
        "Glimpse",
        "Horizon",
        "Quiver",
        "Nebula",
        "Lantern",
        "Brisk",
        "Melody",
        "Zephyr",
        "Fragment",
        "Cascade",
        "Whistle",
        "Meadow",
        "Echo",
        "Ember",
        "Ripple",
        "Velvet",
        "Serene",
        "Dusk",
        "Mingle",
        "Lush"
    ]

    word = random.choice(words).lower()
    print(word)  # For debugging purposes

    print("[+] Guess the word...")

    guessed_positions = ['_' for _ in word]  # List to keep track of guessed characters
    chances = len(word) + 2
    flag = False

    while chances != 0 and not flag:
        print("[+] Enter a character...")
        guess = input(">> ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("[-] Please enter only one alphabetic character.")
            continue

        if guess in word:
            for index, char in enumerate(word):
                if char == guess:
                    guessed_positions[index] = guess  
        else:
            chances -= 1  

        print(" ".join(guessed_positions))  

        if '_' not in guessed_positions: 
            flag = True
            print("[+] Congrats, You won the game")
            break

        if chances != 0:
            print(f"[+] You have {chances} chances left")
        else:
            print("[-] You lost the game. The word was:", word)

if __name__ == "__main__":
    main()

