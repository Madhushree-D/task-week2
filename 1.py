# Initial user list
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Create - Add a new user
def add_user(user_id, name, email):
    for user in users:
        if user["id"] == user_id:
            print(f"User with id {user_id} already exists.")
            return
    users.append({"id": user_id, "name": name, "email": email})
    print("User added successfully.")

# Read - Retrieve user by ID
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return "User not found."

# Update - Update user by ID
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print("User updated successfully.")
            return
    print("User not found.")

# Delete - Remove user by ID
def delete_user(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            print("User deleted successfully.")
            return
    print("User not found.")

# Sample usage
add_user(3, "Charlie", "charlie@example.com")
print(get_user(1))
update_user(2, email="bob123@example.com")
delete_user(1)
print(users)
