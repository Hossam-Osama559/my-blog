from django.http import HttpResponse 
from django.shortcuts import render

import os as os_

def index(req):

    return render(req,"index.html",{})




def os(req,number):

    file_name="os"+number

    file_content=""
#/home/hossam123/my_blog/static/os/

    if os_.path.exists(f"/home/hossam123/my_blog/static/os/{file_name}.txt"):

        with open(f"/home/hossam123/my_blog/static/os/{file_name}.txt","r") as f:

            file_content=f.read()
    

   

        return render(req,"os.html",{"content":file_content})

    else:
        return HttpResponse("this file not exist")
    

def random(req,number):

    file_name="random"+number

    file_content=""
#/home/hossam123/my_blog/static/os/

    if os_.path.exists(f"/home/hossam123/my_blog/static/random/{file_name}.txt"):

        with open(f"/home/hossam123/my_blog/static/random/{file_name}.txt","r") as f:

            file_content=f.read()
    

   

        return render(req,"random.html",{"content":file_content})

    else:
        return HttpResponse("this file not exist")