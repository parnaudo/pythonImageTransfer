#This script downloads all of a user's favorite Imgur images to his/her local folder
import webbrowser

import pyimgur
#set to 1 if you want to download images or just list
#TODO figure out how to get more than the first page
download=0
#Where imgur API keys should go
CLIENT_ID = ""
CLIENT_SECRET = ""   # Needed for step 2 and 3

im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
auth_url = im.authorization_url('pin')

webbrowser.open(auth_url)
#pin = input("What is the pin? ") # Python 3x
pin = raw_input("What is the pin? ") # Python 2x
#get current user or specify which username you want
im_user=im.get_user()
favorites=im_user.get_gallery_favorites()
#returns a list of image objects (each val)
for i, val in enumerate(favorites):
    if val.is_album==True:
        #get this album so we can then iterate through the images
        album=im.get_album(val.id)
        for image in album.images:
            print "album image: ",image.link
            if download==1:
                image.download('album_images',image.title)
    else:
        #just image
        print "This is an image:",val.link
        if download==1:
            val.download('normal_images',val.title)
    print "count: ",i

