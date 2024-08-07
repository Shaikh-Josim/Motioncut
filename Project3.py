from prettytable import PrettyTable
import re, csv
import os

class ExpenseTracker():
    def __init__(self):
        self.openExpenseTracker("Expense_Tracker_Menu")
        self.expenseTrackerMenuChoice()
    
    def openExpenseTracker(self,menu_type,show=None) -> None:
        '''
        This function shows the menu of Expense Tracker in tabular format
        Args:
        menu_type(str): it is string which is use to determine what to show in tabular format
        '''
        if menu_type == "Expense_Tracker_Menu":
            show_menu = ["\tMain Menu:","1.Add Expense","2.View Monthly Summary","3.View Category-wise Expenditure","4.Exit"]
            table = PrettyTable(["Expense Tracker"])
            for row in show_menu:
                table.add_row([row])
            table.align = "l"
            table._padding_width = 10
            print(table)

        elif menu_type == "Add_Expense":
            show_menu = ["1.Enter date:{}".format(show[0]),"2.Enter amount spent:{}".format(show[1]),"3.Enter disciption:{}".format(show[2]),"4.Select category:{}".format(show[3])]
            table = PrettyTable(["Your response:"])
            for row in show_menu:
                table.add_row([row])
            table.align = "l"
            table._padding_width = 10
            print(table)
            print("Do you want to continue with this input?\t")
            self.addExpenseMenuChoice(show)

        elif menu_type == "monthly_expenditure":
            dates = list(show.keys())
            me = list(show.values())
            avg = [(i/30) for i in me]
            table = PrettyTable()
            table.add_column("Date",dates)
            table.add_column("Monthly_expenditure",me)
            table.add_column("Average daily spent",avg)
            table.align = "l"
            table._padding_width = 3
            print(table)
            os.system("pause")
            self.__init__()
        
        elif menu_type == "category-wise_expenditure":
            categories = list(show.keys())
            me = list(show.values())
            table = PrettyTable()
            table.add_column("Category",categories)
            table.add_column("Monthly_expenditure",me)
            table.align = "l"
            table._padding_width = 3
            print(table)
            os.system("pause")
            self.__init__()

    def addExpenseMenuChoice(self,show=None):
        '''
            This function checks if input given by user is right or not for confirmation if user want to continue with entered expenditure
            Args:
            show(data) : its a list of data to be entered in csv file if user really wants to add the expense
        '''
        choice = ''
        while not self.validation(choice,"addExpenseMenu_choice"):
            choice = input("Enter your choice here:\t").lower()
        if choice == 'y':
            self.addExpense(show)
        else:
            os.system('cls')
            self.addExpenseInput()
    
    def addExpense(self,data):
        '''
            This function adds the expenses in csv file
            Args:
            data(list) : its a list containing all the disciption of expenses which need to be added into csv file
        '''
        with open('Expense_disciption.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
        print("Expense added successfully\n")
        os.system('pause')
        print("\nWant to add another expenditure?")
        choice = ''
        while not self.validation(choice,"addExpenseMenu_choice"):
            choice = input("Enter your choice here:\t").lower()
        if choice == 'y':
            self.addExpenseInput()
        else:
            os.system('cls')
            self.__init__()

    def expenseTrackerMenuChoice(self):
        '''
        This function ask user for input of Expense Tracker Menu to perform specific part of the expense tracker
        '''
        choice = ''
        while not self.validation(choice,"menu_choice"):
            choice = input("Enter your choice here:\t")
        
        if choice == '1':
            self.addExpenseInput()
        elif choice == '2':
            self.viewMonthlySummary()
        elif choice == '3':
            self.viewCategoryWiseExpenditure()
        elif choice == '4':
            pass
    
    def addExpenseInput(self):
        '''
            This function takes input to add expenses
        '''
        date = input("Enter the data(format:yyyy-mm-dd)\t")
        amt = input("Enter amount spent:\t")
        discription = input("Enter discription about spent amount:\t")
        category = input("Enter category of thing on which amount is spent(e.g. like food,clothes etc):\t")
        data = [date,amt,discription,category]
        self.openExpenseTracker("Add_Expense",show=data)
        
    def viewMonthlySummary(self):
        '''
            This function extracts the data need to be shown for monthly summary and pass the data to another function to show the result in tabular format
        '''
        dates = []
        data = []
        total = 0
        dates_and_expenses = {}
        with open('Expense_disciption.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row["date"] in dates:
                    dates.append(row['date'])
                data.append(row)
        for date in dates:
            for dict in data:
                if dict["date"] == date:
                    total = total + float(dict["expenses"])
            dates_and_expenses[date] = total
            total = 0
        self.openExpenseTracker("monthly_expenditure",dates_and_expenses)
                
    def viewCategoryWiseExpenditure(self):
        '''
            This function extracts the data need to be shown for category wise expenditure and pass the data to another function to show the result in tabular format
        '''
        categories = []
        data = []
        total = 0
        category_and_expenses = {}
        with open('Expense_disciption.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row["category"] in categories:
                    categories.append(row['category'])
                data.append(row)
            print(categories)
        for category in categories:
            for dict in data:
                if dict["category"] == category:
                    total = total + float(dict["expenses"])
            category_and_expenses[category] = total
            total = 0
        self.openExpenseTracker("category-wise_expenditure",category_and_expenses)

    def validation(self,input,input_field):
        '''
            This function checks if input given by user is right or not
            Args:
            input_field(str) : its a string to identify the input field to check
            input(str or int) : its a input given by user
            Returns:
            it returns true else print a message
        '''
        number_validator = r'^[1-4]$'
        yn_validator = r'^[yn]$'
        if input_field == "menu_choice":
            if re.match(number_validator,input):
                return True
            else:
                print("Please fill input with valid key ---> 1,2,3,4")
        
        elif input_field == "addExpenseMenu_choice":
            if re.match(yn_validator,input):
                return True
            else:
                print("Please fill input with valid key ---> Y/N")


    

if __name__ == "__main__":
    et = ExpenseTracker()