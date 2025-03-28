"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper().replace("O", "0", 2).replace("I", "1").replace("A", "@")
    result = list(result)
    return result  

