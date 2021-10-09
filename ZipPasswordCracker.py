import zipfile

pwd_filename = "rockyou.txt"//wordlist
zip_filename = "File.zip"//zipFile

with open(pwd_filename, "rb") as passwords:
    
     
    passwords_list = passwords.readlines()    
    
    total_passwords = len(passwords_list)
    
    my_zip_file = zipfile.ZipFile(zip_filename)
    
    for index, password in enumerate(passwords_list):
        
        try:
            my_zip_file.extractall(path="Extracted Folder",  pwd=password.strip())
            print("\n +++++++++++++++++++SUCCESS+++++++++++++++++++++++")
            print("Password Found: ", password.decode().strip())
            print("All Files has been Extracted inside the New DIrectory Extracted Folder")
            break
        
        #if password fails
        except:
            
            print(f"!..................................Scanning complete {round((index/total_passwords)*100, 2)}%")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"Trying password {password.decode().strip()} ")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!FAIL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            continue
