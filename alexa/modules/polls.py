__mod_name__ = "Polls 🎲"

__help__ = """
You can now send polls anonymously with Alexa

Here is how you can do it:

*Parameters* -
 ▪️ question - the question you wanna ask
 ▪️ <True@optionnumber/False>(1) - quiz mode, you must state the correct answer with @ eg `True@1` or `True@2`
 ▪️ <True/False>(2) - public votes 
 ▪️ <True/False>(3) - multiple choice

*Syntax* - 
`/poll <question> | <True@optionnumber/False> <True/False> <True/False> <option1> <option2> ... upto <option10>`

*Examples* -
`/poll am i cool? | False False False yes no`
`/poll am i cool? | True@1 False False yes no`
