from pathlib import Path
from time import sleep
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver

gecko = GetGeckoDriver()
gecko.install()


def download_dir(directory: str = None) -> Path:
    """Set dowload directory.

    Defaults to `~/Downloads/` if no directory is given.
    """
    if directory is None:
        downloads = Path.home() / "Downloads"
    return Path(str(directory)).resolve()


def get_driver(downloads: Path) -> webdriver:
    """Setup webdriver options.

    Download PDF from firefox:
    https://stackoverflow.com/a/30455695
    """
    mime_types = "".join(
        [
            "application/pdf",
            "application/vnd.adobe.xfdf",
            "application/vnd.fdf",
            "application/vnd.adobe.xdp+xml",
        ]
    )
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", str(downloads))
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
    profile.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    profile.set_preference("pdfjs.disabled", True)

    driver = webdriver.Firefox(firefox_profile=profile)
    return driver


def open_proof_div(driver: webdriver, wait_time: int = 3) -> None:
    """Click button to open div for requesting proof.

    Since the button is not directly addressable by css selector,
    this loops through the buttons of the desired class and will
    click the button that has the text "proof" in it.
    """
    driver.implicitly_wait(wait_time)
    buttons = driver.find_elements_by_css_selector(".eye-brow-link")
    for button in buttons:
        if "proof" in button.text.lower():
            button.click()
            break


def click_view_pdf(driver: webdriver, wait_time: int = 1) -> None:
    """Click button to view PDF.

    Since the buttion is not directly addressable by css selector,
    this loops through the buttons of the desired class and will
    click the button that has the text "view pdf" in it.
    """
    driver.implicitly_wait(wait_time)
    buttons = driver.find_elements_by_css_selector(".pod button")
    for button in buttons:
        if "view pdf" in button.text.lower():
            button.click()
            break


def get_proof(tracking: str, downloads: Path) -> None:
    driver = get_driver(downloads)
    driver.get(
        f"https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber={tracking}"
    )
    open_proof_div(driver)
    click_view_pdf(driver)
    driver.close()

    sleep(1)
    try:
        file = downloads / "retrievePDF.pdf"
        file.rename(file.with_stem(f"Proof_for_{tracking}"))
    except FileNotFoundError:
        print(tracking)


if __name__ == "__main__":
    downloads = download_dir("PODs")
    tracking_numbers = [
        "923767089915",
        "191476657925",
        "191476658200",
        "191476658174",
        "191476658781",
        "191480054110",
    ]
    for tracking in tracking_numbers:
        get_proof(tracking, downloads)
