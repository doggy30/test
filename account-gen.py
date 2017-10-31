import requests, time, random, string
from random import *
from faker import Faker

fake = Faker()

print ((time.strftime("%H:%M:%S") + " - Adidas account creator"))

time.sleep(2)

first_name = fake.first_name()
last_name = fake.last_name()
allchar = string.ascii_letters + string.digits
password = "".join(choice(allchar) for x in range(randint(8, 12)))
times = int(input(((time.strftime("%H:%M:%S")

def create_account():

	emails = [x.rstrip() for x in open(configs['emails_file']).readlines()]

    base_url = "https://shop.miteam.adidas.co.uk/miadidas-miteam/Login.action"

    s = requests.session()

    params = {
        "registerUser": "",
        "sourcePath": "",
        "recipeIdent": "",
        "orderId": "",
        "minAge": "14",
        "userVO.userAuthentication.regFirstName": first_name,
        "userVO.userAuthentication.regLastName": last_name,
        "userVO.userAuthentication.regLogin": email,
        "userVO.userAuthentication.regPassword": password,
        "userVO.userAuthentication.confrmPassword": password,
        "userVO.dateVO.day": '%d'   % (random.randint(1, 28))
        "userVO.dateVO.month": '%d'   % (random.randint(1, 12))
        "userVO.dateVO.year": '19%d' % (random.randint(80, 95))
        "agree": "true",
        "_sourcePage": "Q_zM-69uzSnv_J5IuzfaPzCh8EB353v6Dyn4g6K-ZaE=",
        "__fp": "cwbm4kzjY63tX0vBwkvCEZJLK9EzG94c0gJWx_ZSn7KmRJxEPupQ7btb9qEXch6S7V9LwcJLwhFmRiJ-SrR4x1OD6-LbZO5dzB5dlMOuFKLKYpT2bTd5fGOQ9fAgsISr"
    }

    res = s.post(base_url, params=params)

    if "e-mail address already exists" in res.text:
        print(((time.strftime("%H:%M:%S") + ' - This email "' + email + '" is a duplicate!')))
    else:
        print(((time.strftime("%H:%M:%S") + " - Successfully adidas created account with " + email)))
		output_handle.write('{}:{}\n'.format(email, password))
		output_handle.flush()

for i in range (times):
    create_account()
