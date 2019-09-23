import lib_bc
import json

try:
    print("[!]Getting chrome cookies...")
    chrome = lib_bc.chrome()
    print("[+]Got chrome cookies without any exceptions!")
except:
    print("[-]Had a problem while getting chrome cookies skipping chrome.")
    chrome = None

try:
    print("[!]Getting chrome firefox...")
    firefox = lib_bc.firefox()
    print("[+]Got firefox cookies without any exceptions!")
except:
    print("[-]Had a problem while getting firefox cookies skipping firefox.")
    firefox = None

try:
    print("[!]Getting safari cookies...")
    safari = lib_bc.safari()
    print("[+]Got safari cookies without any exceptions!")
except:
    print("[-]Had a problem while getting safari cookies skipping safari.")
    safari = None

print("[!]Creating dict for all cookies found...")
cookie_list = {
    "chrome": [],
    "firefox": [],
    "safari": []
}

print("[!]Creating dict for chrome browser cookies...")
if(chrome!=None) and (len(chrome)!=0):
    for cookie in chrome:
            cookie_list["chrome"].append({
                "Name": cookie.name,
                "Value": cookie.value,
                "Domain": cookie.domain,
                "Secure": str(cookie.secure),
                "ExpireTime": str(cookie.expires)
            })
    print("[+]Chrome browser cookie dict created!")
else:
    print("[-]No chrome browser cookie found, so no dict created.")

print("[!]Creating dict for firefox browser cookies...")
if(firefox!=None) and (len(firefox)!=0):
    for cookie in firefox:
            cookie_list["firefox"].append({
                "Name": cookie.name,
                "Value": cookie.value,
                "Domain": cookie.domain,
                "Secure": str(cookie.secure),
                "ExpireTime": str(cookie.expires)
            })
    print("[+]Firefox browser cookie dict created!")
else:
    print("[-]No firefox browser cookie found, so no dict created.")

print("[!]Creating dict for safari browser cookies...")
if(safari!=None) and (len(safari)!=0):
    for cookie in chrome:
            cookie_list["safari"].append({
                "Name": cookie.name,
                "Value": cookie.value,
                "Domain": cookie.domain,
                "Secure": str(cookie.secure),
                "ExpireTime": str(cookie.expires)
            })
    print("[+]Safari browser cookie dict created!")
else:
    print("[-]No safari browser cookie found, so no dict created.")

print("[!]Saving the duct in json file...")
with open('cookies.json', 'w') as f:
    f.write(json.dumps(cookie_list))
print("[+]Cookie list saved to the 'cookies.json' file!")

print("***  COOKIES ARE SAVED TO 'cookies.json' FILE    ***")
print("***  EXITING PYTHON  ***")
