from django.http import HttpResponse 
from django.shortcuts import render



def index(req):

    return render(req,"index.html",{})




def os(req,number):

    file_name="os"+number

    file_content=""

    with open(f"/home/hossam123/my_blog/static/os/{file_name}.txt","r") as f:

        file_content=f.read()
    


    return render(req,"os.html",{"content":file_content})