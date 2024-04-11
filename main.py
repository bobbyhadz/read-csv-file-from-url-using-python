# Reading a CSV file from a URL using Python and Pandas

import pandas as pd

url = "https://gist.githubusercontent.com/bobbyhadz/9061dd50a9c0d9628592b156326251ff/raw/381229ffc3a72c04066397c948cf386e10c98bee/employees.csv"

data = pd.read_csv(
    url,
    sep=',',
    encoding='utf-8',
)

#   first_name last_name        date
# 0      Alice     Smith  2023-01-05
# 1      Bobby      Hadz  2023-03-25
# 2       Carl     Lemon  2021-01-24
print(data)