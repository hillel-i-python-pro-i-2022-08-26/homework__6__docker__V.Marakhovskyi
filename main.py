from faker import Faker
from prettytable import PrettyTable

fake = Faker()
table = PrettyTable()


def generate_table():
    table.field_names = ["Name", "Phone number", "City"]
    for _ in range(5):
        table.add_row([fake.first_name(), fake.phone_number(), fake.city()])
    print(table)


if __name__ == "__main__":
    generate_table()
