from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

Background = ["Background1", "Background2", "Background3", "Background4","Background5"] 
Background_weights = [20, 30 , 10, 30,10]

face = ["White", "Black","Alien"] 
face_weights = [40, 40,20]


eyes = ["Trippy", "Sunglasses", "Regular", "Ninjastyle", "Cartoony"] 
eyes_weights = [20, 20, 40, 10, 10]

Shirts= ["Red","Navy","Purple"]
shirt_weights = [33,33,33]

mouth = ["Regular", "Pirate", "Closed"]
mouth_weights = [80,10,10]

nose = ["Snot", "Regular","Clown","IRL"]
nose_weights = [20, 40,20,20]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
Background_files = {
    "Background1": "Background1",
    "Background2": "Background2",
    "Background3": "Background3",
    "Background4": "Background4",
    "Background5":"Background5"
}

face_files = {
    "White": "Face1",
    "Black": "Face2",
    "Alien": "Face3"
}

eyes_files = {
    "Trippy": "eyes1",
    "Sunglasses": "eyes2",
    "Regular": "eyes3",
   "Ninjastyle": "eyes4",
    "Cartoony": "eyes5"     
}

Shirt_files = {
 "Red" : "Shirt1",
 "Navy" : "Shirt2",
 "Purple" : "Shirt3"
}

mouth_files = {
    "Regular": "Mouth1",
    "Pirate": "Mouth2",
    "Closed": "Mouth3",

}
nose = ["Snot", "Regular","Clown","IRL"]
nose_files = {
    "Snot": "Nose1",
    "Regular": "Nose2",
    "Clown" : "Nose3",
    "IRL" : "Nose4"   
}

## Generate Traits

TOTAL_IMAGES = 1000 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(Background, Background_weights)[0]
    new_image ["Face"] = random.choices(face, face_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Shirt"] = random.choices(Shirts, shirt_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
   
#print(all_images)

# Get Trait Counts

Background_count = {}
for item in Background:
    Background_count[item] = 0

face_count = {}
for item in face:
    face_count[item] = 0
    

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
    
Shirt_count = {}
for item in Shirts:
    Shirt_count[item] = 0
    
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0
    
nose_count = {}
for item in nose:
    nose_count[item] = 0

for image in all_images:
    Background_count[image["Background"]] += 1
    face_count[image["Face"]] += 1
    eyes_count[image["Eyes"]] += 1
    Shirt_count[image["Shirt"]] += 1
    mouth_count[image["Mouth"]] += 1
    nose_count[image["Nose"]] += 1
    
#print(face_count)
#print(ears_count)
#print(eyes_count)
#print(hair_count)
#print(mouth_count)
#print(nose_count)

#### Generate Images

os.mkdir(f'./images')

for item in all_images:

    im1 = Image.open(f'./Pictures/Backgrounds/{Background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./Pictures/Faces/{face_files[item["Face"]]}.png').convert('RGBA')
    im3 = Image.open(f'./Pictures/Eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im4 = Image.open(f'./Pictures/Shirts/{Shirt_files[item["Shirt"]]}.png').convert('RGBA')
    im5 = Image.open(f'./Pictures/Mouths/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./Pictures/Noses/{nose_files[item["Nose"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)   

    #Convert to RGB
    rgb_im = com5.convert('RGB')
    file_name ="Kryptobjørn #" + str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
    
 #### Generate Metadata for all Traits 
os.mkdir(f'./metadata')

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)