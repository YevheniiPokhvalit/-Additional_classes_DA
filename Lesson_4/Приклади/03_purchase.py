# Ціна й доставка невід'ємні, кількість додатна, знижка від 0 до 100.
unit_price = float(input("Ціна за одиницю, грн: "))
quantity = int(input("Кількість: "))
discount_percent = float(input("Знижка на товари, %: "))
delivery = float(input("Доставка, грн: "))

# Знижка поширюється лише на товари, а не на доставку.
subtotal = unit_price * quantity
discount = subtotal * discount_percent / 100
total = subtotal - discount + delivery

print(f"Товари: {subtotal:.2f} грн")
print(f"Знижка: {discount:.2f} грн")
print(f"До сплати: {total:.2f} грн")
