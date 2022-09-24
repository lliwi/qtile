from libqtile.command.client import InteractiveCommandClient
#import sys
#sys.path.append("../qtile/settings")
#from settings.groups import groups

c = InteractiveCommandClient()
#print(c.status())
opened = []
groups = ['   ','   ','   ', '   ', ' 磊  ','   ', '   ']
for x in groups:
    info =  c.group[x].info()
    opened.append(str(len(info.get('windows'))))
print(*opened, sep = " ")

