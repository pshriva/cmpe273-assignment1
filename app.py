from flask import Flask
import sys
from github import Github
import base64
app = Flask(__name__)
import base64
reponame = []
github = Github()
reponame = str(sys.argv[1]).split("/")
#github = Github(reponame[4],baseurl)
@app.route("/v1/<filename>")
def get_config(filename):
   user = github.get_user()
   repository = user.get_repo(reponame[4])
   file_content = repository.get_file_contents(filename).content
   return base64.b64decode(file_content)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
