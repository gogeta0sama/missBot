# MADE BY @MissAlexa_Robot

from telethon import *
from telethon.tl import *
from alexa.events import register
from pymongo import MongoClient
from alexa import MONGO_DB_URI
from alexa.events import register
from alexa import tbot


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client['test']
approved_users = db.approve


#------ THANKS TO LONAMI ------#
async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)
        )
    elif isinstance(chat, types.InputPeerChat):
        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator)
        )
    else:
        return None



@register(pattern="^/poll (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*) (.*)")
async def _(event):
    approved_userss = approved_users.find({})
    for ch in approved_userss: 
        iid = ch['id']
        userss = ch['user']
    if event.is_group:
     if (await is_register_admin(event.input_chat, event.message.sender_id)):
       pass
     elif event.chat_id == iid and event.from_id == userss:  
       pass
     else:
       return
    quiz = event.pattern_match.group(1)
    if "True" in quiz:
       quizy = True
    elif "False" in quiz:
       quizy = False
    else:
       await event.reply("Wrong arguments provided !")
       
    pvote = event.pattern_match.group(2)
    if "True" in pvote:
       pvoty = True
    elif "False" in pvote:
       pvoty = False
    else:
       await event.reply("Wrong arguments provided !")
       
    mchoice = event.pattern_match.group(3)
    if "True" in mchoice:
       mchoicee = True
    elif "False" in mchoice:
       mchoicee = False
    else:
       await event.reply("Wrong arguments provided !")
       
    ques = event.pattern_match.group(4)
    ab = event.pattern_match.group(5)
    cd = event.pattern_match.group(6)
    ef = event.pattern_match.group(7)
    gh = event.pattern_match.group(8)
    ij = event.pattern_match.group(9)
    kl = event.pattern_match.group(10)
    mn = event.pattern_match.group(11)
    op = event.pattern_match.group(12)
    qr = event.pattern_match.group(13)
    st = event.pattern_match.group(14)
    
    if pvoty==False and quizy==False and mchoicee==False:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            types.PollAnswer(ab, b'xnx'),
            types.PollAnswer(cd, b'xxnx'),
            types.PollAnswer(ef, b'dxx'),
            types.PollAnswer(gh, b'dnx'),
            types.PollAnswer(ij, b'xnxxx'),
            types.PollAnswer(kl, b'kskss'),
            types.PollAnswer(mn, b'djdj'),
            types.PollAnswer(op, b'djdjddkd'),
            types.PollAnswer(qr, b'skskslz'),
            types.PollAnswer(st, b'djdbsjs'),
          ],
          quiz=False
            ),           
        ))

    if pvoty==True and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            types.PollAnswer(ab, b'xnx'),
            types.PollAnswer(cd, b'xxnx'),
            types.PollAnswer(ef, b'dxx'),
            types.PollAnswer(gh, b'dnx'),
            types.PollAnswer(ij, b'xnxxx'),
            types.PollAnswer(kl, b'kskss'),
            types.PollAnswer(mn, b'djdj'),
            types.PollAnswer(op, b'djdjddkd'),
            types.PollAnswer(qr, b'skskslz'),
            types.PollAnswer(st, b'djdbsjs'),
          ],
          quiz=False,
          multiple_choice=True, 
          public_vote=True
            ),           
        ))

    if pvoty==True and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            types.PollAnswer(ab, b'xnx'),
            types.PollAnswer(cd, b'xxnx'),
            types.PollAnswer(ef, b'dxx'),
            types.PollAnswer(gh, b'dnx'),
            types.PollAnswer(ij, b'xnxxx'),
            types.PollAnswer(kl, b'kskss'),
            types.PollAnswer(mn, b'djdj'),
            types.PollAnswer(op, b'djdjddkd'),
            types.PollAnswer(qr, b'skskslz'),
            types.PollAnswer(st, b'djdbsjs'),
          ],
          quiz=False,
          multiple_choice=True, 
          public_vote=True
            ),           
        ))

    if pvoty==False and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            types.PollAnswer(ab, b'xnx'),
            types.PollAnswer(cd, b'xxnx'),
            types.PollAnswer(ef, b'dxx'),
            types.PollAnswer(gh, b'dnx'),
            types.PollAnswer(ij, b'xnxxx'),
            types.PollAnswer(kl, b'kskss'),
            types.PollAnswer(mn, b'djdj'),
            types.PollAnswer(op, b'djdjddkd'),
            types.PollAnswer(qr, b'skskslz'),
            types.PollAnswer(st, b'djdbsjs'),
          ],
          quiz=False,
          multiple_choice=True, 
          public_vote=False
            ),           
        ))

    if pvoty==True and quizy==False and mchoicee==False:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            types.PollAnswer(ab, b'xnx'),
            types.PollAnswer(cd, b'xxnx'),
            types.PollAnswer(ef, b'dxx'),
            types.PollAnswer(gh, b'dnx'),
            types.PollAnswer(ij, b'xnxxx'),
            types.PollAnswer(kl, b'kskss'),
            types.PollAnswer(mn, b'djdj'),
            types.PollAnswer(op, b'djdjddkd'),
            types.PollAnswer(qr, b'skskslz'),
            types.PollAnswer(st, b'djdbsjs'),
          ],
          quiz=False,
          multiple_choice=False, 
          public_vote=True
            ),           
        ))

