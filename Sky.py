import requests, bs4, webbrowser
import threading
class SkyClass(threading.Thread):
    
    def __init__(self, search):
        super(SkyClass, self).__init__()
        self.url = 'https://www.skytorrents.lol/?query=' + search
        
    def run(self):    
        self.res = requests.get(self.url)
        self.res.raise_for_status()
        self.soup = bs4.BeautifulSoup(self.res.text, features='lxml')

        self.torRow = self.soup.select('tr[class="result"]')
        self.numOfTor = len(self.torRow)

        self.torName =[]
        for i in range(self.numOfTor):
            self.torName += self.torRow[i].find('a')        

    def displayNum(self):
        print('Sky Torrents: ' + str(self.numOfTor) + ' torrents found.')

    def getElements(self):
        print('Fetching other information')
        print()
        
        # Magnet Link
        self.torMagnet = self.soup.select('img[src="/files/magnet.svg"]')

        #  Size
        self.torSky = self.soup.select('tr[class="result"] > td[class="is-hidden-touch"]')
        self.torSize =[]
        for i in range(0,len(self.torSky),3):
            self.torSize += self.torSky[i]

        # Seeders
        self.torSeeders = self.soup.select('td[style = "text-align: center;color:green;"]')

        # Leechers
        self.torLeechers = self.soup.select('td[style = "text-align: center;color:red;"]')   

    def displayTorrent(self):
        if self.numOfTor == 0:
            print('No torrents available')
        else:
            for i in range(self.numOfTor):
                print(str(i+1) + '. ' + str(self.torName[i]))
                print(str(' ' + self.torSize[i]), end='\t') 
                # print(str(self.torDate[i]), end='\t')
                print('Seeds:' + str(self.torSeeders[i].contents[0]), end=' ')
                print('Leeches:' + str(self.torLeechers[i].contents[0]))
                print()
                11
    def chooseTorrent(self):
        x = 0
        while x not in range(1,self.numOfTor):
            x = int(input('Choose your torrent:' + '[1-' +  str(self.numOfTor) + ']: '))
        # Display chosen torrent
        print()
        print('\tChosen torrent: ')
        print(self.torName[x-1])
        print(str(self.torSize[x-1]), end='\t')
        # print(str(self.torDate[x-1]), end='\t')
        print(str(self.torSeeders[x-1].contents[0]), end='\t')
        print(str(self.torLeechers[x-1].contents[0]))
        # Retrieve and open magnet link
        mag = self.torMagnet[x-1].parent.get('href')
        webbrowser.open(mag)
