import re

phone_formt=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo=phone_formt.search('My Phone number is 252-618-952391')

check_result=mo.group()
if check_result!=None:
    print('Valid Phone Number')
else:
    print('invalid phone number')    
