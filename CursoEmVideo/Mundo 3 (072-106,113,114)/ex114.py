import urllib
import urllib.request as url

try:
    site = url.urlopen('http://www.pudim.com.br')
except:
    print('O site pudim não está acessível no momento.')
else:
    print('O site pudim foi acessado corretamente.')