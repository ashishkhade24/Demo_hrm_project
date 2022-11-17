from page_objects.conftest import setup
from page_objects.admin_pages.job_titles import JOB
import pytest

@pytest.mark.usefixtures("setup")
class Test_Job_page:

    def test_job(self):
        obj=JOB(self.driver)
        obj.goto_job_title()

    def test_delete_select(self):
        obj=JOB(self.driver)
        obj.delete_select()

    def test_delete_btn(self):
        obj=JOB(self.driver)
        obj.delete_btn()

    def test_edit_option(self):
        obj = JOB(self.driver)
        obj.edit_option()





