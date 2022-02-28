import requests
import sys
import time
import os
if __name__ == '__main__':
    print(sys.argv[1])
    comp = "https://www.intel.com/content/www/us/en/homepage.html"
    len(comp)

    r = requests.head("https://www.intel.com/content/www/us/en/download/" + str(sys.argv[1])+"/", allow_redirects=True)
    time.sleep(3)
    if(r.url[0:len(comp)] != comp):
        name = ""+str(sys.argv[1])+".txt"
        f = open(""+str(sys.argv[1])+".txt", "w")
        f.write(r.url)
        f.close()
        os.system("gsutil cp " + name + " gs://int_valid_webs/" + name)
    if(r.status_code == 403):
        name = "FORBIDDEN" + str(sys.argv[1]) + ".txt"
        f = open("FORBIDDEN" + str(sys.argv[1]) + ".txt", "w")
        f.close()
        os.system("gsutil cp " +name + " gs://int_valid_webs/"+name)
    if("oem" in r.url):
        name = "OEM"+str(sys.argv[1])+".txt"
        f = open("OEM"+str(sys.argv[1])+".txt", "w")
        f.write(r.url)
        f.close()
        os.system("gsutil cp " + name + " gs://int_valid_webs/" + name)
