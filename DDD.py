import re
import time
import getpass

def convert_link(original_link):
    # Extract the file ID from the original link
    file_id_match = re.search(r'/d/([^/]+)/', original_link)
    if file_id_match:
        file_id = file_id_match.group(1)

        # Build the modified link
        modified_link = "https://drive.google.com/uc?id={}&export=download".format(file_id)

        return modified_link
    else:
        return None

# Example usage
art = """
================================================================

  ____      ____      ____    
 |  _"\    |  _"\    |  _"\   
/| | | |  /| | | |  /| | | |  
U| |_| |\ U| |_| |\ U| |_| |\ 
 |____/ u  |____/ u  |____/ u 
  |||_      |||_      |||_    
 (__)_)    (__)_)    (__)_)   

================================================================
Direct Drive Downloader(DDD) v1.5
Visit : www.mrkonaymyoaungict.site 
//Create by Ko Nay Myo Aung
"""

print("\033[1;36;40m" ,art)

original_link = input("\033[1;33;40m Enter the Drive link: \n")

# Show loading message
print("Generating..... ", end="")
for _ in range(10):
    print("#", end="", flush=True)
    time.sleep(0.5)

modified_link = convert_link(original_link)

if modified_link:
    print("\033[1;32;40m \n Direct Link:", modified_link)
    
else:
    print("\n \033[1;31;40m Invalid original link provided.")
   
