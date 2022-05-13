from datetime import date, timedelta

class Student:
    """A Student class as base for method testing"""

<<<<<<< HEAD
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
=======
def __init__(self, first_name, last_name):
    self._first_name = first_name
    self._last_name = last_name
    self._start_date = date.today()
    self.end_date = date.today() + timedelta(days=365)
    self.naughty_list = False

>>>>>>> 3c4984d263c9fbe21dd2c471e2e7630e3e718e7c

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

<<<<<<< HEAD

if __name__ == '__main__':
    student = Student("John", "Baker")
    print(student)
=======
print("Hello")
>>>>>>> 3c4984d263c9fbe21dd2c471e2e7630e3e718e7c
