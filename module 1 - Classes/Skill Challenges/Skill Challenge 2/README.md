# Password Generator
Create a password generator based on security level(low,mid and high) and password length.

### Requirements

1) Define a Password class that supports 2 arguments(strength and length);
2) The class should generate a password accordingly to the below requirements:
    - ``low``: Include only lowercase and uppercase letters - 8 chars;
    - ``mid``: Include lowercase and uppercase letters plus digits - 12 chars;
    - ``high``: Include lowercase and uppercase letters as well as digits and punctuation signs - 16 chars.
3) If the user specifies the length at the instance creation,this should override the default length for the strength.
4) If the user does not specify a length or strength use 'mid' as default.
