import random
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

r = random.randint(1,6);
string = "サイコロを振り、<b>" + str(r) + "</b>がでました。<br /><img style=\"width:50px;height:50px;border: 1px solid;\" src=\"../img/dice_" + str(r) + ".png\" />";
print("Content-type: text/html;charset=utf-8\n");
print("""
<html>
    <head>
    	<meta http-equiv="content-type" charset="UTF-8">
	</head>
    <body>
        """+ string +"""
    </body>
 </html>
""");