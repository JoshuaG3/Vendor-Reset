from tkinter import *
from tkinter import ttk
import time
import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

root = Tk()
root.title("Vendor Password Reset Tool")

Exception_1 = "Website Error (unable to find search bar)"
Exception_2 = "Website Error (unable to find 'check supplier' button)"
Exception_3 = "Vendor Not Found"

def resetfunc():
    
    Email = email_input.get()

    pc.copy("Hello, \n  I have reset your security ID. You should receive an email shortly with a temporary password. This will allow you to log in with your email address. Remember, use your \n temporary password as your old password, when creating your new password. This is time sensitive.\n Note: passwords must be 8 characters and contain upper and lowercase letters, a number and at least one special character like a @#$ or %. \n Common problem resolution: \n •	Do not click on the “I accept” button, that feature is in a Beta test with only a few vendors having access to it. \n •	What browser are you using?  - we have noticed that users that are using Internet Explorer versions 8 or 9 have had issues, but versions 10 and 11 seem to be ok.  In  \n addition, Firefox also seems to be ok. \n •	Have you tried clearing your browser’s cache/history? \n •	You should be using the password from the email that setup your account as your “Old” password, not the password that you used to use on the old portal. \n •	Make sure the caps lock is not on.")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("http://supplierportal/SitePages/SupplierAdmin.aspx")

    
    try:
        input_bar = driver.find_element("xpath", '/html/body/form/div[8]/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/input[1]')
        input_bar.click
        input_bar.send_keys(Email)
    except NoSuchElementException:
        Label2 = Label(root, text=Exception_1)
        Label2.grid(row=2, column=0, padx=25, pady=5, columnspan=2)
        time.sleep(2)
        driver.close()
         
    try:
        search_button = driver.find_element("xpath", '/html/body/form/div[8]/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/input[2]')
        search_button.click()
    except NoSuchElementException:
        Label2 = Label(root, text=Exception_2)
        Label2.grid(row=2, column=0, padx=25, pady=5, columnspan=2)
        time.sleep(2)
        driver.close()
        

    time.sleep(2)

    try:
        reset_password = driver.find_element("xpath", '/html/body/form/div[8]/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div[4]/input[2]')
        reset_password.click()
    except NoSuchElementException:
        Label2 = Label(root, text=Exception_3)
        Label2.grid(row=2, column=0, padx=25, pady=5, columnspan=2)
        time.sleep(2)
        driver.close()


    #Un-comment out for full test
    #Alert(driver).accept()
    time.sleep(5)



    driver.close()

    return Label2

#function to clear text box and progress bar
def stop():
    email_input.delete(0, END)




label1 = Label(root, text="Email:")
email_input = Entry(root, width=50, borderwidth=5)

submit_button = Button(root, text="Reset Password", command=resetfunc)
reset_button = Button(root, text="Clear", command=stop)

progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')

label1.grid(row=0, column=0, padx=25, pady=5, columnspan=2)
email_input.grid(row=1, column=0, padx=25, pady=30, columnspan=2)

submit_button.grid(row=3, column=0,padx=0, pady=20)
reset_button.grid(row=3, column=1, pady=20)



root.mainloop()

