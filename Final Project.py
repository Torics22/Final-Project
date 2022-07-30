from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Loan and Investment Banking")
root.geometry("450x120")

#these are the investment menu commands
def invest():
    invest = Toplevel()
    invest.title("Investment Opportunities")
    invest_banner = Label(invest, text = "Welcome to Loan and Investment Bankings' Investment window.\n Please choose which investments you would like to look at.")
    invest_banner.grid(row=0, column=0, rowspan=2, columnspan=2)
    button_SMP = Button(invest, text = "Slow return Loans", padx=50, pady=20, command=slow)
    button_SMP.grid(row=2, column=0)
    button_stock = Button(invest, text = "Fast and Risker loans", padx=50, pady=20, command=fast_message)
    button_stock.grid(row=2, column=1)
    invest.mainloop()

#These are the investment menu buttons, labels, and where they are placed in the application    
def slow():
    global amount_entry, time_entry, application

    slow = Toplevel()
    application = "invest"
    slow.title("SMP Investments")

    investment_label = Label(slow, text="Slow investments return a profit slower, but are more stable\n and reliable.")
    investment_label.grid(row=0, column=0, columnspan=5)

    amount_label = Label(slow, text = "Enter the principal (intial amount):")
    amount_label.grid(row=1, column=0)
    amount_entry = Entry(slow, width=35, borderwidth=5)
    amount_entry.grid(row=1, column=1, columnspan=5, padx=10, pady=10)

    time_label = Label(slow, text="Enter how long you will invest (monthly):")
    time_label.grid(row=2, column=0)
    time_entry = Entry(slow, width=35, borderwidth=5)
    time_entry.grid(row=2, column=1, columnspan=5, padx=10, pady=10)

    button_calculate = Button(slow, text = "Calculate", padx=50, pady=20, command = calculate)
    button_calculate.grid(row=3, column=1)
    slow.mainloop()
def fast_message():
    messagebox.showinfo("Fast and Risker investents Calculation","Coming Soon!")
#These are the loan menu buttons, labels, and where they are placed in the application
def loan():
    global loan_amount, loan_time, loan_interest, application

    application = "loan"
    loan = Toplevel()
    loan.title("Loans Calculator")

    amount_label = Label(loan, text="Enter the amount of the loan:")
    amount_label.grid(row=0, column=0)
    loan_amount = Entry(loan, width=35, borderwidth=5)
    loan_amount.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

    time_label = Label(loan, text="Enter the length of the loan in months:")
    time_label.grid(row=1, column=0)
    loan_time = Entry(loan, width=35, borderwidth=5)
    loan_time.grid(row=1, column=1, columnspan=5, padx=10, pady=10)

    int_label = Label(loan, text="Enter the interest rate in decimal form:")
    int_label.grid(row=2, column=0)
    loan_interest= Entry(loan, width=35, borderwidth=5)
    loan_interest.grid(row=2, column=1, columnspan=5, padx=10, pady=10)

    button_calculate = Button(loan, text = "Calculate", padx=50, pady=20, command = calculate)
    button_calculate.grid(row=3, column=1)
    loan.mainloop()
    
#This calculates the loan side of the program
def calculate():
    if application == "loan":
        global monthly_payment
        try:
            amount = float(loan_amount.get())
        except:
            messagebox.showinfo("Loan Calculator", "Amount of loan is not a number.\n Try again.")
        try:
            time = float(loan_time.get())
        except:
            messagebox.showinfo("Loan Calculator", "length of loan is not a number.\n Try again.")
        try:
            interest = float(loan_interest.get())
        except:
            messagebox.showinfo("Loan Calculator", "interest of loan is not a number.\n Try again.")
        monthly_payment=round((amount/time)*interest)
        loan_calc = messagebox.showinfo("Loan Calculator","Your monthly payment will be " + str(monthly_payment) + "$")
#This calculates the investment side of the program
    if application == "invest":
        global final_amount
        try:
            principal = float(amount_entry.get())
        except:
            messagebox.showinfo("Investment Calculator", "Princpal of loan is not a number.\n Try again.")            
        try:
            num_time = float(time_entry.get())
        except:
            messagebox.showinfo("Investment Calculator", "Time of loan is not a number.\n Try again.")
        interest_rate = float(.08)
        num_time = num_time/12
        final_amount = float(principal*(1+(interest_rate))**num_time)
        net_profit = round(final_amount-principal,2)
        invest_calc = messagebox.showinfo("Investment Calculator","Your investment will net you a total growth of " + str(net_profit))

#main menu buttons
button_investment = Button(root, text="Investment", padx=50, pady = 20, command = invest)
button_loan = Button(root, text="Loan", padx=50, pady = 20, command = loan)

button_investment.grid(row=2, column=0)
button_loan.grid(row=2, column=2)

button_exit = Button(root, text="Exit", padx=50, pady = 20, command = root.destroy)
button_exit.grid(row=3, column=1)

root.mainloop()
