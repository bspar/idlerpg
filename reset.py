def stats(line):
    # get data from web
    f = open('irpg.db', 'rw')
    data = f.read()
    f.close()
    # first line has explanations, drop it
    data = data.split("\n")[line]
    # the data line is separated by tabs
    data = data.split("\t")
    # parse player data from list
    pd = {}
    try:
        pd['name'], pd['password'], pd['isadmin'], pd['level'], pd['class'], pd['nextttl'], \
        pd['nick'], pd['userhost'], pd['online'], pd['idled'], pd['xpos'], pd['ypos'], \
        pd['pen_mesg'], pd['pen_nick'], pd['pen_part'], pd['pen_kick'], pd['pen_quit'], pd['pen_quest'], pd['pen_logout'],\
        pd['created'], pd['lastlogin'], \
        pd['amulet'], pd['charm'], pd['helm'], pd['boots'], pd['gloves'], pd['ring'], pd['leggings'], pd['shield'], pd['tunic'], pd['weapon'], pd['alignment'] = data
    except ValueError:
        print 'fail'
    return pd


player = []
for i in range(1,14):
    pd = stats(i)
    pd['level'] = 0
    pd['nextttl'] = 90
    pd['amulet'] = 0
    pd['charm'] = 0
    pd['helm'] = 0
    pd['boots'] = 0
    pd['gloves'] = 0
    pd['ring'] = 0
    pd['leggings'] = 0
    pd['shield'] = 0
    pd['tunic'] = 0
    pd['weapon'] = 0
    player.append(pd['name'] + '\t' + pd['password'] + '\t' + str(pd['isadmin']) + '\t' + str(pd['level']) + '\t' + pd['class'] + '\t' + str(pd['nextttl']) + '\t' + \
    pd['nick'] + '\t' + pd['userhost'] + '\t' + str(pd['online']) + '\t' + str(pd['idled']) + '\t' + str(pd['xpos']) + '\t' + str(pd['ypos']) + '\t' + \
    str(pd['pen_mesg']) + '\t' + str(pd['pen_nick']) + '\t' + str(pd['pen_part']) + '\t' + str(pd['pen_kick']) + '\t' + str(pd['pen_quit']) + '\t' + str(pd['pen_quest']) + '\t' + str(pd['pen_logout']) + '\t' +\
    str(pd['created']) + '\t' + str(pd['lastlogin']) + '\t' + \
    str(pd['amulet']) + '\t' + str(pd['charm']) + '\t' + str(pd['helm']) + '\t' + str(pd['boots']) + '\t' + str(pd['gloves']) + '\t' + str(pd['ring']) + '\t' + str(pd['leggings']) + '\t' +\
    str(pd['shield']) + '\t' + str(pd['tunic']) + '\t' + str(pd['weapon']) + '\t' + pd['alignment'] + '\n')

f = open('db.test', 'a')
for i in range(0,13):
    f.write(player[i])
