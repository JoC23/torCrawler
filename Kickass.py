import requests, bs4, webbrowser
import threading
class KickassClass(threading.Thread):               # threading.Thread in the argument means that it is a parent(or base) class of the class 'Kickass'                                           
    def __init__(self, search):
        super(KickassClass, self).__init__()        # super() helps to call a function of a class's parent class. ( In this case, parent = threading.Thread.__init__() )
        self.url = 'http://kickass.cd/search.php?q=' + search
        
    def run(self):                                  # run method is called by a thread when thread.start() is executed.
        self.res = requests.get(self.url)
        self.res.raise_for_status()
        self.soup = bs4.BeautifulSoup(self.res.text, features='lxml')
        self.torName = self.soup.select('.markeredBlock a[class = "cellMainLink"]')
        self.numOfTor = len(self.torName)

    def displayNum(self):
        print('Kickass Torrents: ' + str(self.numOfTor) + ' torrents found.')

    def getElements(self):
        print('Fetching other information')
        print()
        
        # Magnet Link
        self.torMagnet = self.soup.select('a[title= "Torrent magnet link"]')

        # Size
        self.torSize = self.soup.select('td[class= "nobr center"]')

        # Date Created 
        self.torDate = self.soup.select('td[title]')

        # Seeders
        self.torSeeders = self.soup.select('td[class= "green center"]')

    def displayTorrent(self):
        if self.numOfTor == 0:
            print('No torrents available')
        else:
            for i in range(self.numOfTor):
                print(str(i+1) + '. ' + str(self.torName[i].contents[0]))
                print(str(self.torSize[i].contents[0]), end='\t') 
                print(str(self.torDate[i].contents[0]), end='\t')
                print('Seeds:' + str(self.torSeeders[i].contents[0]))
                print()

    def chooseTorrent(self):
        x = 0
        while x not in range(1,self.numOfTor):
            x = int(input('Choose your torrent:' + '[1-' +  str(self.numOfTor) + ']: '))
        # Display chosen torrent
        print()
        print('\tChosen torrent: ')
        print(self.torName[x-1].contents[0])
        print(str(self.torSize[x-1].contents[0]), end='\t')
        print(str(self.torDate[x-1].contents[0]))
        # Retrieve and open magnet link
        mag = self.torMagnet[x-1].get('href')
        webbrowser.open(mag)
