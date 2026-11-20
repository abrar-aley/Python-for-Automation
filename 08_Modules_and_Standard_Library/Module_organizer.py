import String_utils as su
import Math_utils as mu
import List_utils as lu

text = "Hello World"
numbers = [4, 2, 7, 1, 2, 9, 7]

print("=== String Utilities ===")
print(su.reverse_string(text))
print(su.count_vowels(text))
print(su.is_palindrome("racecar"))
print(su.capitalize_words("python is awesome"))
print(su.word_count(text))

print("\n=== Math Utilities ===")
print(mu.add(10, 5))
print(mu.divide(20, 4))
print(mu.factorial(5))
print(mu.square(12))
print(mu.is_even(17))

print("\n=== List Utilities ===")
print(lu.find_max(numbers))
print(lu.find_min(numbers))
print(lu.remove_duplicates(numbers))
print(lu.sort_list(numbers))
print(lu.reverse_list(numbers))
print(lu.sum_list(numbers))
print(lu.average_list(numbers))
print(lu.search_item(numbers, 7))