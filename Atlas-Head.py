
import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import os
import time
import requests
from selenium import webdriver
from nltk.corpus import wordnet
import random

images2 = []
synonyms = []
images = []

#FUNCTIONS#

def resize_images(item):
    item = item((400, 400))
    return item
def list_div(list):
    length = len(list)
    split_length = length / 2
    return list[:split_length], list[split_length:]
def fetch_image_urls(query: str, max_links_to_fetch: 8, wd: webdriver, sleep_between_interactions: int = 8):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

        for img in thumbnail_results[results_start:number_results]:
            # click thumbnail to get image source
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            #Fetch the actual URLS
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))
                    print(image_urls)


            image_count = len(image_urls)

            #Output for URL fetch success
            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)
        #Add urls to a list to use in order to make them readable, resize them, and open them
        images.append(image_urls)




    return image_urls


def persist_image2(folder_path:str,new_image, counter):
    try:
        image_content = new_image.content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        f = open(os.path.join(folder_path, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
        f.write(image_content)
        f.close()
        print(f"SUCCESS - saved {url} - as {folder_path}")
        #Save and establish a path to the url
        images2.append(url)
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

def persist_image(folder_path:str,url:str, counter):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        f = open(os.path.join(folder_path, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
        f.write(image_content)
        f.close()
        print(f"SUCCESS - saved {url} - as {folder_path}")
        #Save and establish a path to the url
        images2.append(url)
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

def search_and_download(search_term: str, driver_path: str, target_path='./images', number_images=8):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))
    #Establish a path
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

    counter = 0
    for elem in res:
        persist_image(target_folder, elem, counter)
        counter += 1
DRIVER_PATH = 'C://Users//ezekm//Downloads//chromedriver_win32//chromedriver.exe'
search_term = input('Enter Word Here: ')


#Fetch URLS for the query word
query_images = search_and_download(search_term, DRIVER_PATH, './images', 8)
images2.append(query_images)

#Fetch Synonyms for the query word
for syn in wordnet.synsets(search_term):
    for l in syn.lemmas():
        synonyms.append(l.name())
    for item in synonyms:
        if synonyms.count(item) > 1:
            synonyms.remove(item)
#For synonyms[0-5] fetch urls by inserting the synonyms as a query word
try:
    more_images = search_and_download(synonyms[1], DRIVER_PATH, './images', 8)
    images2.append(more_images)
except:
    pass
try:
    more_images1 = search_and_download(synonyms[2], DRIVER_PATH, './images', 8)
    images2.append(more_images1)
except:
    pass

try:
    more_images2 = search_and_download(synonyms[3], DRIVER_PATH, './images', 8)
    images2.append(more_images2)
except:
    pass

try:
    more_images3 = search_and_download(synonyms[4], DRIVER_PATH, './images', 8)
    images2.append(more_images3)
except:
    pass

try:
    more_images4 = search_and_download(synonyms[5], DRIVER_PATH, './images', 8)
    images2.append(more_images4)
except:
    pass

try:
    more_images5 = search_and_download(synonyms[6], DRIVER_PATH, './images', 8)
    images2.append(more_images5)
except:
    pass

#50 is the image count, 48 is the allowed images with the default presets
#The reasoning behind the 2 difference is to allow room for faulty links that is addressed with the except line in the fetch area
if len(images2) < 50:
    diff = 50 - len(images2)
    try:
        query_images = search_and_download(search_term, DRIVER_PATH, './images', diff)
        images2.append(query_images)
    except:
        pass

#Uncomment this section if you use reddit-fetch but that takes longer and isn't as direct as using PIL and tinker
#you'd also have to assign every single picture a value so that would be pretty annoying

#image1 = images_fetch[0]
#image2  = images_fetch[1]
#image3 = images_fetch[2]
#image4 = images_fetch[3]
#image5 = images_fetch[4]
#image6 = images_fetch[5]
#image7 = images_fetch[6]
#image8 = images_fetch[7]


#Compact is a defined along with Disarrayed in the GIT Intro
pic_type = input('Type "C" for a compact picture, or type "D" for a disarrayed picture ')
if str(pic_type) == 'C':
    size_v = []
    sized = []

    images3 = []


    for item in images2:

        #Tinker to pillow converter to resize using pil but also utlize tinker to help with url readings switching to html
        window = tkinter.Tk()

        url = item

        try:
            r = requests.get(url)

            pilImage = Image.open(BytesIO(r.content))
            pilImage.mode = 'RGB'
            pilImage.save('new.png')
            new = pilImage.resize((400, 400))
            new.save('400_new.png')

            image = ImageTk.PhotoImage(pilImage)

            label = tkinter.Label(image=image)
            label.pack()

            images3.append(new)
        except:
            pilImage = None



    for item in images3:
        item_size = item.size
        size_v.append(item_size)
        sized.append(item)

    #Create the "blank canvas
    new_image = Image.new('RGB', (6 * 400 + 400, 8 * 400 + 1000))
    v_factor = 0
    v_factor1 = 0
    v_factor2 = 0
    v_factor3 = 0
    v_factor4 = 0
    v_factor5 = 0
    v_factor6 = 0
    v_factor7 = 0
    sized_11 = sized[0:8]
    sized_21 = sized[8:16]
    sized_12 = sized[16:24]
    sized_22 = sized[24:32]
    sized_13 = sized[32:41]
    sized_23 = sized[41:50]
    sized_14 = sized[48:56]
    sized_24 = sized[56:64]

#There are more than 8 section of pasting, default settings is 5 Vertical rows but to access all 8/make more, change new.image dimensions
    for item in sized_11:
        #Row 1 (V)
        new_image.paste(item, (200, 200+v_factor))
        v_factor += 400
    for item in sized_12:
        #Row 2 (V)
        new_image.paste(item, (200+400,200+ v_factor1))
        v_factor1 += 400
    for item in sized_21:
        #Row 3 (V)
        new_image.paste(item, (200+800, 200+v_factor2))
        v_factor2 += 400
    for item in sized_22:
        #Row 4 (V)
        new_image.paste(item, (200+1200, 200+v_factor3))
        v_factor3 += 400
    for item in sized_13:
        #Row 5 (V)
        new_image.paste(item, (200+1600, 200+v_factor4))
        v_factor4 += 400
    for item in sized_23:
        #Row 6 (V)
        new_image.paste(item, (200+2000, 200+v_factor5))
        v_factor5 += 400
    #for item in sized_14:
        #Row 7 (V)
        #new_image.paste(item, (200+2400, 200+v_factor6))
        #v_factor6 += 400
    #for item in sized_24:
        #Row 8 (V)
        #new_image.paste(item, (200+2800, 200+v_factor7))
        #v_factor7 += 400


    final_compact = new_image
    final_compact.show()

elif  str(pic_type) == 'D':
    size_v = []
    sized = []

    images3 = []

    for item in images2:

        window = tkinter.Tk()

        url = item

        try:
            r = requests.get(url)

            pilImage = Image.open(BytesIO(r.content))
            pilImage.mode = 'RGB'
            pilImage.save('new.png')

            image = ImageTk.PhotoImage(pilImage)

            label = tkinter.Label(image=image)
            label.pack()

            sized.append(pilImage)
        except:
            pilImage = None

        # Create the "blank canvas
    new_image = Image.new('RGB', (6 * 400 , 8 * 400))
    v_factor = random.randint(0,50)
    v_factor1 = 0
    v_factor2 = random.randint(0,50)
    v_factor3 = random.randint(0,50)
    v_factor4 = 0
    v_factor5 = 0
    v_factor6 = random.randint(0,50)
    v_factor7 = 0
    sized_11 = sized[0:8]
    sized_21 = sized[8:16]
    sized_12 = sized[16:24]
    sized_22 = sized[24:32]
    sized_13 = sized[32:40]
    sized_23 = sized[40:48]
    sized_14 = sized[48:56]
    sized_24 = sized[56:64]

    # There are more than 8 section of pasting, default settings is 5 Vertical rows but to access all 8/make more, change new.image dimensions
    for item in sized_11:
        # Row 1 (V)
        new_image.paste(item, (0, v_factor))
        v_factor += random.randint(150,500)
    for item in sized_12:
        # Row 2 (V)
        new_image.paste(item, (random.randint(300,500),  v_factor1))
        v_factor1 += random.randint(150,500)
    for item in sized_21:
        # Row 3 (V)
        new_image.paste(item, (random.randint(700,900), v_factor2))
        v_factor2 += random.randint(150,500)
    for item in sized_22:
        # Row 4 (V)
        new_image.paste(item, (random.randint(1100,1300), v_factor3))
        v_factor3 += random.randint(150,500)
    for item in sized_13:
        # Row 5 (V)
        new_image.paste(item, (random.randint(1500,1700), v_factor4))
        v_factor4 += random.randint(150,500)
    for item in sized_23:
        # Row 6 (V)
        new_image.paste(item, (random.randint(1900,2100), v_factor5))
        v_factor5 += random.randint(150,500)
    for item in sized_14:
        # Row 7 (V)
        new_image.paste(item, (random.randint(2300,2500), v_factor6))
        v_factor6 += random.randint(150,500)
    for item in sized_24:
        # Row 8 (V)
        new_image.paste(item, (random.randint(2700,2900), v_factor7))
        v_factor7 += random.randint(150,500)
    new_image.save('final.png')
    new_image.show()
####learn how to download a image and save it as a file in your computer and put it below

####learn how to download a image and save it as a file in your computer and put it below

print(len(images2))