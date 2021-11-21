from calendar import month_name


class DVD:
    def __init__(self, name, id: int, creation_year, creation_month: str, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction):
        month_year_data = date.split(".")
        month = month_name[int(month_year_data[1])]
        year = int(month_year_data[2])
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
