import sys
from mechanize import Browser
import sys
from bs4 import BeautifulSoup

def main(a1,a2):
	data = []
	b=Browser()
	for rn in range(a1,a2+1):

		b.open("http://cbseresults.nic.in/class12/cbse122014_total.htm")
		b.select_form("FrontPage_Form1")
		b["regno"]=str(rn)
		resp=b.submit()
		cont=resp.read()
		soup=BeautifulSoup(cont)
		soup.prettify("utf-8")
		cont=soup.get_text()
		cont=cont[cont.index("Roll"):cont.index("Check")]
		cont=cont.encode("UTF-8").strip() 

		data.append(cont)
	return data

if __name__ == "__main__":
	arglen = len(sys.argv)
	if arglen < 3 or arglen > 4:
		print "error : usage scrape-cbse [from-roll-nos] [to-roll-nos] [outfile(optional)]"
	else :
		a1 = int(sys.argv[1])
		a2 = int(sys.argv[2])
		data =  main(a1,a2)
		if arglen == 4 : 
			outfile =  sys.argv[3]
			with open(outfile,'w') as f:
				f.write('\n ----------------------------------------- \n'.join(data))
		elif arglen == 3:
			print '\n ----------------------------------------- \n'.join(data)
			
		
		
