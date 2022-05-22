import os

import pytest

from tests.conftest import DEFAULT_DRIVER_DIR
from webdriver_manager.core.download_manager import WDMDownloadManager
from webdriver_manager.core.http import WDMHttpClient
from webdriver_manager.core.utils import save_file, ChromeType
from webdriver_manager.drivers.chrome import ChromeDriver

download_manager = WDMDownloadManager()


def test_can_download_driver_as_zip_file(delete_drivers_dir):
    file = download_manager.download_file("http://chromedriver.storage.googleapis.com/2.26/chromedriver_win32.zip")
    assert file.filename == "driver.zip"
    archive = save_file(file, DEFAULT_DRIVER_DIR)
    assert archive.file_path == f"{DEFAULT_DRIVER_DIR}{os.sep}{file.filename}"
    assert archive.unpack(DEFAULT_DRIVER_DIR) == ["chromedriver.exe"]


def test_can_download_driver_as_tar_gz(delete_drivers_dir):
    file = download_manager.download_file(
        "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz")
    assert file.filename == 'geckodriver-v0.26.0-linux32.tar.gz'
    archive = save_file(file, DEFAULT_DRIVER_DIR)
    assert archive.file_path == f"{DEFAULT_DRIVER_DIR}{os.sep}{file.filename}"
    assert archive.unpack(DEFAULT_DRIVER_DIR) == ["geckodriver"]


@pytest.mark.parametrize('version', ["2.26", "latest"])
def test_can_download_chrome_driver(delete_drivers_dir, version):
    driver = ChromeDriver(name="chromedriver", version=version, os_type="win32",
                          url="http://chromedriver.storage.googleapis.com",
                          latest_release_url="http://chromedriver.storage.googleapis.com/LATEST_RELEASE",
                          chrome_type=ChromeType.GOOGLE, http_client=WDMHttpClient())

    file = download_manager.download_file(driver.get_url())
    assert file.filename == "driver.zip"
    archive = save_file(file, DEFAULT_DRIVER_DIR)
    assert archive.unpack(DEFAULT_DRIVER_DIR) == ["chromedriver.exe"]
