import requests, bs4, webbrowser
import threading

class ExtraClass(threading.Thread):
    
    def __init__(self, search):
        super(ExtraClass, self).__init__()
        self.url = 'https://extratorrent.si/search/?search=' + search
        
    def run(self):    
        self.res = requests.get(self.url)
        self.res.raise_for_status()
        self.soup = bs4.BeautifulSoup(self.res.text, features='lxml')
        self.torName = self.soup.select('.tli > a')
        self.numOfTor = len(self.torName)

    def displayNum(self):
        print('Extra Torrents: ' + str(self.numOfTor) + ' torrents found.')

    def getElements(self):
        print('Fetching other information')
        print()
        
        # Magnet Link
        self.torMagnet = self.soup.select('a[title= "Magnet link"]')

        #  Date and Size
        self.torRow = self.soup.select('.tli')
        self.torDate = []
        self.torSize = []
        for i in range(self.numOfTor):
            self.torDate += self.torRow[i].next_sibling.next_sibling
            self.torSize += self.torRow[i].next_sibling.next_sibling.next_sibling.next_sibling

        # Seeders
        self.torSeeders = self.soup.select('.sn')

        # Leechers
        self.torLeechers = self.soup.select('.ln')    

    def displayTorrent(self):
        if self.numOfTor == 0:
            print('No torrents available')
        else:
            for i in range(self.numOfTor):
                print(str(i+1) + '. ' + str(self.torName[i].contents[0]))
                print(str(' ' + self.torSize[i]), end='\t') 
                print(str(self.torDate[i]), end='\t')
                print('Seeds:' + str(self.torSeeders[i].contents[0]), end=' ')
                print('Leeches:' + str(self.torLeechers[i].contents[0]))
                # print(str(torMagnet[i].get('href')))

    def chooseTorrent(self):
        x = 0
        while x not in range(1,self.numOfTor):
            x = int(input('Choose your torrent:' + '[1-' +  str(self.numOfTor) + ']: '))
        # Display chosen torrent
        print()
        print('\tChosen torrent: ')
        print(self.torName[x-1].contents[0])
        print(str(self.torSize[x-1]), end='\t')
        print(str(self.torDate[x-1]), end='\t')
        print(str(self.torSeeders[x-1].contents[0]), end='\t')
        print(str(self.torLeechers[x-1].contents[0]))
        # Retrieve and open magnet link
        mag = self.torMagnet[x-1].get('href')
        webbrowser.open(mag)
