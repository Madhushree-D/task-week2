import hashlib

# Dictionary to store users and hashed passwords
users_db = {}

def hash_password(password):
    """Returns the SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    """Registers a new user with a hashed password."""
    if username in users_db:
        return "User already exists"
    users_db[username] = hash_password(password)
    return "Created new user"

def login(username, password):
    """Checks credentials and logs the user in if valid."""
    hashed = hash_password(password)
    if users_db.get(username) == hashed:
        return "Login Successful"
    return "Login Failed"

# Example usage
print(register("john", "mypassword"))  # Output: Created new user
print(login("john", "mypassword"))     # Output: Login Successful
print(login("john", "wrongpass"))      # Output: Login Failed
print(register("john", "anotherpass")) # Output: User already exists
