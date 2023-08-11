FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def get_records(filename):
    """This function is for getting records from list file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
    """This function is for creating dictionary of champions and set of countries"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """This function is for printing champion and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name,count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def main():
    """Main function for read data file"""
    records = get_records(FILENAME)
    champion_to_count, countries = process_data(records)
    display_results(champion_to_count, countries)


main()
