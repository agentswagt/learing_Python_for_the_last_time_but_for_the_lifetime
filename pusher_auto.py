import os
import time
time_gap = int(input("Time_Gap(in min)[default: 1 min]: "))
if time_gap == "":
    time_gap = 60
else:
    time_gap = time_gap*60
commit_name = input("Commit_Name: ")
branch_name = input("Branch Name: ")
if commit_name == "":
    commit_name = "ignored"
    print("[+] Commit Name --> ignored")
else:
    print("[+] Commit Name --> {}".format(commit_name))
if branch_name == "":
    branch_name = "main"
    print("[+] Branch Name: Main")
else:
    print("[+] Branch Name: {}".format(branch_name))

while True:
    os.system("git add .")
    os.system("git commit -m \"{}\"".format(commit_name))
    os.system("git push -u origin \"{}\"".format(branch_name))
    print("waiting")
    time.sleep(time_gap)