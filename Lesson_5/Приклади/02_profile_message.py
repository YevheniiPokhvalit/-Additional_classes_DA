# Зберігаємо введений текст, щоб порівняти його з результатом.
raw_nickname = input("Псевдонім: ")
raw_message = input("Повідомлення: ")

clean_nickname = raw_nickname.strip()
profile_id = clean_nickname.lower().replace(" ", "_")
clean_message = raw_message.strip().replace("!", ".")
preview = clean_message[:10]

print("ПРОФІЛЬ\n--------")
print(f"Ідентифікатор: [{profile_id}]")
print(f"Довжина ідентифікатора: {len(profile_id)}")
print(f"Повідомлення: [{clean_message}]")
print(f"Перші 10 символів: [{preview}]")
