import datetime

from user import User
from plan import basic_plan, premium_plan, standard_plan

shandy = User("Shandy", basic_plan, datetime.date(2022,6,19))
cahya = User("Cahya", standard_plan, datetime.date(2021,3,19))
ana = User("Ana", standard_plan, datetime.date(2019,1,2))
bagus = User("Bagus", basic_plan, datetime.date(2022,7,22))

# check all plan
cahya.check_all_plan()

# check current plan
shandy.current_plan.check_plan()

# upgrade ke premium plan
print(ana.upgrade_plan(premium_plan))

# redeem code new user
faizal = User("Faizal", standard_plan, datetime.date.today())
print(faizal.redeem_code(bagus.referral_code))