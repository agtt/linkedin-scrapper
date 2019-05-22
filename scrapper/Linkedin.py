import re
import urllib.parse as parse
import json

class Linkedin:
    def __init__(self):
        pass

    def profile(self, html):
        find = re.findall("<code style=\"display: none\" id=\"bpr-guid-(.*?)\">([\s\S]*?)</code>", html)
        person = ""
        for data in find:
            if '{&quot;*profile' in data[1]:
                person = json.loads(parse.unquote(self.html_escape(data[1])))
                break
        return json.dumps(person)

    def search(self):
        pass

    def html_escape(text):
        return text.replace("&quot;", '"').replace('&apos;', "'").replace('&gt;', '>').replace('&lt;', '<')
