# PASSWORD GENERATOR
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
length = int(input("Enter the desired password length: "))
password = ""
index = 0

for i in range(length):
    index = (index + length + i) % len(characters)
    password += characters[index]
print("Generated Password:", password)