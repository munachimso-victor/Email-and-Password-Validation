import functions




def email_main():
    print(
        """
        Local Portion:
        The local-part of the email address may be unquoted or may be enclosed in quotation marks.
        The maximum total length of the local-part of an email address is 64 octets.

        If unquoted, it may use any of these ASCII characters:
        =>uppercase and lowercase Latin letters A to Z and a to z;
        =>digits 0 to 9;
        =>printable characters !#$%&'*+-/=?^_`{|}~;
        =>dot , provided that it is not the first or last character and provided also t
        hat it does not appear consecutively (e.g., John..Doe@example.com is not allowed)
        If in a quoted string:
        =>space and special characters "(),:;<>@[\] are allowed with restrictions (they are only allowed inside a quoted string,
        as described in the paragraph below, and in addition, a backslash or double-quote must be preceded by a backslash);

        Domain portion:
        The domain name part of an email address has to conform to strict guidelines: it must match the requirements for a hostname,
        a list of dot-separated DNS labels, each label being limited to a length of 63 characters and consisting of:
        =>uppercase and lowercase Latin letters A to Z and a to z;
        =>digits 0 to 9, provided that top-level domain names are not all-numeric;
        =>hyphen -, provided that it is not the first or last character.

        """
    )
    print("\nThe fromat for a valid Email Address is local@domain E.g. dave@google.com")

    local = input("Type your Email Address LOCAL Portion: ")
    domain = input("Type your Email Address DOMAIN Portion: ")
    local_length = len(local)
    domain_length = len(domain)

    if local_length + domain_length > 253:
        return "Invalid Address: Too Long"


    email_address = f"{local}@{domain}"
    a = functions.is_local_valid(local, local_length)
    b = functions.is_domain_valid(local, domain, local_length, domain_length)

    if a and b:
        if functions.dns_lookup_domain(domain):
            return f"\nThe email address {email_address} is VALID, and the domain exists!"
        else:
            return f"\nThe email address {email_address} is VALID, but the domain does not exist"

    else:
        return f"\nTHE EMAIL ADDRESS {email_address} is INVALID"


if __name__ == "__main__":
    print(email_main())
