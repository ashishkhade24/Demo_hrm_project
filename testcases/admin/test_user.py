import pytest
from page_objects.admin_pages.user_page import Users
from page_objects.conftest import setup

@pytest.mark.usefixtures("setup")
class Test_Search_User:

    def test_user_search(self):
        obj=Users(self.driver)
        obj.search_user()



