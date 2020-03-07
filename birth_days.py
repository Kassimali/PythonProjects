import json
birth_days={'Kassim':'1 Jun',"Dahir":'29 Dec'}

while True:

    name=input('Enter name or(blank to quit) : ')
    if name=='':
        break
    if name in birth_days:
        print(birth_days[name] +' is the birthday of ' + name)
    else:
        print('We do not have birthday for ' + name )   
        birth_day=input('what is his/her birthday ') 
        birth_days[name]=birth_day

with open('birth_days.json','w') as f:
    json.dump(birth_days,f)
    print('successfully written to the file')
