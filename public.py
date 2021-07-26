#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#Code By Zalim
#Credit Tech Abm and Safraz
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

bd = random.randint(10000000.0, 90000000.0)
sim = random.randint(20000, 40000)
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(1e7, 9e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo ="""
    \033[1;92m__________      .__  .__         
    \033[1;92m\____    /____  |  | |__| _____  
    \033[1;93m /     /\__  \ |  | |  |/     \ 
    \033[1;93m/     /_ / __ \|  |_|  |  Y Y  \
    \033[1;96m/_______ (____  /____/__|__|_|  /
    \033[1;96m        \/    \/              \/ 

\033[1;92m-----------------------------------------------
\033[1;92m>> AUTHOR   :   Zalim
\033[1;92m>> FACEBOOK : RequestTimeOut408
\033[1;92m>> YOUTUBE  : Abi Banaya Nhi Jani
\033[1;92m-----------------------------------------------"""

                   
def main():
	os.system("clear")
	print(logo)
	print("")
	print(" \x1b[1;92m    \tMain menu")
	print("")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print(" \x1b[1;92m     [1] Aik press kro\n")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print("")
	os.system('xdg-open https://www.facebook.com/RequestTimeOut408')
	log_sel()
def log_sel():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		login()
	elif sel =="2":
		ran()
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;91m  \tFacebook login")
		print("")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print(" \x1b[1;91m   [1] FACEBOOK ID/PASS LOGIN\n")
		print(" \x1b[1;92m   [2] FACEBOOK TOKEN LOGIN\n")
		print("  \x1b[1;91m  [3] Back ")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print("")
		log_select()
def log_select():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\tFacebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("access_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\tAccount has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\tId/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        token = raw_input        (" Paste token here: ")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("   Welcome: "+name)
    print("")
    print("    Free mode :Actvited")
    print("")
    print("")
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print(" \x1b[1;92m[1]  CRACK AUTO PASS\n")
    print(" \x1b[1;91m[2]  CRACK CHOICE PASS\n")
    print(' \x1b[1;90m[3]   BACK')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print("")
    menu_option()
def menu_option():
	select = raw_input(" Choose option: ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
		
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")
	print("")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print("\x1b[1;92m       [1] CRACK PUBLIC ID")
	
if __name__ == '__main__':
	main()

