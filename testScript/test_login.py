

from pageObject.LoginPage import HRMLoginPage

def test_start():
    assert HRMLoginPage().start() == True
    print('SUCESS: Automation started!!')

def test_login():
    assert HRMLoginPage().login() == True
    print("SUCCESS: Logged In!")

def test_shutdown():
    assert HRMLoginPage().shutdown() == None
    print("SUCCEESS: Automation completed!!")