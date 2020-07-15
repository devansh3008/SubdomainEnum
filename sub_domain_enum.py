import pyfiglet
result = pyfiglet.figlet_format("SubdomainEnum By Devansh Bordia") 
print(result) 
import requests
import optparse
parser=optparse.OptionParser()
parser.add_option("-d","--domain",dest="domain",help="Enter the domain:")
parser.add_option("-w","--wordlist",dest="wordlist",help="Enter the wordlist")
options,arguments=parser.parse_args()

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL: #this error otherwise crashes it
        pass
    except KeyboardInterrupt:
     print("Exiting the Program")
     exit()

target_url=str(options.domain)
target_wordlist=list=str(options.wordlist)
with open(target_wordlist,'r') as wordfile:
    for line in wordfile:
        word = line.strip()
        test_url = word + '.' + target_url
        response = request(test_url)
        if response:
         if target_wordlist and target_url:
          print(test_url + '   ' + str(response))
