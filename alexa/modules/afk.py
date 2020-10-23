from alexa import dispatcher
from alexa.modules.sql import afk_sql as sql
from alexa.modules.users import get_user_id
from telegram import MessageEntity, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, Filters, MessageHandler, run_async, CommandHandler
import time
from telegram import ParseMode

AFK_GROUP = 7
AFK_REPLY_GROUP = 8


@run_async
def afk(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    user = update.effective_user

    if not user:  # ignore channels
        return

    if user.id == 777000:
        return
    fname = update.effective_user.first_name
    notice = ""
    if len(args) >= 2:
        reason = args[1]
        if len(reason) > 100:
            reason = reason[:100]
            notice = "{fname} your afk reason was shortened to 100 characters."
    else:
        reason = ""
    start_time = time.time()
    sql.set_afk(update.effective_user.id, reason, start_time)
    fname = update.effective_user.first_name
    try:
        update.effective_message.reply_text("*{} is now AFK !*\n\n{}".format(
            fname, notice), parse_mode=ParseMode.MARKDOWN)
    except BadRequest:
        pass


@run_async
def no_longer_afk(update: Update, context: CallbackContext):
    user = update.effective_user
    message = update.effective_message

    if not user:  # ignore channels
        return

    res = sql.rm_afk(user.id)
    if res:
        if message.new_chat_members:  # dont say msg
            return
        firstname = update.effective_user.first_name
        try:
            text = "*{} is no longer AFK !*".format(firstname)
            update.effective_message.reply_text(
                text, parse_mode=ParseMode.MARKDOWN)
        except BaseException:
            return


@run_async
def reply_afk(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.effective_message
    userc = update.effective_user
    userc_id = userc.id
    if message.entities and message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]):
        entities = message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION])

        chk_users = []
        for ent in entities:
            if ent.type == MessageEntity.TEXT_MENTION:
                user_id = ent.user.id
                fst_name = ent.user.first_name

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

            if ent.type == MessageEntity.MENTION:
                user_id = get_user_id(message.text[ent.offset:ent.offset +
                                                   ent.length])
                if not user_id:
                    # Should never happen, since for a user to become AFK they
                    # must have spoken. Maybe changed username?
                    return

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

                try:
                    chat = bot.get_chat(user_id)
                except BadRequest:
                    print("Error: Could not fetch userid {} for AFK module"
                          .format(user_id))
                    return
                fst_name = chat.first_name

            else:
                return

            check_afk(update, context, user_id, fst_name, userc_id)

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fst_name = message.reply_to_message.from_user.first_name
        check_afk(update, context, user_id, fst_name, userc_id)


def check_afk(update, context, user_id, fst_name, userc_id):
    if sql.is_afk(user_id):
        user = sql.check_afk_status(user_id)
        if not user.reason:
            etime = user.start_time
            elapsed_time = time.time() - float(etime)
            final = time.strftime("%Hh: %Mm: %Ss", time.gmtime(elapsed_time))

            if int(userc_id) == int(user_id):
                return
            res = "*{} is AFK !*\n\n*Last seen*: {}".format(fst_name, final)
            update.effective_message.reply_text(
                res, parse_mode=ParseMode.MARKDOWN)
        else:
            etime = user.start_time
            elapsed_time = time.time() - float(etime)
            final = time.strftime("%Hh: %Mm: %Ss", time.gmtime(elapsed_time))

            if int(userc_id) == int(user_id):
                return
            res = "*{} is AFK !*\n\n*Reason*: {}\n\n*Last seen*: {}".format(
                fst_name, user.reason, final)
            update.effective_message.reply_text(
                res, parse_mode=ParseMode.MARKDOWN)


AFK_HANDLER = CommandHandler("afk", afk)
NO_AFK_HANDLER = MessageHandler(Filters.all & Filters.group, no_longer_afk)
AFK_REPLY_HANDLER = MessageHandler(Filters.all & Filters.group, reply_afk)

dispatcher.add_handler(AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(NO_AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REPLY_HANDLER, AFK_REPLY_GROUP)

__mod_name__ = "AFK"
