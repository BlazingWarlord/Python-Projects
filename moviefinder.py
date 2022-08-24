import requests

#Horror: https://www.imdb.com/list/ls026579006/
#Action: https://www.imdb.com/list/ls027328830/
#Animation: https://www.imdb.com/list/ls027345371/
#Sci-Fi: https://www.imdb.com/list/ls021424736/
#Documentaries: https://www.imdb.com/list/ls027340130/

while True:

    menu = "Welcome To IMBD Movie List Finder\n\nEnter 0 for Horror\n\nEnter 1 for Action\n\nEnter 2 for Animation\n\nEnter 3 for Sci-Fi\n\nEnter 4 for Documentaries\n\nEnter 9 to Exit\n\n"

    inp = int(input(menu + "Enter the number: "))

    if(inp == 0):
        link = r"https://www.imdb.com/list/ls026579006/"
    if(inp == 1):
        link = r"https://www.imdb.com/list/ls027328830/"
    if(inp == 2):
        link = r"https://www.imdb.com/list/ls027345371/"
    if(inp == 3):
        link = r"https://www.imdb.com/list/ls021424736/"
    if(inp == 4):
        link = r"https://www.imdb.com/list/ls027340130/"
    if(inp == 9):
        break
    else:
        print("Invalid input, Exiting...")
        break

    url = requests.get(link).text

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(url,'lxml')

    listed = soup.find('div',{'class':'article listo'})
    a = listed.find('div',{'class':'lister list detail sub-list'})
    b1 = a.find('div',{'class':'lister-list'})
    b = b1.findAll('div',{'class':'lister-item-content'})


    for x in b:
        try:
            c = x.find('h3',{'class':'lister-item-header'})
            r = x.find('p',{'class':'text-muted text-small'})
            p = x.findAll('p',{'class':'text-muted text-small'})
            li = []
            for i in p:
                j = i.findAll('a')
                for k in j:
                    li.append(k.text)
               
            if li[0] in li:
                s = r.find('span',{'class':'certificate'})
                d = c.find('a')
                if s.text not in []:
                    print(d.text,' ',s.text)
                    for z in li:
                        print(z,end='/')
                    print('\n')
        except:
            print('')
        #d = c.get('a').text
        #print(d)


