import re
import math

# Simple password strength checker in Python
def password_strength(password):
    if not password:
        return "Password cannot be empty"

    length = len(password)

    # Character set size based on content
    char_set = 0
    if re.search(r'[a-z]', password):
        char_set += 26
    if re.search(r'[A-Z]', password):
        char_set += 26
    if re.search(r'[0-9]', password):
        char_set += 10
    if re.search(r'[^A-Za-z0-9]', password):
        char_set += 33

    # Entropy calculation
    entropy = length * math.log2(char_set) if char_set > 0 else 0

    # Strength label based on entropy
    if entropy < 28:
        strength = "Very Weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Fair"
    elif entropy < 128:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return f"Password: {password}\nLength: {length}\nEntropy: {entropy:.2f} bits\nStrength: {strength}"

# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print(password_strength(pwd))

