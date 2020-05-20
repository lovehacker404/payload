#!/usr/bin/python3 env



import os
import random
import time
import Payloads.pld_types as plds



# Cooded By : lovehacker
# Youtube   : BlackMafia



rows, columns = os.popen('stty size', 'r').read().split()
Colms =  int ((int (columns)-37) / 2)-2
c = " " * Colms

colors = ["\033[1;33m","\033[1;37m","\033[1;31m", "\033[1;34m", "\033[1;32m"]
fore = random.choice (colors)
fore1 = "\033[1;36m"
fore2 = "\033[1;35m"
os.system ("clear")



def finaly ():
	print (c+"\033[1;31m __________________________________")
	print (c+"|                                  |")
	print (c+"| \033[1;32mCooded By \033[1;34m :----->>   \033[1;34m lovehacker   \033[1;34m|")
	print (c+"| \033[1;32mYoutube   \033[1;34m :----->>   \033[1;34m BlackMafia \033[1;34m|")
	print (c+"|__________________________________|")

# colors.
blue = "\033[1;34m"
cyan = "\033[1;36m"
norml = "\033[0m"



def banner ():
	os.system ("clear")
	print (" \n ")
	print (c+fore+"                   ./ymM0dayMmy/. ")
        print (c+fore+"                   -+dHJ5aGFyZGVyIQ==+- ")
        print (c+fore+"               `:sm⏣~~Destroy.No.Data~~s:`")
        print (c+fore+"          -+h2~~Maintain.No.Persistence~~h+-")
        print (c+fore+"       `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`")
        print (c+fore+"    ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.")
        print (c+fore+"   -++SecKCoin++e.AMd`          `.-:/+hbove.913.ElsMNh+-")
        print (c+fore+"  -~/.ssh/id_rsa.Des-                `htN01UserWroteMe!-")
        print (c+fore+":dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:")
        print (c+fore+":we're.all.alike'`                     The.PFYroy.No.D7:")
        print (c+fore+":PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:")
        print (c+fore+":msf>exploit -j.                       :Ns.BOB&ALICEes7:")
        print (c+fore+":---srwxrwx:-.`                        `MS146.52.No.Per:")
        print (c+fore+":<script>.Ac816/                        sENbove3101.404:")
        print (c+fore+":NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:")
        print (c+fore+":09.14.2011.raid                       /STFU|wall.No.Pr:")
        print (c+fore+":hevnsntSurb025N.                      dNVRGOING2GIVUUP:")
        print (c+fore+":#OUTHOUSE-  -s:                       /corykennedyData:")
        print (c+fore+":$nmap -oS                              SSo.6178306Ence:")
        print (c+fore+":Awsm.da:                            /shMTl#beats3o.No.:")
        print (c+fore+":Ring0:                             `dDestRoyREXKC3ta/.:")
        print (c+fore+":23d:                               sSETEC.ASTRONOMYist:")
        print (c+fore+" /-                        /yo-    .ence.N:(){ :|: & };:")
        print (c+fore+"                           `:Shall.We.Play.A.Game?tron/")
        print (c+fore+"                           ```-ooy.if1ghtf0r+ehUser5`")
        print (c+fore+"                         ..th3.H1V3.U2VjRFNN.jMh+.`")
        print (c+fore+"                        `MjM~~WE.ARE.se~~MMjMs")
        print (c+fore+"                          +~KANSAS.CITY's~-`")
        print (c+fore+"                           J~HAKCERS~./.`")
        print (c+fore+"                            .esc:wq!:`")
        print (c+fore+"                            +;+ATH`")
        print (c+fore+"   BlackMafia WhatsApp Num")
        print (c+fore+"         03094161457")
	print (c+fore+"       \033[1;47m   \033[1;34mBlack \033[1;30m♡\033[1;35m|\033[1;34m☆\033[1;35m|\033[1;30m♡ \033[1;34mMafia   \033[1;0m     ")





# configure metasploit is installed or not.
def Check_requirments ():
	if os.path.exists ("/sdcard/Black_Mafia") == False :
		os.system ("mkdir /sdcard/Black_Mafia")

	if os.path.exists ('/data/data/com.termux/files/usr/bin/msfconsole') == True :
		print ("")
	else:
		print (blue+"--->>"+cyan+"  Checking Metasploit  ....")
		time.sleep (1)
		print (blue+"--->>"+cyan+"  Ooo No! Msfvenom isn't in your System")
		time.sleep (1)
		print (blue+"--->>"+cyan+"  Install Metasploit Correctly.")
		time.sleep (1)
		print (blue+"--->>"+cyan+"  Then try again.")
		print (" \n ")
		exit (0)


# Available options.
def chose_opt ():
	print ("\033[1;34mBlack \033[1;35m|\033[1;34m••\033[1;35m| \033[1;34mMafia\033[1;31m/~"+cyan+" Choose Your Payload\n")
	time.sleep (0.5)
	pld_list = ["Android" ,"Windows", "Linux", "Mac","Python","Bash", "Perl","Exit"]
	for pld in pld_list:
		time.sleep (0.1)
		print (cyan+"	["+blue,pld_list.index (pld)+1,cyan+"]   "+pld)
	print(" \n ")
	pld_type = int (input ("\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~  \033[1;36m"))
	if pld_type > 8:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
			time.sleep(3)
			exit (0)

	else:
		pld_to_gen = ["plds.Android ()", "plds.Windows ()", "plds.Linux()", "plds.Mac ()", "plds.Python ()", "plds.Bash ()", "plds.Perl ()", "exite ()"]
		exec (pld_to_gen[pld_type - 1])



def exite ():
	time.sleep (1.2)
	banner()
	print ("\n\n\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~"+cyan+"  God By BlackMafia Tool.\n\n")
	exit (0)


def main ():
	os.system ("termux-setup-storage")
	banner ()
	Check_requirments ()
	time.sleep (1.5)
	chose_opt ()


if __name__ == "__main__":
	try:
		main ()
	except KeyboardInterrupt:
		exite ()
	except ValueError:
		print ("\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
		time.sleep()
		exit (0)
	except EOFError:
		exite ()
