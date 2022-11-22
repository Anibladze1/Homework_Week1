str_list = []

for _ in range(5):
    input_str = input("Enter string: ")
    str_list.append(input_str)


max_length = 0
for str_length in str_list:
    if len(str_length) > max_length:
        max_length = len(str_length)

print(f"Largest String Length is {max_length}")
