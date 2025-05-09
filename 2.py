
import re

def is_valid_email(email):
    # Basic email pattern: username@domain.extension
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Example usage
print(is_valid_email("user@domain.com"))  # Output: True
print(is_valid_email("user@domain"))      # Output: False
print(is_valid_email("user123@abc.org"))  # Output: True
