import mechanicalsoup

proxies={
    'https':'159.89.195.153:8118',
    'http':'165.227.192.42:80'
}


def proxyTest(url):
        browser = mechanicalsoup.StatefulBrowser()
        browser.session.proxies=proxies
        browser.open(url, verify=False)
        page = browser.get_current_page()
        #print(page)
        code = open("code.txt", "w")
        code.write(str(page))
        code.close()
        print("copy completed")
proxyTest('http://www.youtube.com/watch?v=21-PTzcVhWs')