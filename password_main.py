import functions

def password_main():
    print(
        """
    FOR A VALID and SAFE password, Your password should follow the following steps:
    
    At least 8 characters—the more characters, the better
    A mixture of both uppercase and lowercase letters
    A mixture of letters and numbers
    Inclusion of at least one special character E.g. !"#$%&'()*+,-./:;=?@[\]^_`{|}~
    """
    )

    password = input("Type your password here: ")

    if len(password) < 8:
        return "Too Short! Password must be at least 8 characters"


    a = functions.password_valid(password)

    if a:
        return "This password is VALID, SAFE and SECURE to use anywhere :)"
    else:
        return "This password is NOT STRONG and SECURE"


if __name__ == "__main__":
    print(password_main())
