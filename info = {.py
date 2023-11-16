info = {
    'ID': 1,
    'Прізвище' : 'Свінціцька',
    "Ім'я" : 'Марія',
    'Група': 'Іпзс-23-2',
    'Курс': 1,
    'Книги (борг)': [],
    'Статистика книг': []
}

def reader_card(info):
    print("Карта читача:")
    for key, value in info.items():
        print(f"{key}: {value}")



while True:
    print("\nОберіть дію:")
    print("1. Вивести карту читача")
    print("2. Взяти книгу")
    print("3. Повернути книгу")
    print("0. Вихід")

    choice = input("Введіть номер дії: ")

    if choice == '1':
        reader_card(info)
    elif choice == '2':
        book_name = input("Введіть назву книги, яку ви бажаєте взяти: ")
        info['Книги (борг)'].append(book_name)
        print(f"Книга '{book_name}' додана до списку боргу.")
    elif choice == '3':
        return_books = info['Книги (борг)']
        if not return_books:
            print("Список боргу порожній.")
        else:
            print("Список книг у боргу:")
            for book in return_books:
                print(book)
            book_name = input("Введіть назву книги, яку ви бажаєте повернути: ")
            if book_name in return_books:
                return_books.remove(book_name)
                info['Статистика книг'].append(book_name)
                print(f"Книгу '{book_name}' повернуто.")
            else:
                print("Книга не знайдена у списку боргу.")
    elif choice == '0':
        print("Дякуємо за користування бібліотекою. Програма завершена.")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")