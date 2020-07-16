import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkm
import selenium.webdriver as webdriver

window = tk.Tk()
window.title("채용사이트 검색")
window.geometry("260x68+850+350")
window.resizable(width=False,height=False)


values = ["사람인", "잡플래닛", "워크넷"]

combobox = ttk.Combobox(window, height=20, values=values)
combobox.grid(row=0,column=0,columnspan=2)
combobox.set("목록 선택")

lb1 = tk.Label(window, width=5, text="내용")
lb1.grid(row=1,column=0)
contents = tk.Entry(window, width=20)
contents.grid(row=1,column=1)

def findJob():
    if(contents.get() == ""):
        tkm.showwarning("공백확인","값을 입력하세요.")
    else:
        if(combobox.get() == "목록 선택"):
            tkm.showwarning("목록 선택","목록을 선택하세요.")
        else:
            driver = webdriver.Chrome("C:\\Users\\limm2\\Desktop\\python tutorial\\chromedriver.exe") 
            if(combobox.get() == "사람인"):
                driver.get("https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword={0}".format(contents.get()))
            elif(combobox.get() == "잡플래닛"):
                driver.get("https://www.jobplanet.co.kr/search?query={0}".format(contents.get()))
            else:
                driver.get("https://www.work.go.kr/wnSearch/unifSrch.do?topQuery={0}".format(contents.get()))
btn1 = tk.Button(window, text="검색", command=findJob, width=17)
btn1.grid(row=2,column=0)

def closecallBack():
    window.destroy()
btn2 = tk.Button(window, text="종료",command=closecallBack, width=17)
btn2.grid(row=2,column=1)

window.mainloop()