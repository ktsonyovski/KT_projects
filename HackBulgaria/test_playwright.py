from resources import *

def test_login_success(page):
    login_success(page)
    expect(page).to_have_url("https://automation-workshop.hacksoft.io/admin/")

def test_add_user_success(page):
    login_success(page)
    user_add(page)
    
def test_delete_all_users_success(page):
    login_success(page)
    delete_all_users(page)