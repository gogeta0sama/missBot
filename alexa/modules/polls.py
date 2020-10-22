__mod_name__ = "Polls 🎲"

__help__ = """
You can now send polls anonymously with Alexa

Here is how you can do it:

*Parameters* -
 ▪️ poll_id - a poll id consists of an 5 digit random integer, this id is automatically removed from the system when you stop your previous poll
 ▪️ question - the question you wanna ask
 ▪️ <True@optionnumber/False>(1) - quiz mode, you must state the correct answer with `@` eg: `True@1` or `True@2`
 ▪️ <True/False>(2) - public votes 
 ▪️ <True/False>(3) - multiple choice 

*Syntax* - 
`/poll <poll_id> <question> | <True@optionnumber/False> <True/False> <True/False> <option1> <option2> ... upto <option10>`

*Examples* -
`/poll 12345 | am i cool? | False False False yes no`
`/poll 12345 | am i cool? | True@1 False False yes no`

*To stop a poll*
Reply to the poll with /stoppoll <poll_id> to stop the poll
"""
