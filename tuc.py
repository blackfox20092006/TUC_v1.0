from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import threading
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from colorama import init, AnsiToWin32
from colorama import Fore, Back, Style
import datetime
from time import sleep
import sys
banner = '''                                              
TTTTTTTTTTTTTTTTTTTTTTTUUUUUUUU     UUUUUUUU       CCCCCCCCCCCCC
T:::::::::::::::::::::TU::::::U     U::::::U    CCC::::::::::::C
T:::::::::::::::::::::TU::::::U     U::::::U  CC:::::::::::::::C
T:::::TT:::::::TT:::::TUU:::::U     U:::::UU C:::::CCCCCCCC::::C
TTTTTT  T:::::T  TTTTTT U:::::U     U:::::U C:::::C       CCCCCC
        T:::::T         U:::::D     D:::::UC:::::C              
        T:::::T         U:::::D     D:::::UC:::::C              
        T:::::T         U:::::D     D:::::UC:::::C              
        T:::::T         U:::::D     D:::::UC:::::C              
        T:::::T         U:::::D     D:::::UC:::::C              
        T:::::T         U:::::D     D:::::UC:::::C              
        T:::::T         U::::::U   U::::::U C:::::C       CCCCCC
      TT:::::::TT       U:::::::UUU:::::::U  C:::::CCCCCCCC::::C
      T:::::::::T        UU:::::::::::::UU    CC:::::::::::::::C
      T:::::::::T          UU:::::::::UU        CCC::::::::::::C
      TTTTTTTTTTT            UUUUUUUUU             CCCCCCCCCCCCC
                                        Tiktok Username Checker by Quang Nhan v1.0
'''
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
f = open('tiktokid.txt', 'r')
f2 = open('live.txt', 'w')
f3 = open('die.txt', 'w')
print(Fore.MAGENTA + banner, file=stream)
print(Fore.WHITE, 'Check live username Tiktok. Input list of usernames in file tiktokid.txt in the same directory.', file = stream)
print(Fore.WHITE, 'Live accounts will be written to live.txt and the banned accounts will be written to die.txt.', file = stream)
data = f.readlines()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_rect(400, 10, 400, 600)
t = True
for i in data:
    if t == True:
        sleep(10)
        t = False
    else:
        pass
    i.replace('\n', '')
    url = 'https://tiktok.com/@'+i
    driver.get(url)
    WebDriverWait(driver, timeout = 2)
    try:
        e = driver.find_element(By.CSS_SELECTOR, "#app > div.tiktok-ywuvyb-DivBodyContainer.e1irlpdw0 > div.tiktok-w4ewjk-DivShareLayoutV2.elmjn4l0 > div > div.tiktok-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.elmjn4l2 > div.tiktok-1gk89rh-DivShareInfo.ekmpd5l2 > div.tiktok-1hdrv89-DivShareTitleContainer.ekmpd5l3 > div > div > button").click()
        now = datetime.datetime.now()
        print(Fore.BLUE + '[',now.strftime("%Y-%m-%d %H:%M:%S"),'] ', file=stream, end = '')
        print(Fore.GREEN + '[LIVE] -> ', file=stream, end = '')
        print(Fore.YELLOW + i, file=stream)
        f2.write(i)
    except:
        now = datetime.datetime.now()
        print(Fore.BLUE + '[',now.strftime("%Y-%m-%d %H:%M:%S"),'] ', file=stream, end = '')
        s1 = '[DIE]  -> '+ i
        print(Fore.RED + s1, file = stream)
        f3.write(i)
    sleep(10)
now = datetime.datetime.now()
print(Fore.BLUE + '[', now.strftime("%Y-%m-%d %H:%M:%S"), '] Done !', file=stream, end='')
f.close()
f2.close()
f3.close()
driver.close()