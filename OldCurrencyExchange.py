import tkinter as tk
import requests as rq

response = rq.get("https://api.exchangeratesapi.io/latest?base=USD")
current_rates = response.json()['rates']  # prints just rates
cur_name = list(current_rates.keys())
cur_exchange = list(current_rates.values())

# Handles "Enter" event for both input boxes
def exchange_rate(event):
    curr_amt = boxCurAmt.get()
    curr_name = boxName.get()
    convert_value = conversion(curr_amt, curr_name)

    display.configure(text="Converted Amount " + str(convert_value))  # Updates display to CA


# Conversion of USD -> requested currency
def conversion(curr_amt, curr_name):
    index_cur_name = cur_name.index(curr_name)
    index_cur_exchange = cur_exchange[index_cur_name]
    conv_cur = float(curr_amt) * index_cur_exchange
    return conv_cur

# GUI Builder
master = tk.Tk()
master.geometry('500x500')
master.title("Static Currency Exchange Rate")
tk.Label(master, text="Static Currency Exchange Rate Calculator\n Created by: Wilson Miller\n January 2021").pack()

# Handles input of how much user wants to convert in USD
tk.Label(master, text="USD Amount to be Converted").pack()
boxCurAmt = tk.Entry(master)
boxCurAmt.bind("<Return>", exchange_rate)
boxCurAmt.pack()

tk.Label(master, text="Name of Currency").pack()
boxName = tk.Entry(master)
boxName.bind("<Return>", exchange_rate)
boxName.pack()

tk.Label(master, text="Available Currency Names:").pack()
tk.Label(master, text=cur_name).pack()

display = tk.Label(master)
display.pack()

master.mainloop()
