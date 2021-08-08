import os
import platform
import sys
print("\n\n")
print("		[1] English - Gofran\n		[2] English - Rokon\n		[3] Biology\n		[4] ICT\n		[5] Bangla - Halima Khanom\n		[6] Bangla - Sultana Ara Begum\n		[7] Physcis\n		[8] Highermath\n		[9] Chemistry")

print("\n")
class_number = input("[+] Select your Class: ")
class_number = str(class_number)

if class_number == "1":
	Subject_name2 = "english"


	teacher = "Muhammad Gofran"
	ID = "6911096065"
	Password = "14280529"
if class_number == "2":
	Subject_name2 = "english"

	teacher = "Rokan Jahangir"
	ID = "5953408143"
	Password = "14220529"
if class_number == "3":
	teacher_image = "biology.jpeg"
	Subject_name2 = "biology"

	ID = "7419175762"
	Password = "3456"
if class_number == "4":

	Subject_name2 = "ict"
	teacher = "Abdullah Al Maruf"
	ID ="8615434353"
	Password = "8Lttk8"
if class_number == "5":
	Subject_name2 = "Bangla"
	teacher = "Halima Khanom"

	ID = "7522389093"
	Password = "ABA6uJ"
if class_number == "6":
	Subject_name2 = "Bangla"
	teacher = "Sultana Ara Begum"

	ID = "3329293832"
	Password = "14280529"
if class_number == "7":
	Subject_name2 = "physics"
	teacher = "MD. Mujibul Alam"

	ID = "7645869114"
	Password = "AbCd0123"       
if class_number == "8":
	Subject_name2 = "highermath"
	teacher = "MD. Amanat Ali Khan"

	ID = "7216954315"
	Password = "45678"
if class_number == "9":
	Subject_name2 = "chemistry"
	teacher = "Ramkrisna Dhar"

	ID = "3346504150"
	Password = "W2FPcA"
Subject_name2 = Subject_name2.capitalize()
print("\n")
print("[+] All Details Here: \n")
print("		[*] Subject Name: {}\n		[*] Teacher Name: {}\n		[*] ID: {}\n		[*] Password: {}".format(Subject_name2, teacher, ID, Password))
print("\n")
req_for_link = input("Do you want to get the Link:(press ENTER for yes)")

if req_for_link == "":
	platforms = platform.system()
	platforms = platforms.lower()
	
	link = "https://us04web.zoom.us/j/{}".format(ID)
	if platforms.startswith("lin"):
		
		os.system("google-chrome {}".format(link))
		sys.exit()
	if platforms.startswith("win"):
		os.system("start chrome {}".format(link))
	
