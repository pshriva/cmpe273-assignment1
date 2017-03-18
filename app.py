from flask import Flask
import sys
from github import Github
import base64
app = Flask(__name__)
import base64
reponame = []
github = Github()
reponame = str(sys.argv[1]).split("/")
@app.route("/v1/<filename>")
def get_config(filename):
 try:
    if('.yml' in filename or '.json' in filename):
     file_content = github.get_user(reponame[3]).get_repo(reponame[4]).get_file_contents(filename).content
     return base64.b64decode(file_content)
    else:
       return "Please provide either yml or json file"
 except Exception:
      return "No such file found"
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
