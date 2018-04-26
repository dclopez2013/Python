#!usr/bin/env python

import mechanicalsoup


def viewpage(url):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)

    toCopy = input("Do you want to copy the code to a local file?")

    if(toCopy.lower() == "yes"):
        print("*" * 80)
       # page = browser.get_current_page()
        code = open("code.txt", "w")
        code.write(str(browser.download_link()))
        code.close()
        print("*" * 80)
        print("Copying code to file")
    elif (toCopy.lower() == "no"):
        page = browser.get_current_page()
        print(page)
    else:
        page = browser.get_current_page()
        print(page)


print("*" * 80)
url = input("Please enter the url of the site you wish to visit \n")
print("*" * 80)
print("Visiting URL now")

viewpage(url)
