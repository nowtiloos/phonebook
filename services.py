import csv


def contact_manager(file: str, mode: str = "w", encoding: str = "utf-8"):
    with open(file=file, mode=mode, encoding=encoding, newline="") as csvfile:

        match mode:
            case "r":
                reader = csv.DictReader(csvfile)
                data: list[dict] = [row for row in reader]
                return data
