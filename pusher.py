import os

commit_name = input("Commit_Name: ")
branch_name = input("Branch Name: ")
if commit_name == "":
    commit_name = "ignored"
    print("[+] Commit Name --> ignored")
if branch_name == "":
    branch_name = "main"
    print("[+] Branch Name: Main")

os.system("git add .")
os.system("git commit -m \"{}\"".format(commit_name))
os.system("git push -u origin \"{}\"".format(branch_name))