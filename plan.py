from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Plan:
    name: str
    can_download: bool
    can_stream: bool
    has_SD: bool
    has_HD: bool
    has_UHD: bool
    number_of_device: int
    content: list
    price: int

    def check_plan(self):
        table = [
            ["Service", "Detail"],
            ['Name Plan', self.name],
            ["Download", 'v' if self.can_download else '-'],
            ["Stream", 'v' if self.can_stream else '-'],
            ['SD', 'v' if self.has_SD else '-'],
            ['HD', 'v' if self.has_HD else '-'],
            ['UHD', 'v' if self.has_UHD else '-'],
            ['Number of Device', self.number_of_device],
            ['Content', self.content],
            ['Price', f'Rp {self.price:,}']
        ]

        print(tabulate(table, headers="firstrow"))


basic_plan = Plan(
    name = "Basic Plan",
    can_download = True,
    can_stream = True,
    has_SD = True,
    has_HD = False,
    has_UHD = False,
    number_of_device = 1,
    content = ['3rd party movie'],
    price = 120_000
)

standard_plan = Plan(
    name = "Standard Plan",
    can_download = True,
    can_stream = True,
    has_SD = True,
    has_HD = True,
    has_UHD = False,
    number_of_device = 2,
    content = ['3rd party movie', 'Sports'],
    price = 160_000
)

premium_plan = Plan(
    name = "Premium Plan",
    can_download = True,
    can_stream = True,
    has_SD = True,
    has_HD = True,
    has_UHD = True,
    number_of_device = 4,
    content = ['3rd party movie', 'Sports', 'Original Series'],
    price = 200_000
)