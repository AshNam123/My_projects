import  sys,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date,datetime


#today = date.today().strftime('%d/%m/%Y')
#current_time = datetime.now().strftime("%H/%M/%S")

#msgDate = '24/5/2021'
#msgTime = '2:30'

msg = "I love you"

def new_chat(username):
    new_chat = chrome.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
    new_chat.send_keys(username)
    time.sleep(2)

    try:
        user = chrome.find_element_by_xpath('//span[@title="{}"]'.format(username))
        user.click()
    except NoSuchElementException as se:
        print("Username not in contact list")
    except Exception as e:
        chrome.close()
        print(e)
        sys.exit()




if __name__ == '__main__':
            #if msgDate == today:
             #   current_time = datetime.now().strftime("%H/%M/%S")
              #  if current_time >= msgTime:

                        options = webdriver.ChromeOptions()
                        options.add_argument(r'--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default')
                        options.add_argument('--profile-directory=Default')
                        chrome = webdriver.Chrome(executable_path=r'C:\projects(python)\whatsappautomation\chromedriver_win32\chromedriver.exe', options=options)
                        chrome.get('https://web.whatsapp.com/')
                        time.sleep(5)
                        #user_name_list = ['M']
                        user_name_list = ['Irshaad','Komal','M','Mahesh','Militry','N','Namrata Mam','Nihal','Nisha','Nithin','Onant','Prince Ka Mausi Ka Beta','Preeti Mam','Robin','Rohit Mohan','Romeobaaz','Rutuja','Sam','Sarvesh','Smitha Mam','Shija Aunty','Shubham Pawar','Shubham Yadav','Sunita','Sayali','Swetha','Tejas','Vimlesh','Vishnu','Vkas','Yash']
                        for username in user_name_list:
                            try:
                                user = chrome.find_element_by_xpath('//span[@title="{}"]'.format(username))
                                user.click()
                            except NoSuchElementException as se:
                                new_chat(username)
                                time.sleep(2)
                            time.sleep(2)
                            message_box = chrome.find_element_by_xpath('//div[@class="_2A8P4"]')
                            time.sleep(2)

                            message_box.send_keys(msg)
                            time.sleep(1)

                            message_box  = chrome.find_element_by_xpath('//button[@class="_1E0Oz"]')
                            message_box.click()
                            time.sleep(2)
                        chrome.close()
                        sys.exit()
               # today = date.today().strftime('%d/%m/%Y')
                #time.sleep(5)