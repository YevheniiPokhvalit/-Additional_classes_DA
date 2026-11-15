# Вводь невід'ємну цілу кількість хвилин.
total_minutes = int(input("Тривалість у хвилинах: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Тривалість: {hours} год {minutes} хв")
