import os


folder = 'C:\\New Folder (71)\\Visual Studio\\_Projects\\Arcaea b30\\'

def get_jacket_arts(path):
    with open(path, 'r') as file, open(folder+'Text Files\\jacket arts.txt', 'w') as new:
        for line in file:
            temp = []
            thing = line.strip()
            if thing:
                static = 0
                revision = 0
                while static != -1:
                    static = thing.find('static', static)
                    if static == -1:
                        break
                    revision = thing.find('revision', revision)
                    art = thing[static:revision-1]
                    static += 1
                    revision += 1
                    if art not in temp:
                        temp.append(art)
                if temp:
                    new.write('\n'.join(temp))
            else:
                new.write('\n\n')

def filter_links(path):
    with open(path, 'r') as file, open(folder+'Text Files\\jacket arts.txt', 'w') as new:
        for line in file:
            thing = line.strip()
            static = thing.find('https://static')
            if static == -1 or 'scale-to-width' in thing:
                continue
            revision = thing.find('revision')
            art = thing[static:revision-1]
            new.write(art+'\n')

def find_missing_links(path):
    arts = {}
    keys = []
    with open(path, 'r') as file:
        for line in file:
            thing = line.strip()
            start = thing.rfind('/')
            song = thing[start+1:]
            arts[song] = 1
            keys.append(song)

    jackets = folder+'Jacket Arts\\'
    for jacket in os.listdir(jackets):
        if jacket in keys:
            arts[jacket] += 1
        else:
            arts[jacket] = 1

    for key in keys:
        if arts[key] != 2:
            print(f"{key} - {arts[key]}")

def remove_duplicate_links(path):
    links = []
    with open(path, 'r') as file, open(folder+'Text Files\\non-dupe arts.txt', 'w') as new:
        for line in file:
            thing = line.strip()
            if thing not in links:
                links.append(thing)
                new.write(thing+'\n')

def delete_dupes(path):
    for jacket in os.listdir(path):
        if '(1)' in jacket:
            os.remove(path+jacket)

def recalculate_links(path):
    delete_dupes(path+'Jacket Arts\\')

    arts = []
    for jacket in os.listdir(path+'Jacket Arts\\'):
        arts.append(jacket)

    links = []
    with open(path+'Text Files\\non-dupe arts.txt', 'r') as file:
        for line in file:
            thing = line.strip()
            start = thing.rfind('/')
            song = thing[start+1:]
            if song not in arts:
                links.append(thing)

    with open(path+'Text Files\\non-dupe arts.txt', 'w') as file:
        file.write('\n'.join(links))
        
    delete_dupes(path+'Jacket Arts\\')

def replace_chars():
    chars = {'%21':'!', '%22':'\"', '%23':'#', '%24':'$', '%25':'%', '%26':'&', '%27':'\'',
             '%28':'(', '%29':')', '%2A':'', '%2B':'+', '%2C':',', '%2D':'-', '%2E':'.', '%2F':'/'}
    jackets = folder+'Jacket Arts\\'
    for jacket in os.listdir(jackets):
        old = jacket
        if '_' in jacket:
            jacket = jacket.replace('_', ' ')
        if '%' in jacket:
            for key, val in chars.items():
                jacket = jacket.replace(key, val)
        if old != jacket:
            os.rename(jackets+old, jackets+jacket)

def read_csv():
    with open(folder+'Csv Files\\chart data.csv', r'r') as file:
        i = 0
        for line in file:
            thing = line.strip()
            #if thing.count(',') != 2:
                #print(thing)
            i += 1
            print(f"{i}: {thing}")

def match_song_names():
    arts = {}
    keys = []
    with open(folder+'Csv Files\\chart data.csv', 'r') as file:
        for line in file:
            thing = line.strip()
            end = thing.find(',')
            song = thing[:end]
            if song not in keys:
                arts[song] = 1
                keys.append(song)

    jackets = folder+'Jacket Arts\\'
    for jacket in os.listdir(jackets):
        jacket = jacket[:-4]
        if jacket in keys:
            arts[jacket] += 1
        else:
            arts[jacket] = 1
    i = 1
    for key in keys:
        if arts[key] < 2:
            print(f"{key} - {arts[key]}")
            i += 1
            if i%5 == 0:
                print()

