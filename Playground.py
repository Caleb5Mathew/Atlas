
import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import os
import time
import requests
from selenium import webdriver
from nltk.corpus import wordnet
import random

images3 = []
images = []
images2 = []

DRIVER_PATH = 'C://Users//ezekm//Downloads//chromedriver_win32//chromedriver.exe'
search_term = input('Enter Word Here: ')
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

search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

more_images5 = search_and_download(search_term, DRIVER_PATH, './images', 8)
images2.append(more_images5)
for item in images2:

    # Tinker to pillow converter to resize using pil but also utlize tinker to help with url readings switching to html
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
print(images3)
imgSmall = images3[0].resize((20, 20))

# Scale back up using NEAREST to original size
result = imgSmall.resize(images3[0].size, Image.NEAREST)

new_image = Image.new('RGB', (1000 , 1000))
new_image.paste(result, (200, 200 ))
new_image.show()
