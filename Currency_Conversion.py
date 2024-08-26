## Libraries import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

## Major setting - fields, tabs, currencies

# Define the conversion rates (hardcoded)
conversion_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "AUD": 1.35,
    "CAD": 1.25,
    "CHF": 0.91,
    "CNY": 6.45,
    "SEK": 8.7,
    "NZD": 1.4,
    "BGN": 1.95,
    "INR": 74.5,
    "BRL": 5.2,
    "MXN": 20.3,
    "ZAR": 15.2,
    "RUB": 73.1,
    "SGD": 1.34,
    "HKD": 7.77
}

# Getting the conversion rate
def get_conversion_rate(currency):
    return conversion_rates.get(currency, None)

root = Tk()
root.title('Currency Converter')
root.geometry("500x500")

# Setting the background color and font colors
root.configure(bg='#1e1e2f')

# Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=10)

# Frames
currency_frame = Frame(my_notebook, width=480, height=480, bg='#1e1e2f')
conversion_frame = Frame(my_notebook, width=480, height=480, bg='#1e1e2f')

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# Adding Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# Disable tab 2 until Tab 1 is locked; Find lock definition below:
my_notebook.tab(1, state='disabled')

################################### CURRENCY ###################################

## Lock Definition:
def lock():
    if not home_currency.get() or not conversion_currency.get():
        messagebox.showwarning("WARNING!", "Did you fill all the fields?")    
    else:
        # Disable dropdowns
        home_currency_menu.config(state="disabled")
        conversion_currency_menu.config(state="disabled")
        # Enable tab
        my_notebook.tab(1, state='normal')
        # Change Tab Field
        amount_label.config(text=f'Amount of {home_currency.get()} To Convert To {conversion_currency.get()}', fg='white')
        converted_label.config(text=f'Equals This Many {conversion_currency.get()}', fg='white')
        convert_button.config(text=f'Convert From {home_currency.get()}', fg='white', bg='#5a9')

def unlock():
    # Enable dropdowns
    home_currency_menu.config(state="normal")
    conversion_currency_menu.config(state="normal")
    # Disable Tab
    my_notebook.tab(1, state='disabled')

home = LabelFrame(currency_frame, text="Currency To Convert", bg='#1e1e2f', fg='white')
home.pack(pady=20)

# Home currency dropdown menu
home_currency = StringVar()
home_currency.set("Select Currency")
home_currency_menu = OptionMenu(home, home_currency, *conversion_rates.keys())
home_currency_menu.config(font=("Lucida Console", 24), bg='#5a9', fg='white', bd=5, highlightthickness=0)
home_currency_menu['menu'].config(bg='#5a9', fg='white')
home_currency_menu.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="Convert To", bg='#1e1e2f', fg='white')
conversion.pack(pady=20)

# Convert to label
conversion_label = Label(conversion, text="Currency", bg='#1e1e2f', fg='white')
conversion_label.pack(pady=10)

# Conversion currency dropdown menu
conversion_currency = StringVar()
conversion_currency.set("Select Currency")
conversion_currency_menu = OptionMenu(conversion, conversion_currency, *conversion_rates.keys())
conversion_currency_menu.config(font=("Lucida Console", 24), bg='#5a9', fg='white', bd=5, highlightthickness=0)
conversion_currency_menu['menu'].config(bg='#5a9', fg='white')
conversion_currency_menu.pack(pady=10, padx=10)

# Button Frame
button_frame = Frame(currency_frame, bg='#1e1e2f')
button_frame.pack(pady=20)

# Creating Buttons
lock_button = Button(button_frame, text="Lock", command=lock, fg='white', bg='#a56', bd=0, highlightthickness=0)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock, fg='white', bg='#808080', bd=0, highlightthickness=0)
unlock_button.grid(row=0, column=1, padx=10)

################################### CONVERSION ###################################

def convert():
    # Clear Converted Entry Box
    converted_entry.delete(0, END)
    
    try:
        # Get the amount to convert
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "The number you entered was not valid.")
        return

    # Get the home and conversion rates
    home_rate = get_conversion_rate(home_currency.get())
    conversion_rate = get_conversion_rate(conversion_currency.get())
    
    if home_rate is None or conversion_rate is None:
        messagebox.showwarning("WARNING!", "Conversion rate not found!")
        return

    # Convert the amount from home currency to the target currency
    converted_amount = (amount / home_rate) * conversion_rate

    # Convert to two decimals and add commas
    converted_amount = round(converted_amount, 2)
    formatted_amount = '{:,}'.format(converted_amount)

    # Update the converted entry box
    converted_entry.insert(0, f'{formatted_amount}')

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text="Amount To Convert", bg='#1e1e2f', fg='white')
amount_label.pack(pady=20)

## Labels and Buttons
# Entry Box For Amount
amount_entry = Entry(amount_label, font=("Lucida Console", 24), fg='white', bg='#2e2e3f', bd=2, relief='solid')
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(amount_label, text="Convert", command=convert, fg='white', bg='#5a9', bd=5, highlightthickness=0)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency", bg='#1e1e2f', fg='white')
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(converted_label, font=("Lucida Console", 24), fg='white', bg='#2e2e3f', bd=2, relief='solid')
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conversion_frame, text="Clear", command=clear, fg='white', bg='#5a9', bd=5, highlightthickness=0)
clear_button.pack(pady=20)

# Fake Label for spacing
spacer = Label(conversion_frame, text="", width=68, bg='#1e1e2f')
spacer.pack()

root.mainloop()
