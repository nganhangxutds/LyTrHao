import requests,os
class GETPRX():
    def proxy(self,luachon,namesave):
        if luachon == '1':
            open(namesave,'a+',encoding='utf-8').write(requests.get('https://proxy-daily.com/').text.split('Free Http/Https Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><br><div class="centeredProxyList">Free Socks4 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[0].replace(' ','')+requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text.replace(' ','').replace('\n',''))
        elif luachon == '2':
            open(namesave,'a+',encoding='utf-8').write(requests.get('https://proxy-daily.com/').text.split('</div><br><br><div class="centeredProxyList">Free Socks4 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><br><div class="centeredProxyList">Free Socks5 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[0].replace(' ','')+requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text.replace(' ','').replace('\n',''))
        elif luachon == '3':
            open(namesave,'a+',encoding='utf-8').write(requests.get('https://proxy-daily.com/').text.split('</div><br><br><div class="centeredProxyList">Free Socks5 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"')[0].replace(' ','')+requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text.replace(' ','').replace('\n',''))
        a = open(namesave,'r').readlines()
        print(f'GET {len(a)} PROXY')
print('[1] HTTP/HTTPS')
print('[2] SOCKS4')
print('[3] SOCKS5')
luachon = input('SELECT: ')
namesave = input('NAME FILE SAVE(example: proxy.txt): ')
GETPRX().proxy(luachon,namesave)