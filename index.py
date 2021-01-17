from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw,choice):
        self.driver = webdriver.Chrome()
        self.username = username
        self.choice = choice
        self.driver.get("https://instagram.com")
        sleep(2)

        if choice == 1:
            self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(4)
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                    .click()
                sleep(5)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                    .click()
                sleep(5)
                self.get_unfollowers()
            except:
                print("You entered invalid details..")
        else:
           self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]')\
               .click()
           self.driver.find_element_by_xpath('//*[@id="email"]')\
               .send_keys(username)
           self.driver.find_element_by_xpath('//*[@id="pass"]')\
               .send_keys(pw)
           self.driver.find_element_by_xpath('//*[@id="loginbutton"]')\
               .click()
           sleep(4)
           try:
              sleep(10)
              self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                  .click()
              sleep(5)
              self.get_unfollowers()
           except:
               print("You entered invalid details..")
        
    def get_unfollowers(self):
        if self.choice == 1:
            self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
                .click()
        else:
            self.driver.find_element_by_class_name("gmFkV")\
                .click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print()
        print("****************UNFOLLOWERS*****************")
        for i in not_following_back:
            print(i)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

print("How would you like to login?")
print("Please press 1 for login via instagram")
print("Please press 2 for login via facebook")

choice = int(input())

user_name = input("Enter your username :: ")
password = input("Enter your password :: ")
my_bot = InstaBot(user_name,password,choice)
