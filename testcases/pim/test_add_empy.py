import pytest
from page_objects.conftest import setup
from page_objects.PIM_pages.add_employee import Add_Employees

@pytest.mark.usefixtures("setup")
class Test_Add:

    def test_add_employee(self):
        obj=Add_Employees(self.driver)
        obj.add_emp()

