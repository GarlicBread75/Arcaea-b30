folder = 'C:\\New Folder (71)\\Visual Studio\\_Projects\\Arcaea b30\\Text Files\\'

def get_jacket_arts(path):
    with open(path, 'r') as file, open(folder+'jacket arts.txt', 'w') as new:
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
    with open(path, 'r') as file, open(folder+'jacket arts.txt', 'w') as new:
        for line in file:
            thing = line.strip()
            static = thing.find('https://static')
            if static == -1 or 'scale-to-width' in thing:
                continue
            revision = thing.find('revision')
            art = thing[static:revision-1]
            new.write(art+'\n')

filter_links(folder+'extracted links.txt')