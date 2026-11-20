def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def capitalize_words(text):
    return text.title()

def remove_spaces(text):
    return text.replace(" ", "")

def word_count(text):
    return len(text.split())

def count_character(text, char):
    return text.count(char)

def demo():
    print("=== String Utilities Demo ===")
    text = "Hello World"

    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Vowels: {count_vowels(text)}")


if __name__ == "__main__":
    demo()