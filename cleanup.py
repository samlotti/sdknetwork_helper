
import re

##
## Simple python to cleans a list of 
##    SKAdNetworkIdentifier's
##

f = open("source.txt", "r")
o = open("output.txt", "w")

source = f.read()
source = source.replace("<string>","\n<string>")
source = source.replace("</dict>","\n</dict>")
matches = re.findall("<string>(.*)</string>", source)

unique = set()
for entry in matches:
    unique.add(entry.lower())
sorted = []
for entry in unique:
    sorted.append(entry)
    sorted.sort()
for entry in sorted:
    o.write("""		<dict>
			<key>SKAdNetworkIdentifier</key>
""")
    o.write("\t\t\t<string>")
    o.write(entry)
    o.write("</string>\n		</dict>\n")


o.close()
