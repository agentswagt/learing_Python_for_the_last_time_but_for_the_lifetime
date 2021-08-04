import os

commit_name = input("Commit_Name: ")
if commit_name == "":
    commit_name = "ignored"

os.system("git add .")
os.system("git commit -m \"{}\"".format(commit_name))
os.system("git push -u origin main")