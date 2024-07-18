from enum import Enum
import re
import json


{
    "TEXT": "<p>{content}</p>",
    "TITLE1": "<h1>{content}</h1>",
    "TITLE1": "<h1>{content}</h1>",
    "TITLE1": "<h1>{content}</h1>",
    "TITLE1": "<h1>{content}</h1>",
    "TITLE1": "<h1>{content}</h1>",
    "TITLE1": "<h1>{content}</h1>",
    "QUOTE": "<blockquote>{content}</blockquote>",
    "REF": "<div class=\"reference\">{content}</div>",
    "CODE": "<pre>{content}</pre>",
    "TABLE": "<table>{content}</table>",
    "FORMULA": "<div>{content}</div>"
}


def main():
    lines = open('src.blog', 'r').readlines()
    lines = tag_lines()
    
def tag_lines(lines):
    ""
    if 


    


# print(json.dumps(content, ensure_ascii=False))
# print(re.search(r'```\n', content))


content = re.sub(r'```(.*)```', r'<pre>\1</pre>', content, flags=re.DOTALL)
content = re.sub(r'<pre>(python|java|text|html|css|c\+\+|bash)\n', r'<pre language="\1">\n', content)
content = re.sub(r'\$(.*)\$', r'<code>\1</code>', content)
print(content)

