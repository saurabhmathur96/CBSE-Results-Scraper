"""scrape-cbse.py : gets the cbse results by scraping the website

"""

from sys import stdout
from mechanize import Browser
from bs4 import BeautifulSoup
from argparse import ArgumentParser

USAGE = 'usage : python scrape-cbse.py \
        [from-roll-num] \
        [to-roll-num(optional)] \
        [outfile(optional)]'
URL = 'http://cbseresults.nic.in/class12/cbse122014_total.htm'
FORM = 'FrontPage_Form1'
REG_NO = 'regno'

def parse_content(html):
    """ returns result text from html """
    soup = BeautifulSoup(html)
    text = soup.get_text()
    begin = text.index('Roll')
    end = text.index('Check')
    return text[begin:end].encode('UTF-8').strip()

def main(reg_num):
    """ main function """
    browser = Browser()
    browser.open(URL)
    browser.select_form(FORM)
    browser[REG_NO] = str(reg_num)
    response = browser.submit()
    content = response.read()
    return parse_content(content)


if __name__ == '__main__':
    parser = ArgumentParser(
        description='gets the cbse results by scraping the website'
        )
    parser.add_argument('from_roll_number', type=int)
    parser.add_argument('to_roll_number', type=int)
    parser.add_argument('--outfile', type=str, 
                        help='save output to a file')
    args = parser.parse_args()
    results = [main(num) for num in range(args.from_roll_number, args.to_roll_number)]
    outfile = open(args.outfile, 'w') if args.outfile else stdout
    for result in results:
        print >> outfile, result
            
