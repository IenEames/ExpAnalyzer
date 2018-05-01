import sqlite3

# Connecting to existing database "EADatabase.db" which contains two tables: Categories and Expenses

condb = sqlite3.connect("EADatabase.db")
c = condb.cursor()


def addcategory():

    # Adding a new Category

    print("\nPlease enter information about new category: ")
    newcategory = input("Name for a new expense category: ")
    description = input("Shirt description for a new category: ")
    c.execute("INSERT INTO Categories (Category, Category_description) VALUES (?, ?)", (newcategory, description))
    condb.commit()
    print("New category added!")
    print("{} : {}".format(newcategory, description))


def showcategories():

    # Displaying existing categories and their ID's.

    print("\nAvailable expense categories:\n")
    for row in c.execute("SELECT Id, Category, Category_description FROM Categories"):
        category_id, category, description = row
        print("{}) {} : {}".format(category_id, category, description))


def addexpense():

    # Adding a new expense to some with defined date, category and description.

    date = input("\nExpense date in YYYY-MM-DD format: ")
    catname = input("Expense category: ")
    c.execute("SELECT Id FROM Categories WHERE Category = ? LIMIT 1", (catname,))
    category_id = c.fetchone()[0]
    amount = input("Amount spent: ")
    description = input("Expense description(optional): ")
    c.execute("INSERT INTO Expenses (Date, Category_id, Amount, Description) VALUES (?,?,?,?)",
              (date, category_id, amount, description))
    condb.commit()


def showexpenses():

    # Displaying expenses currently existing in the database

    print("\nExpense database currently contains the following records:\n")
    print(" ID | EXPENSE DATE | EXPENSE CATEGORY | AMOUNT SPENT | DESCRIPTION")
    for row in c.execute("SELECT Expense_id, Date, Categories.Category, Amount, Description "
                         "FROM Expenses JOIN Categories ON Category_id = Categories.Id"):
        expid, date, category, amount, description = row
        print("{:3} | {:12} | {:16} | {:12} | {:11}".format(expid, date, category, amount, description))


def removeexpense():

    # Removing the expense record from database based on expense ID.
    remexp = (input("\nPlease enter the ID of the expense record that you would like to remove: "))
    c.execute("DELETE FROM Expenses WHERE Expense_id=?", (remexp,))
    condb.commit()
    print("Record with ID{} has been removed from the database.".format(remexp))


def removecategory():

    # Removing the category from database based on category name.

    remcat = (input("\nPlease enter the name of the category that you would like to remove: "))
    c.execute("DELETE FROM Categories WHERE Category=?", (remcat,))
    condb.commit()
    print("'{}' category has been removed from database.".format(remcat))

addexpense()
showexpenses()
showcategories()
