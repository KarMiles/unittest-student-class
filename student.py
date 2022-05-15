from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from urllib import response
import requests

class Student:
    """A Student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + relativedelta(years=1)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    def alert_santa(self):
        self.naughty_list = True


    def apply_extension(self, days):
        self.end_date += timedelta(days=days)
        # return self.end_date
    

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"


    def return_student_start_date(self):
        return self._start_date


    def given_extension(self):
        extended = self.end_date > date.today() + relativedelta(years=1)

        if extended:
            extended_message = "Student given extension"
        else:
            extended_message = "Student not given extension"

        print(extended_message)
        return extended_message
