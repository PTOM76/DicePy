import random

print("Content-type: text/html;charset=utf-8\n");
r = random.randint(1,6);
string = "サイコロを振り、<b>" + str(r) + "</b>がでました。<br /><img style=\"width:50px;height:50px;border: 1px solid;\" src=\"../img/dice_" + str(r) + ".png\" />";
print("""
<html>
    <head></head>
    <body>
        """+ string +"""
    </body>
 </html>
""");