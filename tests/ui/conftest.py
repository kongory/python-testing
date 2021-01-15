from pathlib import Path

import allure
import pytest
from slugify import slugify


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call" and call.excinfo is not None:
        page = item.funcargs["page"]
        screenshot_dir = Path(Path(__file__).parent.parent / ".playwright-screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        page.screenshot(path=str(screenshot_dir / f"{slugify(item.nodeid)}.png"))
        allure.attach.file(str(screenshot_dir / f"{slugify(item.nodeid)}.png"),
                           attachment_type=allure.attachment_type.PNG)
