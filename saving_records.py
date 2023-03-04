import csv
import os.path
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# check if file exists
if not os.path.isfile('saving_records.csv'):
    # create file if it does not exist
    with open('saving_records.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Amount','total'])

# initialize tkinter
root = tk.Tk()
root.title("Savings Tracker")

# create date label and entry
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# create amount label and entry
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# create summary label


# create submit button
def submit():
    date_str = date_entry.get()
    amount_str = amount_entry.get()
    date = datetime.strptime(date_str, '%Y-%m-%d')
    amount = float(amount_str)

    with open('saving_records.csv', mode='a' , newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date.date(), amount])
    
    total = get_total_amount()
    with open('saving_records.csv', mode='a' , newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Total', total])



submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, padx=5, pady=5)

def get_total_amount(file_path):
    total = 0
    with open(file_path, 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(csv_file)

        # read the CSV file and compute the total
        for row in csv_reader:
            if len(row) == 2:
                try:
                    amount = float(row[1])
                    total += amount
                except ValueError:
                    pass
        
        # update the total in the CSV file
        csv_file.seek(2)  # move the file pointer to the beginning of the file
        csv_writer.writerow(['Total', total])  # write the updated total to the file

    return total


    return total

def summarize():
    file_path = 'saving_records.csv'  # replace with your file path
    total = get_total_amount(file_path)
    messagebox.showinfo("Total Savings", "The total savings is {:.1f}".format(total))



summarize_button = tk.Button(root, text="Summarize", command=summarize)
summarize_button.grid(row=2, column=1, padx=5, pady=5)

# create exit button
def exit_program():
    if messagebox.askyesno("Exit", "Do you want to exit the program?"):
        root.destroy()

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()



































# import csv
# from datetime import datetime
# import os.path

# # check if file exists
# if not os.path.isfile('saving_records.csv'):
#     # create file if it does not exist
#     with open('saving_records.csv', mode='w') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Date', 'Category', 'Amount'])

# while True:
#     date_str = input('Enter date (YYYY-MM-DD): ')
    
#     amount_str = input('Enter amount: ')
#     date = datetime.strptime(date_str, '%Y-%m-%d')
#     amount = float(amount_str)

#     with open('saving_records.csv', mode='a' ) as file:
#         writer = csv.writer(file)
#         writer.writerow([date.date(), amount])

#     cont = input('Do you want to continue? (y/n): ')
#     if cont.lower() != 'y':
#         break
































































