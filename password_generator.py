import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "========== PASSWORD GENERATOR ==========")

length = int(input(Fore.YELLOW + "Enter the desired password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    password += random.choice(characters)

print(Fore.GREEN + "\nGenerated Password:")
print(Fore.MAGENTA + password)

print(Fore.CYAN + "\n========== PASSWORD CREATED SUCCESSFULLY ==========")