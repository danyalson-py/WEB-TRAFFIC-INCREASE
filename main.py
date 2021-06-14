import requests
import time
import sys
from torrequest import TorRequest

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}
print('''
 __     __  _                       ____            _   मैं आप कई किसी गलत काम में हिस्सा नहीं रखता!
 \ \   / / (_)   ___  __      __   | __ )    ___   | |_ 
  \ \ / /  | |  / _ \ \ \ /\ / /   |  _ \   / _ \  | __|
   \ V /   | | |  __/  \ V  V /    | |_) | | (_) | | |_ 
    \_/    |_|  \___|   \_/\_/     |____/   \___/   \__|
                                                        Aitzaz Imtiaz, यह काम मिट license शुदा है ''')
proxyPort=9050
ctrlPort=9051
site = raw_input("Enter your Blog Address : ")
blog = input("Enter The number of Viewers : ")


def run():
     response = tr.get(site, headers=headers,verify=False)
#     time.sleep(10)
#     print(response.text)  
     print "["+str(i)+"]" + " Blog View Added With IP:" +  tr.get('http://ipecho.net/plain').content
     tr.reset_identity()
  


if __name__ == '__main__':
	if len(sys.argv) > 3:
	   if sys.argv[1] and sys.argv[2]:
		proxyPort=sys.argv[1]
		ctrlPort=sys.argv[2]	
	with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	    for i in range(blog):
		  run()
print ("ह्यूज शुक्रिया! Aitzaz Imtiaz की तरफ साई धन्यवाद!"
