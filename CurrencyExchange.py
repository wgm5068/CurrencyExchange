#!/usr/bin/python

import tkinter as tk
import requests as rq

# The Pennsylvania State University, May 2022
# Wilson Miller

# Rewritten version of a simple currency exchange program. This program was originally written when
# ExchangeRateAPI did not require a subscription to set a base currency. This version has not been
# updated to allow users to convert USD to a given currency, rather it uses the EUR as the base.

# Replace 'USER-API-KEY' with your API key (free key needed).
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=USER-API-KEY&format=1'
response = rq.get(url)
print(response.json())
dictionary = response.json()['rates']
print(dictionary)

# Print all keys and values in the exchange dictionary
# for key in current_rates:
#    print(key, current_rates[key])
currency_name = list(dictionary)
currency_rate = list(dictionary.values())


# Handles "Enter" event for both input boxes
def exchange_rate(event):
    curr_amt = boxCurAmt.get()
    curr_name = boxName.get()
    convert_value = conversion(curr_amt, curr_name)

    display.configure(text="Converted Amount " + str(convert_value))  # Updates display to CA


# Conversion of EUR -> requested currency
def conversion(curr_amt, curr_name):
    index_cur_name = currency_name.index(curr_name)
    index_cur_exchange = currency_rate[index_cur_name]

    conv_cur = float(curr_amt) * index_cur_exchange
    return round(conv_cur, 2)


master = tk.Tk()
master.geometry('750x750')
master.title("Dynamic Currency Exchange Rate for the EUR")
tk.Label(master, text="Dynamic Currency Exchange Rate Calculator\n Created by: Wilson Miller\n May 2021").pack()

# Handles input of how much user wants to convert in EUR
tk.Label(master, text="EUR Amount to be Converted").pack()
boxCurAmt = tk.Entry(master)
boxCurAmt.bind("<Return>", exchange_rate)
boxCurAmt.pack()

tk.Label(master, text="Name of Currency").pack()
boxName = tk.Entry(master)
boxName.bind("<Return>", exchange_rate)
boxName.pack()

tk.Label(master, text="Available Currency Names:").pack()
tk.Label(master, text=currency_name, wraplength=250).pack()

display = tk.Label(master)
display.pack()

master.mainloop()
