from time import sleep

def login_page(self):
    self.goto("https://automation-workshop.hacksoft.io/admin/login/?next=/admin/")
    

def user_name_pass(self):
    user_name = self.locator("#id_username")
    user_name.fill("bassline1911@mail.com")
    
    user_pass = self.locator("#id_password")
    user_pass.fill("qaworkshop")
    
def login_button_click(self):
    login_button = self.locator(".submit-row > input:nth-child(1)")
    login_button.click()
    
def login_success(self):
    login_page(self)
    user_name_pass(self)
    login_button_click(self)
    
def user_add(self):
    add_user_button = self.locator(".model-guest > td:nth-child(2) > a:nth-child(1)")
    add_user_button.click()
    
    first_name = self.locator("#id_first_name")
    first_name.fill("Kaloyan")
    
    last_name = self.locator("#id_last_name")
    last_name.fill("Tsonyovski")
    
    mail = self.locator("#id_email")
    mail.fill("ktsonyovski@outlook.com")
    
    phone = self.locator("#id_phone")
    phone.fill("1234")
    
    save_button = self.locator(".default")
    save_button.click()
    
    
def delete_all_users(self):
    change_button = self.locator(".model-guest > td:nth-child(3) > a:nth-child(1)")
    change_button.click()
    
    self.locator(".actions > label:nth-child(1) > select:nth-child(1)").select_option(label="Delete selected guests")
    
    select_all = self.locator("#action-toggle")
    select_all.click()
    
    go_button = self.locator(".button")
    go_button.click()
    
    sleep(1)
    confirm_button = self.locator("input[type='submit']")
    confirm_button.click()

