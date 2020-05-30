import password_main
import email_main
import sys
import functions

def main():
    print(
        """
                                    THIS IS THE EMAIL AND PASSWORD VALIDATION  AND VERIFICATION PROGRAM
        
        This program takes in an email address and VALIDATES if it is Syntacically CORRECT, and also VERIFIES if the domain exists
        The program also takes in a password and EXAMINES if it meets the minimum requirements for a SAFE and SECURE password
        """)

    while True:
        print("Would you like to Validate your Email or Password first?\nType '[e]mail' or '[p]assword'")
        print("Type 'quit' or 'q' to leave the game")
        task= input("Type here:").lower()

        if task[0] == "e":
            print(email_main.email_main())
        elif task[0] == "p":
            print(password_main.password_main())
        elif task[0] == "q":
            print("\n would be expecting you again!")
            sys.exit()
        else:
            continue

        functions.play_again()





if __name__ == "__main__":
    print(main())