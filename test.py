from datetime import datetime, timedelta
from flask import json
import yahoo_fin.stock_info as si
import pandas as pd


# print(si.get_live_price('FB'))

# print(si.get_quote_data('FB'))

# print(si.get_earnings_history('FB'))

# -----------------------------------------------------------------------------

# my_dict = si.get_quote_table('FB')
# print(type(my_dict))
# print(my_dict)
# print(my_dict['1y Target Est'])
# print(str(my_dict['1y Target Est']))

# -----------------------------------------------------------------------------


# base = datetime.today()
# numdays = 7
# date_list = [base + timedelta(days=x) for x in range(numdays)]
# for fecha in date_list:
#     print(fecha)

# desde = datetime(2021, 3, 2)
# hasta = datetime(2021, 3, 4)

# numdays = abs((hasta - desde).days) + 1
# date_list = [desde + timedelta(days=x) for x in range(numdays)]
# for fecha in date_list:
    # print(fecha)
    # print(si.get_earnings_for_date(fecha))

# for i in range(5):
#     print(si.get_earnings_for_date(datetime(2020,4,1 + i)))

# -----------------------------------------------------------------------------
# try:
#     pd = si.get_dividends("MO")
#     print(type(pd))
#     print(pd)
#     print("OK")
# except:
#     print("Error")
# finally:
#     print("End")

# -----------------------------------------------------------------------------
# print(si.get_quote_data("MO")["shortName"])
# -----------------------------------------------------------------------------
# Pandas dataframe
# df = si.get_data("MO", None, None, True, "1mo")
# df.to_csv("hist_stock_price_data.csv")    

# print(si.get_cash_flow("MO"))

# print(si.get_day_most_active())

# data = si.get_futures()
# print(data)

print(si.get_market_status())
