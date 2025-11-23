print("Hello world!")

message = ("Hello world!")
print(message)

name = "ada lovelace"
print(name.title())

name = "ada lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# Eliminar prefijos.
nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')

print(nostarch_url)