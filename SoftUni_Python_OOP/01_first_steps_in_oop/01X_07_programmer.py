class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.skills = skills
        self.language = language

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:  # language in different scope
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"

        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if skills_needed <= self.skills:
            if new_language == self.language:
                return f"{self.name} already knows {new_language}"
            else:
                previous_language = self.language
                self.language = new_language
                return f"{self.name} switched from {previous_language} to {new_language}"
        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))