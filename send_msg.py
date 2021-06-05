from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pathlib

class automation:
    def __init__(self):
        path='chromedriver.exe'
        option = webdriver.ChromeOptions()
        option.add_argument(f'--user-data-dir={pathlib.Path.home()}/AppData/Local/Google/Chrome/User Data')

        self.driver = webdriver.Chrome(executable_path=path,chrome_options= option)

    def message_sender(self,phone,message):
        time.sleep(1)
        self.driver.get(f'https://web.whatsapp.com/send?phone={phone}&text={message}&app_absent=0')
        
        try:
            invalid = WebDriverWait(self.driver,5).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div'))
            )
            invalid.click()

            return 1
        except:
            
            try:
                time.sleep(1)
                send = WebDriverWait(self.driver,10).until(
                    EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/footer/div[1]/div[3]/button'))
                )
                
                send.click()
                time.sleep(2)
                return 0
            except:
                self.driver.close() 
                return 1
                
from tkinter import *
from tkinter import messagebox

class Direct_Whatsapp(automation):
    def __init__(self):
        root = Tk()
        
        self.root = root
        self.root.geometry("500x700+20+20")
        self.root.resizable(0, 0)
        self.root.config(bg="#253133")
        self.root.title("Direct WhatsApp")
        
        self.main_frame = Frame(self.root, height="720", bg="#253133")
        self.main_frame.pack(side="left",padx=10,pady=10)

        msg_label = Label(self.main_frame,text="Message",font=("Arial",20),fg="#6a7ae6", bg="#253133")
        msg_label.pack(padx=15,pady=15,side=TOP)
        self.input_msg = Text(self.main_frame, height=5, width=50,bg="#98cfe3")
        self.input_msg.pack(padx=15,pady=15,side=TOP)

        num_label = Label(self.main_frame,text="Contacts",font=("Arial",20),fg="#6a7ae6", bg="#253133")
        num_label.pack(padx=15,pady=15,side=TOP)
        self.input_num = Text(self.main_frame, height=20, width=15,bg="#98cfe3")
        self.input_num.pack(padx=15,pady=15,side=TOP)

        send_btn = Button(self.main_frame, text="Send",bg="#98cfe3",width=10,height=2,font=("Arial",20),command=self.send_msg)
        send_btn.pack(padx=15,pady=15)

        self.root = mainloop()
        


    def send_msg(self):
        
        message = self.get_msg()
        numbers = self.get_num()
        numbers = set(numbers)

        auto = automation()
        while len(numbers) > 0:
            num = numbers.pop()
            num = "91" + num.strip()
            if len(num) is 12:
                try:
                    
                    resp = auto.message_sender(num,message)
                    if resp == 1:
                        messagebox.showerror("Failed",f"Invalid Number : {num}")  
                except Exception as e:
                    
                    auto.driver.close()
                    messagebox.showerror("Failed","Something went wrong!,\nTry Again...")
                    break
        
            else:
                messagebox.showerror("Failed",f"Invalid Number : {num}")

        auto.driver.close()
        messagebox.showinfo("Success!!!","Message has been sent to all contacts.")

    def get_msg(self):
        message = self.input_msg.get("1.0",END)
        return message

    def get_num(self):
        number_txt = self.input_num.get("1.0",END)
        number_lst = number_txt.split("\n")
        while ("\n" in number_lst):
            number_lst.remove("\n")
        while ('' in number_lst):
            number_lst.remove('')

        return number_lst

def main():
   w = Direct_Whatsapp()

if __name__== "__main__":
    main()
