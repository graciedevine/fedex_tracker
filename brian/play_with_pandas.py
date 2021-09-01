import pandas as pd
from pathlib import Path

XL_FILE = Path("tracking.xlsx")


def create_example_xl():
    """Create an excel file to mimic original file.

    This shoud not be used in your script, this is just so I can have a file similar.
    """
    if XL_FILE.exists():  # Don't need to recreate it
        return

    df = pd.DataFrame(
        {
            "tracking": ["F12", "U23", "F34", "U45"],
            "invoice": ["I120", "I230", "I340", "I450"],
        }
    )
    df.to_excel(XL_FILE, index=False)


def download_fedex(tracking: str, invoice: str):
    """This represents all the work you already have going."""
    print(f"Downloading FedEx tracking number {tracking} for Invioce {invoice}")


def download_ups(tracking: str, invoice: str):
    """This represents the FedEx script, but modified for UPS."""
    print(f"Downloading UPS tracking number {tracking} for Invioce {invoice}")


def is_fedex_number(tracking: str) -> bool:
    """Determine if the tracking number is FedEx or UPS.

    You'll have to find a way to represent how to differentiate the two.
    """
    return tracking[0] == "F"


def get_proofs_of_delivery_iterrows(excel_file: Path) -> None:
    """Read excel file and send requests to download proof of delivery."""
    data = pd.read_excel(excel_file)

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html
    #                           See this word? ^^^
    for row in data.iterrows():
        tracking, invoice = row[1]
        if is_fedex_number(tracking):
            download_fedex(tracking, invoice)
        else:
            download_ups(tracking, invoice)


def get_proofs_of_delivery_itertuples(excel_file: Path) -> None:
    """Read excel file and send requests to download proof of delivery."""
    data = pd.read_excel(excel_file)

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html
    # This is the way I'd recommend
    for row in data.itertuples():
        if is_fedex_number(row.tracking):
            download_fedex(row.tracking, row.invoice)
        else:
            download_ups(row.tracking, row.invoice)


def get_proofs_of_delivery_zip(excel_file: Path) -> None:
    """Read excel file and send requests to download proof of delivery."""
    data = pd.read_excel(excel_file)

    # https://docs.python.org/3/library/functions.html#zip
    tracking_numbers = data["tracking"]
    invoice_numbers = data["invoice"]
    for tracking, invoice in zip(tracking_numbers, invoice_numbers):
        if is_fedex_number(tracking):
            download_fedex(tracking, invoice)
        else:
            download_ups(tracking, invoice)


if __name__ == "__main__":
    create_example_xl()

    print("Iterating with iterrows")
    get_proofs_of_delivery_iterrows(XL_FILE)

    print("Iterating with itertuples")
    get_proofs_of_delivery_itertuples(XL_FILE)

    print("Iterating with zip")
    get_proofs_of_delivery_zip(XL_FILE)
