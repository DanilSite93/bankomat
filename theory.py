class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def code(self):
        print(f"{self.name} пишет код на языке {self.language}")

    def debug(self):
        print(f"{self.name} исправляет ошибки в программе")

    def info(self):
        print(f"Привет меня зовут {self.name}, мне {self.age}, я знаю язык {self.language}")

class BackendR(Programmer):
    def __init__(self, name, age, language, website):
        super().__init__(name, age, language)
        self.website = website

    def setup_website(self):
        print(f"{self.name} работает над сайтом {self.website}")

class FrontendR(Programmer):
    def __init__(self, name, age, language, IDLE, sait):
        super().__init__(name, age, language)
        self.idle = IDLE
        self.sait = sait

    def editor(self):
        print(f"{self.name} пишет в программе {self.idle}")

    def work_website(self):
        print(f"{self.name} создаёт дизайн сайта {self.sait}")



backender = BackendR("Мария", 29, "Python", "VK")
backender.code()
backender.debug()
backender.setup_website()

frontender = FrontendR("Кирилл", 62, "HTML+CSS","VS code", "Яндекс")
frontender.info()
frontender.editor()
frontender.work_website()

# frontender.setup_website() нельзя вызвать метод одного дочернего класса из другого дочернего класса