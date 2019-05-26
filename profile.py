import sys
import json
from LinkedinController import LinkedinController


def main(params):
    linkedin = LinkedinController(config=True, debug=True)
    linkedin.login()
    linkedin.search('murat')
    # profile = linkedin.profile("https://www.linkedin.com/in/agitt/")
    # print(json.dumps(profile))


if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
