# Email-and-Password-Validation Program
 This program takes in an email address and VALIDATES if it is Syntactically CORRECT, and also VERIFIES if the domain exists
 The program also takes in a password and EXAMINES if it meets the minimum requirements for a SAFE and SECURE password

## EMAIL ADDRESS ##
### Local Portion:
The local-part of the email address may be unquoted or may be enclosed in quotation marks.
The maximum total length of the local-part of an email address is 64 octets.
 If unquoted, it may use any of these ASCII characters:
•	uppercase and lowercase Latin letters A to Z and a to z;
•	digits 0 to 9;
•	printable characters !#$%&'*+-/=?^_`{|}~;
•	dot(.), provided that it is not the first or last character and provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed)
        
If in a quoted string:
=>space and special characters "(),:;<>@[\] are allowed with restrictions (they are only allowed inside a quoted string as described above, and in addition, a backslash or double-quote must be preceded by a backslash);

### Domain portion ###:
The domain name part of an email address has to conform to strict guidelines: it must match the requirements for a hostname, a list of dot-separated DNS labels, each label being limited to a length of 63 characters and consisting of:
uppercase and lowercase Latin letters A to Z and a to z;
digits 0 to 9, provided that top-level domain names are not all-numeric;
hyphen -, provided that it is not the first or last character.

*The details instructions above were gotten from https://en.wikipedia.org/wiki/Email_address. Visit the page for more info on the syntax
*This program does not accept comments in the local or domain section and IP address literals
 * The maximum email length is based on the RFC 5321 and the errata submitted against the RFC 3696. This errata specifies that the maximum number of characters is 254 due to the reverse and forward path specification

## PASSWORD ##
FOR A VALID and SAFE password, Your password should follow the following steps:
    
•	At least 8 characters—the more characters, the better
•	A mixture of both uppercase and lowercase letters
•	A mixture of letters and numbers
•	Inclusion of at least one special character E.g. !"#$%&'()*+,-./:;=?@[\]^_`{|}~
