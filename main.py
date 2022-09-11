"""
Joseph Dowdy
MIS 315, Summer 1st Session 2022 - Section 1
7/1/22
Final Assignment, MSRP Comparison Project
I, Joseph Dowdy, can attest that this script is my work and my work alone, enjoy! :-)

Please refer to my submitted word doc for more details on this project.
"""

# -------------------------------------------------- Imports ---------------------------------------------------------#
import csv
import tkinter
import tkinter.ttk
import tkinter.messagebox

# -------------------------------------------------- Variables -------------------------------------------------------#
HEADER = ["Seller", "Car Make and Model", "Year", "MSRP", "User Found Price", "Good Deal?"]

cars = []
csv_file = []
options = ["View Records", "Clear Records", "Close Application"]
msrp_price = 0.0

overall_bg_color = "#faf0ca"
button_colors = ["lightgreen", "#f9844a", "#e36414", "#f8961e"]
msrp_data_str = ""

# -------------------------------------------------- Functions -------------------------------------------------------#


def format_str_to_int(str_: str):
    """This function serves to take in the non formatted msrp string from the data set and it turns it into a comparable
    numeric value. The return result is an integer"""
    str_filter = filter(str.isdigit, str_)
    formatted_string = "".join(str_filter)
    return int(formatted_string)


def compute_comparison():
    """This function serves to compare user entered values to actual MSRP and provides analysis"""
    car_entered = car_options.get()
    seller_ = seller_entered.get()
    global msrp_data_str

    # This handles if a user enters an acceptable price entry (float or integer)
    try:
        user_price = float(price_entered.get())

        # This handles the case where a user enters a negative price (not possible)
        if user_price < 0:
            raise Exception

        # This handles if the user selected an accepted car make and model
        try:

            # iterating through dataset to see if entered car make and model match any data points
            for row_ in csv_file:

                if car_entered == row_[1]:
                    msrp_data_str = row_[2]

            msrp_data = format_str_to_int(msrp_data_str)
            result_tuple = compare_two_numbers(msrp_data, user_price)

            # User is paying MSRP
            if result_tuple[0] == 0.0:

                good_deal = True
                write_to_file(car_entered, msrp_data, user_price, good_deal, seller_)
                tkinter.messagebox.showinfo("Fair Price", "Fair price, you are paying the MSRP price. Data has been "
                                                          "written to main_record.csv, go take a look.")
            # User is paying less than MSRP
            elif result_tuple[0] < 0:

                good_deal = True
                write_to_file(car_entered, msrp_data, user_price, good_deal, seller_)
                tkinter.messagebox.showinfo("Good Price", f"You would be paying {round(result_tuple[1] * 100, 2)}% "
                                                          f"under MSRP. Data has been written to main_record.csv, go "
                                                          f"take a look.")

            # User is paying over MSRP
            else:
                good_deal = False
                write_to_file(car_entered, msrp_data, user_price, good_deal, seller_)
                tkinter.messagebox.showinfo("Bad Price", f"You would be paying {round(result_tuple[1] * 100, 2)}% over "
                                                         f"MSRP. Data has been written to main_record.csv, go take a "
                                                         f"look.")
            msrp_data_str = ""

            # resetting entry boxes and combobox
            price_entered.delete(0, "end")
            seller_entered.delete(0, "end")
            car_options.set('')

        # Car make and model is not supported
        except:
            tkinter.messagebox.showwarning("Warning", "Unfortunately that car make and model is not currently "
                                                      "supported. Please try another.")
            msrp_data_str = ""

    # User entered price is not accepted
    except:
        tkinter.messagebox.showwarning("Warning", "Please enter a positive number in the price found field")
        msrp_data_str = ""


def write_to_file(car, msrp, entered_price, good_deal, seller):
    """This function accepts car make and model, said MSRP, user entered price, boolean, and car seller and runs logic
    to write the appropriate output to the main_records.csv"""
    if good_deal:
        good_deal = "Yes"
    else:
        good_deal = "No"
    if seller == "" or seller is None:
        seller = "No seller entered"

    row_to_write = [seller, car, 2021,  msrp, entered_price, good_deal]

    with open("main_record.csv", "a") as file_:
        writer_ = csv.writer(file_)
        writer_.writerow(row_to_write)


def compare_two_numbers(msrp_int: float, user_int: float):
    """This function accepts two integers and returns a tuple with the difference and percentage difference as a
    fraction"""
    difference = user_int - msrp_int
    percentage_dif = abs(difference) / msrp_int
    return float(difference), float(percentage_dif)


def quit_application():
    """When called this function quits the application"""
    root.destroy()
    print("Application successfully closed.")


def clear_main_record():
    """When called this function clears the main_record.csv"""
    # Opens main_record.csv and just writes the HEADER list onto it, ultimately "resetting" it
    with open("main_record.csv", "w") as file_:
        writer_ = csv.writer(file_)
        writer_.writerow(HEADER)
    tkinter.messagebox.showinfo("Success", "The main_record.csv has successfully been cleared.")


def view_main_record():
    """This function opens the main record as a GUI new window"""
    new_window = tkinter.Toplevel()
    new_window.title("Main Record - Viewer")

    # Reading from main_record.csv
    with open("main_record.csv", "r") as file_:
        reader_ = csv.reader(file_)
        data_ = list(reader_)

        # after reading main_record.csv this logic iterates through and writes corresponding output onto the new window
        # This section was inspired by a stackoverflow post - reference posted on submitted word doc
        for i, row_ in enumerate(data_, start=0):
            for col in range(0, 6):
                tkinter.Label(new_window, text=row_[col]).grid(row=i, column=col, padx=40)


def option_menu_clicked():
    """This function serves to perform logic on the option combo box to see user submitted option and call the
    appropriate function when clicked"""
    option_entered = option_menu.get()
    if option_entered == "View Records":
        view_main_record()
    elif option_entered == "Clear Records":
        clear_main_record()
    elif option_entered == "Close Application":
        quit_application()


# ------------------------------------------- Main Logic & GUI Setup -------------------------------------------------#

# First try-except block checks that msrp_data.csv and ascii_logo.txt are both available
try:
    with open("ascii_logo", "r") as file:
        ascii_logo = file.read()

    data = csv.reader("msrp_data.csv")
    print("'msrp_data.csv' and 'ascii_logo.txt' were loaded successfully.")

    # opening the dataset and appending to various lists used for the application
    with open("msrp_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            csv_file.append(row)
            cars.append(row[1])
        cars = cars[1:]

    # Checks if main_record.csv exists, if not then it is created
    try:
        with open("main_record.csv", "r") as file:
            print("'main_record.csv' loaded successfully.")

    except:
        with open("main_record.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)
            print("'main_record.csv' created.")

    # Main window setup and configuration
    root = tkinter.Tk()
    root.title("Car Price Navigator")
    root.configure(bg=overall_bg_color)

    # Various label setups and configurations
    ascii_label = tkinter.Label(root, text=ascii_logo)
    ascii_label.configure(bg=overall_bg_color, font="Courier", justify="left")
    ascii_label.grid(columnspan=3, row=0, column=0)

    car_label = tkinter.Label(root, text="Car make and model: ")
    car_label.configure(bg=overall_bg_color)
    car_label.grid(column=0, row=1)

    price_entry_label = tkinter.Label(root, text="Price found for car: ")
    price_entry_label.configure(bg=overall_bg_color)
    price_entry_label.grid(column=0, row=2)

    seller_entry_label = tkinter.Label(root, text="Seller: ")
    seller_entry_label.configure(bg=overall_bg_color)
    seller_entry_label.grid(column=0, row=3)

    option_label = tkinter.Label(root, text="Option Menu: ")
    option_label.configure(bg=overall_bg_color)
    option_label.grid(column=0, row=4)

    # Combo boxes setup and configuration
    car_options = tkinter.ttk.Combobox(root, values=cars, width=25)
    car_options.grid(column=1, row=1)

    option_menu = tkinter.ttk.Combobox(root, values=options, width=25)
    option_menu.configure(state="readonly")
    option_menu.current(0)
    option_menu.grid(column=1, row=4)

    # Entry boxes setup and configuration
    price_entered = tkinter.Entry(root, width=26)
    price_entered.grid(column=1, row=2)

    seller_entered = tkinter.Entry(root, width=26)
    seller_entered.grid(column=1, row=3, pady=7.5)

    # Button setup and configuration
    compute_button = tkinter.Button(root, text="Analyze", command=compute_comparison)
    compute_button.configure(highlightbackground=button_colors[0], width=15, bg=button_colors[0])
    compute_button.grid(column=2, row=1, padx=5, pady=7.5)

    option_button = tkinter.Button(root, text="Choose Option", command=option_menu_clicked)
    option_button.configure(highlightbackground=button_colors[1], width=15, bg=button_colors[1])
    option_button.grid(column=2, row=4)

    root.mainloop()

except:
    print("Double check that msrp_data.csv and ascii_logo.txt are properly loaded.")
