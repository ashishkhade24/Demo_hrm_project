from page_objects.admin_pages.pay_grades import Pay_Grade
import pytest
from page_objects.conftest import setup

@pytest.mark.usefixtures("setup")
class Test_Paygrade:

    def test_add_grade(self):
        obj=Pay_Grade(self.driver)
        obj.add_grade()

    def test_cancel_button(self):
        obj = Pay_Grade(self.driver)
        obj.cancel_button()

    def test_delete_employee(self):
        obj = Pay_Grade(self.driver)
        obj.delete_emp()



