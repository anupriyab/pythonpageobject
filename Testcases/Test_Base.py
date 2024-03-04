import pytest


@pytest.mark.usefixtures("log_on_failure","launch_browser")
class Test_BaseTest:
    pass
