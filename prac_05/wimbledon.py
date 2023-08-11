FILENAME = "wimbledon.csv"


def get_records(filename):
    """This function is for getting records from list file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


