import bs                           #Created By MythB # http://github.com/MythB
import bsInternal
import os

chatfile = '/root/bs/chat/ChatMessages.html'
#Use your own file location here
class Optchat(object):

    def collector(self, msg, nick, accountID):
        #get the current time
        msgTime = ''
        from datetime import datetime
        msgTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        #generate a pretty html log table (ignore errors it's fine)
        if not os.path.exists(chatfile):
            with open(chatfile,mode='w') as f:
                f.write("""<!DOCTYPE html><head><meta charset="UTF-8"></head><body><p><b>Automatically generated by <a href="http://bombsquadgame.com ">
                        BombSquad</a> Server - Created by <a href="http://github.com/MythB ">MythB</a> - """ +msgTime+ """
                        </b></p><style>table,th,td {border: 0.1px solid grey;}</style><table style="width:100%"><tr>
                        <th align="left">NAME</th><th align="left">MESSAGE</th><th align="left">DATE</th><th align="left">ACCOUNT-ID</th></tr>""")           
        else:
            with open(chatfile,mode='a') as f:
                f.write('<tr><td>'+nick+'</td><td>'+msg+'</td><td>'+msgTime+'</td><td>'+accountID+'</td></tr>')
t=Optchat()
def collectedMsg(msg, clientID):
    isAccAccesible = False #check is account id accesible
    if bsInternal._getForegroundHostActivity() is not None:
        if bsInternal._getForegroundHostActivity().players:# check if player exists
            for i in bsInternal._getForegroundHostActivity().players:
                if i.getInputDevice().getClientID() == clientID:
                    isAccAccesible = True
                    accountID = i.get_account_id()
                    nick = i.getName().encode('utf8')
                    t.collector(msg, nick, accountID)
                    break
            if not isAccAccesible: # if not, go without account ıd
                for s in bsInternal._getGameRoster():
                    if s['clientID'] == clientID:
                        nick = s['displayString']
                        accountID = 'NOT FOUND'
                        t.collector(msg, nick, accountID)
                        break
        else:#if not, continue from here
            for s in bsInternal._getGameRoster():
                if s['clientID'] == clientID:
                    nick = s['displayString']
                    accountID = 'NOT FOUND'
                    t.collector(msg, nick, accountID)
                    break