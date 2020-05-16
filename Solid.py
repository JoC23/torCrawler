import requests, bs4, webbrowser
import threading
class SolidClass(threading.Thread):
    
    def __init__(self, search):
        super(SolidClass, self).__init__()
        self.url = 'https://solidtorrents.net/search?q=' + search
        
    def run(self):    
        self.res = requests.get(self.url)
        self.res.raise_for_status()
        self.soup = bs4.BeautifulSoup(self.res.text, features='lxml')
        self.torName = self.soup.select('h3[class = "subtitle-2 text-truncate"] span')
        self.numOfTor = len(self.torName)

    def displayNum(self):
        print('Solid Torrents: ' + str(self.numOfTor) + ' torrents found.')

    def getElements(self):
        print('Fetching other information')
        print()
        # Magnet Link
        self.torMagnet = self.soup.select('div[class = "v-list-item__action"] a')
        
        # Size
        self.torSize = self.soup.select('.v-list-item__title strong')

        # Date Created 
        # self.torDate = self.soup.select('td[title]')

        # Seeders
        self.torSeeders = self.soup.select('span[class = "green--text darken-4 font-weight-bold"]')

        # Leechers
        self.torLeechers = self.soup.select('span[class = "red--text darken-4 font-weight-bold"]')

    def displayTorrent(self):
        if self.numOfTor == 0:
            print('No torrents available')
        else:
            for i in range(self.numOfTor):
                print(str(i+1) + '. ' + str(self.torName[i].contents[0]))
                print(' ' + str(self.torSize[i].contents[0]), end='\t') 
                # print(str(torDate[i].contents[0]), end='\t')
                print('Seeds:' + str(self.torSeeders[i].contents[1]), end=' ')
                print('Leeches:' + str(self.torLeechers[i].contents[1]))


    def chooseTorrent(self):
        x = 0
        while x not in range(1,self.numOfTor):
            x = int(input('Choose your torrent:' + '[1-' +  str(self.numOfTor) + ']: '))
        # Display chosen torrent
        print()
        print('\tChosen torrent: ')
        print(self.torName[x-1].contents[0])
        print(str(self.torSize[x-1].contents[0]))
        # print(str(torDate[x-1].contents[0]))
        # Retrieve and open magnet link
        mag = self.torMagnet[x-1].get('href')
        # print(mag)
        webbrowser.open(mag)