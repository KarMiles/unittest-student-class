import unittest
from unittest.result import failfast
from student import Student
from datetime import date, timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    """ A Student class as a basis for method testing """

    # Use of the classmethod decorator signify
    # the method logic acts on the class itself instead of class instances
    @classmethod
    def setUpClass(cls):
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, "john.doe@email.com")


    def test_apply_extention(self):
        print('test_apply_extention')
        old_end_date = self.student.end_date
        self.student.apply_extension(30)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=30))


    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"    

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

    def test_return_student_start_date(self):
        print('test_return_student_start_date')

        start_date = self.student.return_student_start_date()
        today = date.today()
        self.assertEqual(start_date, today)
        print(today)

if __name__ == '__main__':
    unittest.main()