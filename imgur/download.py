#This script downloads all of a user's favorite Imgur images to his/her local folder
import webbrowser
import pyimgur
import os
import credentials
import json
#set to 1 if you want to download images or just list
#TODO figure out how to get more than the first page

def get_cred():
    """ returns a dictionary of dictionaries that will
    give you access to the blocks in feste.json"""

    with open(os.environ['HOME'] + "/cred.json", 'r') as f:
        cfg = json.load(f)

    return cfg



def get_favorites():
    download=0
    cfg=get_cred()
    print cfg
    #Where imgur API keys should go
    CLIENT_ID = cfg['imgur']['client']
    CLIENT_SECRET = cfg['imgur']['secret']   # Needed for step 2 and 3

    im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
    #auth_url = im.authorization_url('pin')
    #webbrowser.open(auth_url)
    #pin = input("What is the pin? ") # Python 3x
    #pin = raw_input("What is the pin? ") # Python 2x
    pin=cfg['imgur']['pin']
    #get current user or specify which username you want
    user=cfg['imgur']['user']
    im_user=im.get_user(user)
    favorites=im_user.get_gallery_favorites()
    #returns a list of image objects (each val)
    for i, val in enumerate(favorites):
        fname=''
        if val.is_album==True:
            #get this album so we can then iterate through the images
            album=im.get_album(val.id)
            for image in album.images:
                print "album image: ",image.link
                fname="album_images/"+image.link.replace("http://i.imgur.com/","")
                if download==1 and file_exists(fname) is False:
                    image.download('album_images',image.link)
        else:
            #just image
            print "This is an image:",val.id
            fname="normal_images/"+val.link.replace("http://i.imgur.com/","")
            print "file name is ",fname
            if download==1 and file_exists(fname) is False:

                val.download('normal_images',val.link)

        print "count: ",i


def file_exists(fname):
    if os.path.isfile(fname):
        return True
    else:
        return False

get_favorites()