from resources import *
from playwright.sync_api import Page, expect

def test_login_success(page):
    login_success(page)

def test_add_user_success(page):
    login_success(page)
    user_add(page)
    
def test_delete_all_users_success(page):
    login_success(page)
    delete_all_users(page)