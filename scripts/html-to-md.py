# coding=utf-8

import subprocess, sys

assert(sys.argv[1].startswith("proceedings/"))
rel = ""
for i in range(2,sys.argv[1].count("/")):
  rel = rel + "../"

output = open(sys.argv[1]).read()
output = output.replace(' class="selected"', "").strip()
head = \
"""<div id="textContent">"""

foot = """</div> <!-- <div id="textContent"> -->"""

#print(output)
#print(head)
#print(rel)

assert(head in output)
assert(foot in output)
output = output.split(head,1)[1].split(foot)[0]
output = output.strip()
# output = output + "</div>"

mdfile = sys.argv[1].replace(".html",".md")
open(mdfile, "w").write(output)
subprocess.check_output(["git", "add", mdfile])
subprocess.check_output(["git", "rm", "-f", sys.argv[1]])
