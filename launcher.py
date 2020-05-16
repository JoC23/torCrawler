#! /usr/bin/python3
import sys, Kickass, Solid, Extra, Sky, threading, time

searchTerm = ' '.join(sys.argv[1:])
print('Processing...')

# Object Creation
# TODO Parallel Processing

start = time.perf_counter()

kickass = Kickass.KickassClass(searchTerm)
solid = Solid.SolidClass(searchTerm)
extra = Extra.ExtraClass(searchTerm)
sky = Sky.SkyClass(searchTerm)

# start() calls the run() method of the thread
kickass.start()             
solid.start()
extra.start()
sky.start()

kickass.join()
solid.join()
extra.join()
sky.join()

# object creations were drastically faster. 
# averaged to around 3 secs in contrast to 7-9 secs
# TODO Learn threading on objects

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} secs')

torrentsites = [kickass, solid, extra, sky]

# Display number of torrents available
index = 1
for i in torrentsites:
    print(str(index) + '.', end = ' ' )
    i.displayNum()
    index += 1
    print()

# Choose torrent site
x = 0
while x not in range(1,len(torrentsites) + 1):
    x = int(input('Choose your torrent site:' + '[1-' +  str(len(torrentsites)) + ']: '))
    print()
x -= 1

# TODO Improve this
print(torrentsites[x])

print()
torrentsites[x].getElements()       # get elements

torrentsites[x].displayTorrent()    # display all torrents

torrentsites[x].chooseTorrent()     # choose torrent