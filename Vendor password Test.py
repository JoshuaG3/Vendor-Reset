from tkinter import *
from tkinter import ttk
import time
import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options

root = Tk()
root.title("Vendor Password Reset Tool")


def resetfunc():
    options = Options()
    options.add_argument('--headless=new')
    
    Email = email_input.get()

    #copies to clipboard email response.
    pc.copy("Hello, \n  I have reset your security ID. You should receive an email shortly with a temporary password. This will allow you to log in with your email address. Remember, use your \n temporary password as your old password, when creating your new password. This is time sensitive.\n \n Note: passwords must be 8 characters and contain upper and lowercase letters, a number and at least one special character like a @#$ or %.\n \n Common problem resolution: \n •	Do not click on the “I accept” button, that feature is in a Beta test with only a few vendors having access to it. \n •	What browser are you using?  - we have noticed that users that are using Internet Explorer versions 8 or 9 have had issues, but versions 10 and 11 seem to be ok.  In  \n addition, Firefox also seems to be ok. \n •	Have you tried clearing your browser’s cache/history? \n •	You should be using the password from the email that setup your account as your “Old” password, not the password that you used to use on the old portal. \n •	Make sure the caps lock is not on.")

    #Location of Chromedriver.exe file
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH, chrome_options=options)

    #Goes to the supplier portal page and will throw an exception if the page does not load in time
    try:
        driver.set_page_load_timeout(3)
        driver.get("http://supplierportal/SitePages/SupplierAdmin.aspx")
    except TimeoutException as ex:
        pass
        isrunning = 0
        print("Exception has been thrown. " + str(ex))
        error_message.set("Website Error")
        driver.close()    

    #Clicks on the search bar and enters the Email that was entered in the Label, will throw an error if it can not locate the search bar
    try:
        input_bar = driver.find_element("xpath", '/html/body/form/div[8]/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/input[1]')
        input_bar.click
        input_bar.send_keys(Email)
    except NoSuchElementException:
        print("Issue finding search bar") 
        error_message.set("Website/Code Error")
        driver.close()
        pass

    #Clicks on the Search Vendor button, will throw an error if it can not locate the button
    try:
        search_button = driver.find_element("xpath", '/html/body/form/div[8]/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/input[2]')
        search_button.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Issue finding search button")
        error_message.set("Website/Code Error")
        driver.close()
        pass

    #Clicks on the reset password button, if it cannot find the button the email was not entered correctly
    try:
        reset_password = driver.find_element("xpath", '/html/body/form/div[8]/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div[4]/input[2]')
        reset_password.click()
    except NoSuchElementException:
        print("Incorrect email format")
        error_message.set("Incorrect Email Format")
        driver.close()
        pass

    #Clicks the Alert asking to confirm resetting the password, will throw an error saying vendor not found if it cannot locate this alert popup
    try:
        Alert(driver).accept()
        time.sleep(5)
        print("Password Reset")
        error_message.set("Password has been reset and response has been copied")
    except NoAlertPresentException:
        print("Vendor Not Found")
        error_message.set("Vendor Not Found")
        driver.close()
        pass

    driver.close()

    

#function to clear text box and alert box
def stop():
    email_input.delete(0, END)
    error_message.set("")

#setting variable for the error message in the function
error_message = StringVar()
error_message.set("")
label2 = Label(root, textvariable=error_message)

#creating the parts of the GUI
label1 = Label(root, text="Enter Email:")
email_input = Entry(root, width=50, borderwidth=5)
submit_button = Button(root, text="Reset Password", command=resetfunc)
reset_button = Button(root, text="Clear", command=stop)

#Placing the different elements onto the GUI
label1.grid(row=0, column=0, padx=25, pady=5, columnspan=2)
email_input.grid(row=1, column=0, padx=25, pady=30, columnspan=2)

submit_button.grid(row=2, column=0,padx=0, pady=20)
reset_button.grid(row=2, column=1, pady=20)

label2.grid(row=3, column=0, padx=15, pady=5, columnspan=2)


root.mainloop()

