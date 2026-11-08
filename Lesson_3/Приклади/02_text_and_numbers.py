# Ті самі введені символи можна використати як текст або як числа.
first_text = input("Перше ціле число: ")
second_text = input("Друге ціле число: ")

joined_text = first_text + second_text
first_number = int(first_text)
second_number = int(second_text)
total = first_number + second_number

print(f"З'єднання тексту: {joined_text}")
print(f"Сума чисел: {total}")
print("Тип першого введення:", type(first_text))
print("Тип після перетворення:", type(first_number))
