import re
import dns.resolver
import sys
import main

local_regex_that_catches_consecutive_dots = re.compile(r"([.])\1")

local_regex_without_quotes = re.compile(
    r"""^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"""
    r"""[A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]{0,62}"""
    r"""[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]*$"""
)

local_regex_with_quotes = re.compile(
    r"""^"[A-Za-z0-9!#$%&'*+/=?^_`{|}~."(),:;<>@[\\ \]-]"""
    r"""{0,62}"$|^'[A-Za-z0-9!#$%&'*+/=?^_`{|}~."()"""
    r""",:;<>@[\\ \]-]{0,62}'$"""

)
domain_regex = re.compile(r"""^[A-Za-z0-9][A-Z0-9a-z-]{0,63}$""")


def is_local_valid(local, local_length):
    local_Validity = False

    if local_length > 64:
        print("Invalid local portion: Too long(max 64 characters)")
        local_Validity = False

    if local_regex_that_catches_consecutive_dots.search(local):
        print("The local portion does not support conssecutive dots without quotes")
        local_Validity = False

    match_without_quotes = local_regex_without_quotes.fullmatch(local)
    if match_without_quotes:
        local_Validity = True

    match_with_quotes = local_regex_with_quotes.fullmatch(local)
    if match_with_quotes:
        local_Validity = True
        answer = match_with_quotes.group()
        answer = answer[1:-1]
        test_local = list(answer)

        if len(test_local) == 1 and test_local[-1] == "\\":
            print("back-slash must be preceeded by back-slash")
            local_Validity = False

        if test_local[-1] == "\\":
            if test_local[-2] != "\\":
                print("back-slash must be preceeded by back-slash")
                local_Validity = False

        if test_local[0] == "\"":
            print("double-quote should be preceeded by a back-slash")
            local_Validity = False

        for indx, char in enumerate(test_local[1:]):
            if char == "\"":
                if test_local[indx] != "\\":
                    print("double-quote should be preceeded by a back-slash")
                    local_Validity = False

    if local_Validity:
        print("The host/local portion is valid!!")
        return True

    else:
        print("The host/local portion in invalid, enure the syntax is correct.Check you guidelines above")
        return False


def is_domain_valid(local, domain, local_length, domain_length):

    if not domain:
        print("The domain is invalid")
        return False

    Domain_Validity = False
    if (domain[-1].isalpha() or domain[-1].isnumeric()) and domain_length <= 253 - local_length:
        domain = domain.split(".")
    else:
        Domain_Validity = False

    for DNS_label in domain:
        match_with_domain = domain_regex.fullmatch(DNS_label)
        if  match_with_domain:
            Domain_Validity = True
        else:
            Domain_Validity = False
            break

    if Domain_Validity:
        print("\nThe Domain portion is valid!!")
        return True

    else:
        print("\nThe Domain portion in invalid, ensure the syntax is correct. Check you guidelines above")
        return False


def dns_lookup_domain(domain):
    try:
        answers = dns.resolver.query(domain, 'MX')
    except:
        answers = None

    if answers:
        print("\ndomain DNS lookup Succeeded!")
        return True
    else:
        print("\ndomain DNS lookup failed: Domain does not exist")
        return False


def password_valid(password):
    password_validity = False
    print("\nPROCESSING...\n")
    special_characters = {'$', '\\', '+', '_', '.', "'", ')', '%', '^', '!', ']',
                          '?', ',', '*', '=', '`', '#', '-', '/', '@', '|', '~',
                          '[', '{', '"', '&', ':', '(', ';', '}'}
    # greater and less than sign excluded because it causes issues with some systems


    is_upper = 0
    is_lower = 0
    is_special = 0
    is_number = 0
    invalid_character = []

    for char in password:
        if char.isalpha():
            if char.isupper():
                is_upper += 1
            else:
                is_lower += 1
        elif char.isnumeric():
            is_number += 1
        elif char in special_characters:
            is_special += 1
        else:
            invalid_character.append(char)
            if char == " ":
                print("White Spaces are not accepted as characters\n")
                # return "\n PASSWORD IS NOT VALID!"

    if is_upper == 0:
        print("Password shoould Include at least one uppercase letter")
        password_validity = False
    if is_lower == 0:
        print("Password shoould Include at least one lowercase letter")
        password_validity = False
    if is_special == 0:
        print("""Password shoould Include at least one special character E.g. !"#$%&'()*+,-./:;=?@[\]^_`{|}~ """)
        password_validity = False
    if is_number == 0:
        print("Password should Include at least one number")
        password_validity = False


    if is_upper + is_lower + is_special + is_number == len(password):
        password_validity = True
    else:
        password_validity = False
        print("The following characters are invalid and should not be included:")
        for char in invalid_character:
            print(f"{char}")
    return password_validity


def play_again():
    print("\nDo you want to VALIDATE/VERIFY again? \nYes or No")
    ans = input("Type here: ").lower()
    if ans[0] == "y":
        print(main.main())
    elif ans[0] == "n":
        print("\n would be expecting you again!")
        sys.exit()
    elif ans == None:
        play_again()
    else:
        play_again()