import random
import textwrap

def welcome():
    print("""
    .__                               
    __  _  __ ____ |  |   ____  ____   _____   ____  
    \ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
     \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
      \/\_/  \___  >____/\___  >____/|__|_|  /\___  >
                 \/          \/            \/     \/ """)
    print("               HANG MAN GAME!")

def main():
    attempts = 6
    global length
    global display

    # List of words for the game
    words = [
        'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm',
        'compiler', 'database', 'encryption', 'firewall', 'hardware',
        'internet', 'java', 'kernel', 'malware', 'network', 'object',
        'protocol', 'query', 'router', 'security', 'token', 'url',
        'virtual', 'wireless', 'xml', 'zip', 'abstract', 'binary',
        'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal',
        'iteration', 'juxtapose', 'keystroke', 'lambda', 'metadata', 'node']

    # Randomly choose a word from the list
    chosen_word = random.choice(words)
    length = len(chosen_word)
    print(chosen_word)  # For testing, remove this line later

    # Initialize the display with underscores
    display = ['_' for _ in range(length)]

    # Stages of the hangman
    stages = [
        textwrap.dedent("""\
            +---+                  
                |                  
                |                  
                |                  
               ===                 
            """),
        textwrap.dedent("""\
            +---+                  
            0    |                 
                 |                 
                 |                 
                ===                
            """),
        textwrap.dedent("""\
            +---+                  
            0    |                 
            |    |                 
                 |                 
                ===                
            """),
        textwrap.dedent("""\
                 +---+             
                 0    |            
                /|    |            
                      |            
                     ===           
            """),
        textwrap.dedent("""\
                  +---+            
                  0    |           
                 /|\   |           
                       |           
                      ===          
            """),
        textwrap.dedent("""\
                     +---+         
                     0    |        
                    /|\   |        
                    /     |        
                         ===       
            """),
        textwrap.dedent("""\
                        +---+      
                        0    |     
                       /|\   |     
                       / \   |     
                            ===    
            """)
    ]

    # Main game loop
    stage_num = 0
    game_over = False
    while not game_over:
        print(' '.join(display))  # Print the current state of the word
        guess_letter = input("\nENTER A LETTER: ").lower()  # Ask for user input

        # Check if the guessed letter is in the chosen word
        if guess_letter in chosen_word:
            print("Match!")
            # Update the display to reveal the guessed letter(s)
            for position in range(length):
                if chosen_word[position] == guess_letter:
                    display[position] = guess_letter
        else:
            # Decrease attempts and display the current stage of hangman
            attempts -= 1
            print(f"Attempts left: {attempts}")
            if attempts == 0:
                game_over = True
                print('YOU LOSE!')
            else:
                print(stages[stage_num])
                stage_num += 1

        # Check if all letters have been guessed
        if '_' not in display:
            game_over = True
            print("CONGRATULATIONS! YOU WIN!")

# Start the game
welcome()
main()
