from tkinter import *
import PIL.ImageTk
import PIL.Image  
from instagramy import InstagramUser
import urllib.request
import cv2
session_id='49579652208%3A0Ai6EUM1flNtBS%3A28'



def displayprofilepicture():
    name=username.get()
    try: 
        user=InstagramUser(name,sessionid=session_id)
        profilepictureurl=user.profile_picture_url
        urllib.request.urlretrieve(profilepictureurl, ("profilephotos/%s.jpg" %username))
        cv2.imshow("image",cv2.imread("profilephotos/.!entry.jpg"))
    except:
        print("incorrect username")
        


    
master = Tk()
Label(master, text='Username').grid(row=0,column=0)
username= Entry(master)
username.grid(row=0,column=1)
submitbutton=Button(master,text="Submit",width=10,command=displayprofilepicture).grid(row=1,column=1)
master.mainloop()

