from page_objects.conftest import setup
import pytest
from page_objects.PIM_pages.configuration_page import Configuration
@pytest.mark.usefixtures("setup")
class Test_Check:

    def test_add_field(self):
        obj=Configuration(self.driver)
        obj.check_custom_field()

    @pytest.mark.skip(reason="my will")
    def test_cancel_button(self):
        obj=Configuration(self.driver)
        obj.check_cancel_button()

    def test_delete_field(self):
        obj=Configuration(self.driver)
        obj.delete_user()

