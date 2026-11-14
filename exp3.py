# Создай родительский класс Book, который содержит атрибуты title, author и метод get_description(), 
# который выводит "Книга {title}, автор: {author}.". Создай два дочерних класса:
# Fiction, который добавляет метод get_genre(), выводящий "Жанр: художественная литература."
# NonFiction, который добавляет метод get_genre(), выводящий "Жанр: научно-популярная литература."


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_description(self):
        print(f"Книга {self.title}, автор: {self.author}.")


class Fiction(Book):
    def get_genre(self):
        print("Жанр: художественная литература.")


class NonFiction(Book):
    def get_genre(self):
        print("Жанр: научно-популярная литература.")


book1 = Fiction("Война и мир", "Лев Толстой")
book2 = NonFiction("Краткая история времени", "Стивен Хокинг")

book1.get_description()
book1.get_genre()

book2.get_description()
book2.get_genre()
