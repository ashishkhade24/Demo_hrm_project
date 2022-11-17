import pytest
from page_objects.conftest import setup
from page_objects.admin_pages.job_empy_status import Emp_Status

@pytest.mark.usefixtures("setup")
class Test_Employee:

    def test_add_employees(self):
        obj=Emp_Status(self.driver)
        obj.add_employee()

    def test_cancel_button(self):
        obj=Emp_Status(self.driver)
        obj.check_cancel()

