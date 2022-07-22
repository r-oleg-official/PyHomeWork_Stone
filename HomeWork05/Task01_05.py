exception_word = input("Введите исключающие символы одной строкой: ")

word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'.split()
print(f"Оригинальный текст: {' '.join(word)}")
result = [i for i in word if exception_word not in i]
print(f"Текст без слова {exception_word}: {' '.join(result)}")