from dotenv import load_dotenv
import os
load_dotenv()
user = os.getenv("ROOT_USER")
password = os.getenv("ROOT_PASSWORD")

def login_page(self):
    self.goto("https://automation-workshop.hacksoft.io/admin/login/?next=/admin/")
    
def user_name_pass(self):
    self.locator("#id_username").fill(user)
    self.locator("#id_password").fill(password)
    
def login_button_click(self):
    self.locator(".submit-row > input:nth-child(1)").click() # login_button.click()
    
def login_success(self):
    login_page(self)
    user_name_pass(self)
    login_button_click(self)
    
def user_add(self):
    self.locator(".model-guest > td:nth-child(2) > a:nth-child(1)").click() # add_user_button
    self.locator("#id_first_name").fill("Kaloyan")
    self.locator("#id_last_name").fill("Tsonyovski")
    self.locator("#id_email").fill("ktsonyovski@outlook.com")
    self.locator("#id_phone").fill("1234")
    self.locator(".default").click() # save_button
    
    
def delete_all_users(self):
    self.locator(".model-guest > td:nth-child(3) > a:nth-child(1)").click() # change_button
    self.locator(".actions > label:nth-child(1) > select:nth-child(1)").select_option(label="Delete selected guests") # dropdown_menu
    self.locator("#action-toggle").click() # select_all_button
    self.locator(".button").click() # go_button
    self.locator("input[type='submit']").click() # confirm_button

