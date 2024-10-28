# Program liczący wystąpienia słów w tekście

# Pobieramy tekst od użytkownika
text = input("Wprowadź tekst: ")

# Zmieniamy wszystko na małe litery i dzielimy tekst na słowa
words = text.lower().split()

# Tworzymy słownik, aby zliczać wystąpienia słów
word_count = {}

# Iterujemy po każdym słowie w tekście
for word in words:
    if word in word_count:
        word_count[word] += 1  
    else:
        word_count[word] = 1    

# Wyświetlamy wyniki
print("\nWystąpienia słów:")
for word, count in word_count.items():
    print(f"{word}: {count}")

