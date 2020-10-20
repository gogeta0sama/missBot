import asyncio
import inspect
import io
import sys
import traceback
from telethon import errors, events, functions, types
from alexa.events import register
from alexa import OWNER_ID

@register(pattern="^/eval")
async def _(event):
    check = event.message.sender_id
    checkint = int(check)
    # print(checkint)
    if int(check) != int(OWNER_ID):
        return
    cmd = event.text.split(" ", maxsplit=1)[1]
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success 😃"

    final_output = "**EVAL**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    if len(final_output) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await tbot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            
    else:
        await event.reply(final_output)

async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(slitu.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f'async def __aexec(message, reply, client, p): ' +
        '\n event = smessatatus = message' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](message, reply, message.client, p)

