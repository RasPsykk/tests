import requests
import re
from bs4 import BeautifulSoup


url = 'https://pass.canal-plus.com/form/authentication_sms_activation?bundle=site&ssoconf=auth_mini_actsms_myc&popin=true&pass_target=https%3A%2F%2Fwww.mycanal.fr%2F&urlSource=https%3A%2F%2Fwww.mycanal.fr%2F&pass_modal=false&socialLinksDisabled=true&omnitureChannel=Usage&distributorId=D22024'
user = ''
mdp = ''
infos = {
    'error': '',
    'submit': 'submit',
    'socialAction': 'authentication',
    'ssoEmail': user,
    'ssoPass': mdp,
    '__checkbox_ssoMem': 'true',
    'submitButton': 'Valider'
}
r = requests.session()

print('Send auth')
r = requests.post(url, data=infos)
print(r.cookies)

print('Retrieve redirect url')
redirect_url = re.search(r"redirection\('(.+)'\)", r.text).group(1)

print('Go to redirect page')
r = requests.get(redirect_url)

print('Retrieve url homepage')
redirect_url = re.search(r"window.location.href='(.+)';", r.text).group(1)

print('Go to homepage')
r = requests.get(redirect_url)

with open('homepage.html', 'wb') as f:
    f.write(r.text.encode('utf-8'))
