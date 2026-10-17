def test_login(username, password):
    if username == "student1" and password == "pass123":
        return "Login successful"
    return "Invalid username or password"


print(test_login("student1", "pass123"))
print(test_login("student1", "wrong123"))

print(test_login("", ""))