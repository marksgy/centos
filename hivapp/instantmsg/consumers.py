import json
from channels import Channel, Group
from channels.sessions import enforce_ordering, channel_session
from django.db.models import Count

from .models import People, ChatMessage, ChatList
from oflMsgForm.myFuncs.sendForm import sendForm
from ..hiv.models import UserInfo


# Connected to websocket.connect
def msg_consumer(message):
    # Save to model
    fromid = message.content['fromid']
    toid = message.content['toid']
    msg = message.content['msg']
    time = message.content['time']
    topeople = People.objects.get(id=toid)
    to_channel = topeople.reply_channel

    sendornot = int(message.content['sendornot'])
    chatmessage = ChatMessage.objects.create(
        fromid=fromid,
        toid=toid,
        text=msg,
    )
    chatlist = ChatList.objects.filter(id1=fromid).filter(id2=toid) | ChatList.objects.filter(id2=fromid).filter(
        id1=toid)
    frompeople = UserInfo.objects.get(id=fromid)

    if not chatlist:
        newchatlist = ChatList.objects.create(
            id1=fromid,
            id2=toid,
            id1deleted=0,
            id2deleted=0
        )

    # 发一次消息
    if sendornot:
        Channel(to_channel).send({
            "text": json.dumps({
                'id': fromid,
                'nickname': frompeople.nickname,
                'photo': frompeople.vatarUrl,
                'msg': msg,
                'time': time,
            }),
        })
        chatmessage.issent = 1
    else:
        sendForm("session")
        chatmessage.issent = 0
    chatmessage.save()


@channel_session
def ws_usualconnect(message):
    message.reply_channel.send({"accept": True})


@channel_session
def ws_message(message):
    # Parse the query string

    msssg = json.loads(message["text"])

    id = msssg['id']
    toid = msssg['toid']
    msg = msssg['msg']
    time = msssg['time']

    if toid == 'first':
        people_exist = People.objects.filter(id=id)

        if not people_exist:
            people = People.objects.create(id=id, reply_channel=message.reply_channel.name)
        else:
            people = people_exist[0]
            people.reply_channel = message.reply_channel.name

        chatmsgs = ChatMessage.objects.filter(toid=id).filter(issent=0)
        chatlists = ChatList.objects.filter(id1=id).filter(id1deleted=0) | ChatList.objects.filter(id2=id).filter(
            id2deleted=0)

        # 还需要更改数据库，加入自定义id，取出名字和最后一条信息
        message.channel_session["id"] = id
        mychatlist = []
        mymsg = []
        # 取出历史消息列表~ok！
        for chatlist in chatlists:
            filters = chatmsgs.filter(chatlist=chatlist).order_by(-'time')
            lastMessage = filters[0].text
            unreadCount = filters.count()
            lastSendTime = filters[0].time.strftime('%Y-%m-%d %H:%M')
            if chatlist.id1 == id:
                user = UserInfo.objects.get(id=chatlist.id2)
                onechatlist = {
                    'id': chatlist.id,
                    'unreadCount': unreadCount,
                    'lastMessage': lastMessage,
                    'lastSendTime': lastSendTime,
                    'user': {
                        'id': chatlist.id2,
                        'nickname': user.nickname,
                        'photo': user.vatarUrl
                    }

                }
                mychatlist.append(onechatlist)
            else:
                user = UserInfo.objects.get(id=chatlist.id1)
                onechatlist = {
                    'id': chatlist.id,
                    'unreadCount': unreadCount,
                    'lastMessage': lastMessage,
                    'lastSendTime': lastSendTime,
                    'user': {
                        'id': chatlist.id1,
                        'nickname': user.nickname,
                        'photo': user.vatarUrl
                    }
                }
                mychatlist.append(onechatlist)

        for chatmsg in chatmsgs:
            onemsg = {
                'id': chatmsg.fromid,
                'nickname': frompeople.nickname,
                'photo': frompeople.vatarUrl,
                'msg': msg,
                'time': time,
                'fromid': chatmsg.fromid,
                'msg': chatmsg.text,
            }
            mymsg.append(onemsg)
            chatmsg.issent = 1
            chatmsg.save()
        people.online = 1
        people.save()

        message.reply_channel.send({
            'text': json.dumps({
                'chatlist': mychatlist,
                'chatmsg': mymsg,
            })
        })
    else:
        frompeople = People.objects.get(id=id)
        topeople = People.objects.get(id=toid)

        frompeople_online = frompeople.online
        topeople_online = topeople.online

        sendornot = frompeople_online * topeople_online

        Channel("chat-messages").send({

            "msg": msg,
            "fromid": id,
            "toid": toid,
            "sendornot": sendornot,
            "time": time

        })


@channel_session
def ws_disconnect(message):
    id = message.channel_session['id']
    people = People.objects.get(id=id)
    people.online = 0
    people.save()
