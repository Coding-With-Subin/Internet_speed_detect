import urllib.request

try:
    urllib.request.urlopen("https://www.google.com")
    print("Website is reachable")
except:
    print("Website is not reachable")
