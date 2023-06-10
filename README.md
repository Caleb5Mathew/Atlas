# Atlas
~A program used in order to derive images from Google Search in order to capture human perspective of inputted words 
<br />
<br />
<span style="color:red"> **Visit Atlas2 Branch for up to date (6/10/23) version of BS4 Webscraper implementation </span>
<pre>
In Order To Run:  
  ⁃Enter word to lookup  
  ⁃Type C or D for Compact and Disarrayed  
     -Compact: an arrangement of equal square pieces in rows and columns  
           -Refer to Compact_ex file  
     -Disarrayed: a piece that has random image sizes and random image placements 
      along the piece  
           -Refer to Dissarrayed_ex file  
</pre>
~Coding Breakdown
```diff
-Atlas Functions-
  
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
    ⁃Takes query (string), max links (int), wd, and time to rest between fetches (int), as input and gets the 
     urls of the thumbnails from the results of the search
    ⁃Ex. fetch_image_urls("nature", 40, wd, 10)
-persist_image_2-
    ⁃Takes folderpath (str), Image (str), and counter (int) as inputs and writes the url path in order to save the image
    ⁃Ex. persist_image_2('C://Users//ezekm//Downloads', 'https://tinyurl.com/bdhxtkkd', 2)
    *Note* persist_image_2 is not used in this project, it is only there in case of future changes in which the final 
     image is saved, not the fetched images
-persist_image-
    ⁃Takes folderpath (str), Image (str), and counter (int) as inputs and writes the url path in order to save the image
    ⁃Ex. persist_image_2('C://Users//ezekm//Downloads', 'https://tinyurl.com/bdhxtkkd', 2)    
-search_and_download-
    ⁃Takes query (string), driver location (str), download location (str), number of images to get (int)
    ⁃Ex. search_and_download('parrot',''Downloads//chromedriver_win32//chromedriver.exe' , './images', 32)


!Atlas Scheme!
    ⁃Atlas uses Selenium Chromedriver in order to fetch images for the query word. 
    ⁃NLTK is used to fetch synonyms and look-alikes for the query word and these outputs are stored
    ⁃images for the query word and it's synonyms is stored in images2 and if the synonym list length is below 6, the starting 
     query word is searched for and downloaded. The amount of "query searches" that is looked for is based off of the 
     synonym list length times 8 and that total number minus 50. 48 is the allowed pictures that is shown in the default 
     settings, but 50 allows room for 2 broken url links or unaccessable photos.
    ⁃Atlas then takes the images and uses requests to convert it to byte form. Then it converts 
     the bytes form to a readable PIL form and resizes the images
    ⁃Atlas then splits the list of images and creates a blank canvas, afterwards the items are pasted
     into rows and arranged symmetrically if compact or in a random array if disarrayed



