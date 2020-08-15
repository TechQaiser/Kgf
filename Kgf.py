#!/usr/bin/python
# coding=utf-8
# Written By Tech Qaiser If You want to Get Creadit Of My Project Then See Your self again
# Source : Python2"
# Ranked : Silver lll.

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Kgf.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
##### LOGO #####
banner = """
\033[1;92m╭━━━╮
\033[1;92m┃╭━╮┃
\033[1;92m┃┃╱┃┣━━┳┳━━┳━━┳━╮
\033[1;92m┃┃╱┃┃╭╮┣┫━━┫┃━┫╭╯
\033[1;92m┃╰━╯┃╭╮┃┣━━┃┃━┫┃
\033[1;92m╰━━╮┣╯╰┻┻━━┻━━┻╯
\033[1;92m╱╱╱╰╯

\033[1;97m-----------------------------------------------

\033[1;91m╘\033[1;93mCoder   :\033[1;95mTech Qaiser
\033[1;91m╘\033[1;93mGithub  :\033[1;95mhttps://github.com/TechQaiser
\033[1;91m╘\033[1;93mFacebook:\033[1;95mQaiser Abbas
\033[1;91m╘\033[1;93mYoutube :\033[1;95mTech Qaiser
\033[1;91m╘\033[1;93mNote :\033[1;95mThis Is only For Educational Purpose
\033[1;91m╘\033[1;93mNew Update :\033[1;95m Identity Problem Fixed 100% If You Login With Acces Token

\033[1;97m-----------------------------------------------"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔]\033[1;92mLogging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

def tlogin():
	os.system('clear')
	print banner
	username = raw_input("[🔐].\033[1;96mTOOL USERNAME: ")
	if username =="Qaiser":
	    os.system('clear')
	    print banner
	    print "[✓] .\033[1;92mTOOL USERNAME: "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    time.sleep(1)
	    tlogin()
	    
	passw = raw_input("[🔐] .\033[1;96mTOOL PASSWORD: ")
	if passw =="Kgf":
	    os.system('clear')
	    print banner
	    print "[🔑] \033[1;92mTOOL USERNAME: " +username+ " (correct)"
	    print "[🔑] \033[1;92mTOOL PASSWORD: " +passw+ "  (correct)"
	    time.sleep(2)
	else:
	    print "[!] Invalid Password."
	    time.sleep(1)
	    tlogin()
	try:
		toket = open('login.txt','r')
		os.system('python2 .Kgf2.py')
	except (KeyError,IOError):
		methodlogin()
	else:
		print "\033[1;91m[!] \033[1;94mInvalid Password"
		time.sleep(1)
		tlogin()

##### Login Method #####


def methodlogin():
	os.system('clear')
	print banner
	print "\033[0;32m[-->1<--] \033[1;95mLogin With Email/Password."
	print "\033[0;32m[-->2<--] \033[1;95mLogin Using Fb Token."
	print "\033[0;32m[-->3<--] \033[1;95mExit."
	print ('      ')
	hos = raw_input("\n\033[1;96mChoose Option >>  ")
	if hos =="":
		print"\033[1;91m[!] \033[1;95mWrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print banner
		hosp = raw_input("[☪] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n\[✓]\033[1;92mLogged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
		os.system('python2 .Kgf2.py')
		
	elif hos =="0":
		exit()
	else:
		print"[!]\033[1;95mWrong Input"
		exit()
def login():
	os.system("clear")
	try:
		tb=open('login.txt', 'r')
		os.system("python2 .Kgf2.py")
	except (KeyError,IOError):
		os.system("clear")
		print (banner)
		hamza('\033[1;94mLogin Your Facebook Account')
		hamza('\033[1;94mNote : Donot Use Your Personal Account Bcoz Of Identity')
		hamza('\033[1;94m Please Sir Use a New Facebook Account To Login Safely')
		print'-------------------------------------'
		iid=raw_input('\033[1;92mNumber/Email = ')
		id=iid.replace(" ","")
		pwd=raw_input('\033[1;92m Password = ')
		tik()
		data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("login.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print "\n[✓]\033[1;92mLogged In Successfully."
		    time.sleep(1)
		    os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
		    os.system("clear")
		    os.system("python2 .Kgf2.py")
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('\033[1;92m User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('\033[1;92mEmail / Password Is Wrong ')
		        time.sleep(1)
		        login()
if __name__=='__main__':
    tlogin()
