def get_jacket_arts(path):
    with open(path, 'r') as file, open(folder+'new.txt', 'w') as new:
        for line in file:
            temp = []
            thing = line.strip()
            if thing:
                # find has custom range
                thing.count()
                start = thing.find('stat')
                end = thing.find('revi')-1
                art = thing[start:end]
                if art not in temp:
                    temp.append(art+'\n')
            else:
                temp.append('\n')
# open file
# make new file
# read lines
# if find empty line
#     add empty line to new
# elif find matching link
#     add link to new

folder = 'C:\\New Folder (71)\\Visual Studio\\_Projects\\Arcaea b30\\'
#get_jacket_arts(folder+'notes.txt')