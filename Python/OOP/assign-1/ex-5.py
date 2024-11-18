#5. Write a program to take multi-line input from the user.

user_text = []
print("Tell me about yourself.")

while True:
    text_line = input()
    if text_line:
        user_text.append(text_line)
    else:
        break
final_text = '\n'.join(user_text)
print()
print("---final text input---")
print()
print(final_text)
