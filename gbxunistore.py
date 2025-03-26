build = "gba" # or set it to "gba"

#for managing jsons
import json

#to get extensions from a filename
from pathlib import Path

#for urlencode (because of spaces)
import urllib.parse

#for thumbnail (icon) creation
from PIL import Image
import matplotlib.pyplot as plt

# import date class from datetime module for today
from datetime import date

#load the revison, to increment it
file = open("revision.txt", "r")
revision = int(file.read())
file.close()
print("(i) Last revision: " + str(revision))
revision += 1
print("(i) This revision: " + str(revision))

#store the inceremented revison number
file = open("revision.txt", "w")
file.write(str(revision))
file.close()

#setting default paths and other constanst
nl = "\n"
if build == "gb":
   storebaseurl = "https://raw.githubusercontent.com/vargaviktor/database-unistore/master/"
   baseurl = "https://raw.githubusercontent.com/vargaviktor/database-unistore/master/entries/"
   rombase = "/roms/gb/"
   t3sfile = "gb.t3s"
   t3xfile = "gb.t3x"
   storefajl = "gb.unistore"    
else:
   storebaseurl = "https://raw.githubusercontent.com/vargaviktor/games-unistore/master/"
   baseurl = "https://raw.githubusercontent.com/vargaviktor/games-unistore/master/entries/"
   rombase = "/roms/gba/"
   t3sfile = "gba.t3s"
   t3xfile = "gba.t3x"
   storefajl = "gba.unistore"    

defaultdate = "2001-01-01"
gbt3sfirstline = "--atlas -f rgba -z auto"
icon_index = 1
numofgames = 1
noicon = "000.png"
allgamejson = [] 

#store the first line of gbx.t3s
#and the second line with for icon zero as "no icon" icon
gbt3s = open("./iconversion/" + t3sfile , "w")
gbt3s.write(gbt3sfirstline + nl)
gbt3s.write(noicon+nl)

if build == "gb":
   storeinfo = {
        "title": "Homebrew Hub GB(C) DB" ,
        "author": "https://hh.gbdev.io (+ vargaviktor)",
	#                #######################################################
        "description": 	"Homebrew Hub is a community-led initiative to collect," + nl +
			"archive and preserve homebrew and demoscene software" + nl +
			"developed for Game Boy (Color), Game Boy Advance and" + nl + 
			"NES. In this database you can browse GB(C) homebrews" + nl +
			"published on the site: https://hh.gbdev.io " + nl + nl +
			"Converter made by vargaviktor" + nl +
			"Created on " + str(date.today()) ,
        "url": storebaseurl + storefajl,
        "file": storefajl,
        "sheetURL": storebaseurl + t3xfile,
        "sheet": t3xfile ,
        "bg_index": 0,
        "bg_sheet": 0,
        "revision": revision,
        "version": 3
	    }
else:
   storeinfo = {
        "title": "Homebrew Hub GBA DB" ,
        "author": "https://gbadev.org/ (+ vargaviktor)",
        #                #######################################################
        "description":  "Homebrew Hub is a community-led initiative to collect," + nl +
                        "archive and preserve homebrew and demoscene software" + nl +
                        "developed for Game Boy (Color), Game Boy Advance and" + nl +
                        "NES. In this database you can browse GBA homebrews" + nl +
                        "published on the site: https://gbadev.org/" + nl + nl +
                        "Converter made by vargaviktor" + nl +
                        "Created on " + str(date.today()) ,
        "url": storebaseurl + storefajl,
        "file": storefajl,
        "sheetURL": storebaseurl + t3xfile,
        "sheet": t3xfile ,
        "bg_index": 0,
        "bg_sheet": 0,
        "revision": revision,
        "version": 3
	    } 
  
#ide masolni a masik jsont

# Open the file in read mode
with open('jsondirlist.txt', 'r') as listafile:
    # Read each line in the file
    for fileline in listafile:
        fileline = "./" + fileline.replace("\n", "") 
        #print(fileline.strip())

        #clearing releasenotes
        releasenotes = ""

        #import the game.json
        actualjsonpath = fileline + "game.json"

        with open(actualjsonpath) as fajl:
            inp = json.load(fajl)

        #reading game.json values to variables
        print(" ---- EXTRACTION ----")
        print("(i) Extraction of game.json started")

        #developer can be a string or a list, or developer object
        if "developer" in inp:
            author = inp["developer"]
            #if it is a single string then we have it now
            if isinstance(author, list):
                print(type(author))
                try:
                   authorstr = str(', '.join(author))
                   # if it is succesfull, it was a multistrign
                except TypeError:
                   # if typeerror this a developer structure 
                   # we need to extract the name item from this dict
                   print("Typerror, this is an object")
                except:
                   print("If we are here I dont know WFT happened. :)")
                
                author = authorstr
                print ("(i) Multiple author: " + author)
            else:
                print("(i) Single author: " + author)
                #the string is there, nothing to do

        else:
            print("(w) Developer - Key doesn't exist in JSON data")
            author = "(not known)"

        if "typetag" in inp:
            category = inp["typetag"]
        else:
            print("(w) Typetag - Key doesn't exist in JSON data")
            category = "(not set)"

        if "platform" in inp:
            console = inp["platform"]
        else:
            print("(w) Platform - Key doesn't exist in JSON data")
            console = "(not set)"

        if "slug" in inp:
            slug = inp["slug"]
        else:
            print("(w) Slug - Key doesn't exist in JSON data")

        if "description" in inp:
            description = inp["description"]
        else:
            print("(w) Description - Key doesn't exist in JSON data")
            description = ""

        if "tags" in inp:
            tags = "Tags: " + ', '.join(inp["tags"])
        else:
            print("(w) Tags - Key doesn't exist in JSON data")
            tags = ""

        #extend tags with typetag - disabled
        #if "typetag" in inp:
        #    if tags != "":
        #        tags = tags + ", "
        #    tags = tags + ', '.join(inp["tags"])
        #else:
        #    print("(w) Typetag - Key doesn't exist in JSON data")

        #adding tags to the descrition
        if (description != "") and (tags != ""):
            description = description + nl + tags
        elif (description == "") and (tags != ""):
            description = tags
        else:
            print("(w) Description was not extended with tags")

        if "website" in inp:
            website = inp["website"]
        else:
            print("(w) Website - Key doesn't exist in JSON data")
            website = ""

        #adding website to the description
        if (description != "") and (website != ""):
            description = description + nl + website
        elif (description == "") and (website != ""):
            description = website
        else:
            print("(w) Description was not extended with website")

        #if description longer than 270 char, then copy to releasenotes, then cut description
        if len(description)>270:
           releasenotes = description
           description = description[:270] + "..." + nl + "See release notes..." 

        if "license" in inp:
            license = inp["license"]
        elif "gameLicense" in inp:
            license = inp["gameLicense"]
        else:
            print("(w) License, gameLicense  - Key doesn't exist in JSON data")
            license = "(not set)"

        if "date" in inp:
            last_updated = inp["date"]
        else:
            print("(w) Date - Key doesn't exist in JSON data, using default date: " + defaultdate)
            last_updated = defaultdate # set to dafault if not set

        if "title" in inp:
            title = inp["title"]
        else:
            print("(w) Title - Key doesn't exist in JSON data")

        #extracting the 'files' list's zero item (the only one element)
        #then dumping that json structured element as json element, to have " around the keys (list doesnot does that)
        #then loading back that json element as dict, to find dinali the filename

        version = "(not set)" # set to default


        if "files" in inp:
            #find files in json
            fajloklst = inp["files"]

            #extract zero item from list
            if fajloklst:
                lstoneitem=fajloklst[0]

                #convert that subjson to dict
                fajlokjson = json.loads(json.dumps(lstoneitem))

                if "filename" in fajlokjson:
                    filename = fajlokjson["filename"]

                if "version" in fajlokjson:
                    version = fajlokjson["version"]
                    #if there is a version, use that
            else: 
                print("(w) No attached file.")
        else:
            print("(w) Files key doesn't exist in JSON data")
            
        extension = Path(filename).suffix

        print("------- SUMMARY --------")
        print("(i) Converted file#" + str(numofgames))
        print("(i) Converted JSON: " + actualjsonpath)
        print("(i) Title       :" + title)
        print("(i) Author      :" + author)
        print("(i) Category    :" + category)
        print("(i) Console     :" + console)
        print("(i) Extended description :")
        print(description)

        print("(i) Iconindex :" + str(icon_index))
        print("(i) Last upd. :" + last_updated)
        print("(i) License   :" + license)
        print("(i) Version   :" + version)

        #extract screenshots
        screenshots = inp["screenshots"]
        if not screenshots:
           print("(i) No screenshot, nothing to convert to icon.")
        else:
            numshots = len(screenshots)
            print("(i) Number of screenshots: " + str(numshots))
            sstitle = [""] * numshots
            ssall = [] 
            for x in range(numshots):
               sstitle [x]=(Path(screenshots[x]).stem).upper().replace("-", " ").replace("_", " ")
               print ("(i) Screenshot: " + sstitle[x] + " -- " + screenshots[x])
               ssjson = {
                   "description":sstitle[x],
                   "url":(baseurl + slug + "/" + screenshots[x])
                   }
               ssall.append(ssjson)

        #creating a 48x48 (or smaller) thumbnail in png format from the first image
        #also adding to the gb.t3s to create the t3x later based on that
        # but only when we have screenshots
        if screenshots:
           inputpath = "./entries/" + slug + "/" + screenshots[0]
           img = Image.open(inputpath)
           iconsize = (48,48)
           img.thumbnail(iconsize)
           outputpath = "./iconversion/" + slug + ".png"
           try:
              img.save(outputpath)
              #if succesfull, then ok
           except:
              #if it was not succesful we try the next one screen
              inputpath = "./entries/" + slug + "/" + screenshots[1]
              img = Image.open(inputpath)
              iconsize = (48,48)
              img.thumbnail(iconsize)
              outputpath = "./iconversion/" + slug + ".png"
            
           gbt3s.write(slug + ".png" + nl)

        #creating the game info structure (with screenshots)
        if screenshots:
            gamejson = {
                    "info":{
                    "author":author,
                    "category":[category],
                    "console":[console],
                    "description":description,
                    "icon_index":icon_index,
                    "last updated":last_updated,
                    "license":license,
                    "title":title,
                    "version":version,
                    "releasenotes":releasenotes,
                    "screenshots":ssall
                    },
                    "Download": [
                            {
                            "type": "downloadFile",
                            "file": baseurl +slug + "/" + urllib.parse.quote(filename),
                            "output": rombase + slug + extension
                            }
                            ]
                      }
        else:
            icon_index -= 1
            gamejson = {
                    "info":{
                    "author":author,
                    "category":[category],
                    "console":[console],
                    "description":description,
                    "icon_index": 0,
                    "last updated":last_updated,
                    "license":license,
                    "title":title,
                    "version":version,
                    "releasenotes":releasenotes
                    },
                    "Download": [
                            {
                            "type": "downloadFile",
                            "file": baseurl +slug + "/" + urllib.parse.quote(filename),
                            "output": rombase + slug + extension
                            }
                            ]
                      }
        if not fajloklst:
            gamejson = {
                    "info":{
                    "author":author,
                    "category":[category],
                    "console":[console],
                    "description":description,
                    "icon_index":icon_index,
                    "last updated":last_updated,
                    "license":license,
                    "title":title,
                    "version":version,
                    "releasenotes":releasenotes,
                    "screenshots":ssall
                           }
                       }

        if screenshots: 
             icon_index += 1
        numofgames += 1
        allgamejson.append(gamejson)
#these shall be outside the cycle

numofgames -= 1
print("----------------------")
print("(i) Conversion of finished, number of converted games: " + str(numofgames))
        
#the second is just test.
storejson = {
	"storeInfo":storeinfo,
	"storeContent":allgamejson
	    }


#print ("(i) Dumping the final JSON to screen:")
#print(json.dumps(storejson,indent=2, ensure_ascii=False))

#save the json to unistore file
with open(storefajl, 'w', encoding='utf-8') as storefile:
    json.dump(storejson, storefile, ensure_ascii=False, indent=4)
print("(i) Game JSON writen to " + storefajl + " file.")

gbt3s.close()
