# Atlas
~A program used in order to derive images from Google Search in order to capture human perspective of inputted words

```diff
-FUNCTIONS-
  
-resize_items-
    ⁃Takes image as input and returns a cropped version
    ⁃Ex. resize_images(Image)
    *Note*: Image is only cropped, not sized
-list_div-    
    ⁃Takes list as input and returns the list divided in 2
    ⁃Ex. list_div(listA)
    *Note* In this project, list_div is iterated to split the list into sections as needed by rows
-scroll_to_end-
    ⁃Takes webdriver(wb) as input and scrolls to the bottom of the webpage
    ⁃Ex. scroll_to_end(wd)
-fetch_image_urls-
    ⁃Takes query (string), max links (int), wd, and time to rest between fetches (int), as input and gets the urls of the thumbnails from the results of the search
    ⁃Ex. fetch_image_urls("nature", 40, wd, 10)
-persist_image_2-
    ⁃Takes folderpath (str), Image (str), and counter (int) as inputs and writes the url path in order to save the image
    ⁃Ex. persist_image_2('C://Users//ezekm//Downloads', 'https://tinyurl.com/bdhxtkkd', 2)
    *Note* persist_image_2 is not used in this project, it is only there in case of future changes in which the final image is saved, not the fetched images
-persist_image-
    ⁃Takes folderpath (str), Image (str), and counter (int) as inputs and writes the url path in order to save the image
    ⁃Ex. persist_image_2('C://Users//ezekm//Downloads', 'https://tinyurl.com/bdhxtkkd', 2)    
-search_and_download-
    ⁃Takes query (string), driver location (str), download location (str), number of images to get (int)
    ⁃Ex. search_and_download('parrot',''Downloads//chromedriver_win32//chromedriver.exe' , './images', 32)
