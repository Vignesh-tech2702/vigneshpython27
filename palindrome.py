from collections import deque

def palindrome(input_string):
    cleaned_chars = [char.lower() for char in input_string if char.isalnum()]
    cleaned_string = "".join(cleaned_chars)
    print(f'output: "{cleaned_string}"')
   
    char_deque = deque(cleaned_chars)
    is_palindrome = True
   
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            is_palindrome = False
            break
           
    if is_palindrome:
        print("palindrome")
    else:
        print("not a palindrome")
ui = input("Enter a string: ")
palindrome(ui)
