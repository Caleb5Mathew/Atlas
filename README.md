# Atlas
~A program used in order to derive images from Google Search in order to capture human perspective of inputted words
<pre>
In Order To Run:  
  -pip install tkinter
  -pip install pillow
  -pip install requests
  -pip install beautifulsoup4
  
  -python (file_name).py ~Atlas3.py if you don't touch anything~
  
  -Enter word to lookup

</pre>
<br />
<br />
~Coding Breakdown
Importing the Required Libraries:
The code begins by importing the necessary libraries:

   tkinter is used for creating the GUI and displaying the images.
   
   PIL (Python Imaging Library) is used for image processing and displaying images in Tkinter.
   
   os provides functionality for interacting with the operating system, such as creating directories and file paths.
    
   requests is used for sending HTTP requests to fetch the image URLs.
    
   BeautifulSoup is a library for web scraping and parsing HTML.
<br />
<br />
   
    
https://github.com/Caleb5Mathew/Atlas/blob/0e60b180ca00df5e7a90e17d34ea159391550b9a/Atlas3.py#L1-L5

<br />
<br />
Defining the display_images Function:
    The display_images function is responsible for creating a Tkinter window and displaying the images in a gallery format.<br /> It takes the image_folder parameter, which represents the path to the       folder where the images are stored.
<br />
<br />
https://github.com/Caleb5Mathew/Atlas/blob/0e60b180ca00df5e7a90e17d34ea159391550b9a/Atlas3.py#L8-L36

<br />
<br />
Defining the fetch_and_display_images Function:
    The fetch_and_display_images function takes two parameters: query_word, representing the keyword for image search, and max_images, representing the maximum number of images to fetch.

  Inside this function:

   The search_url variable is set to the Google Images search URL with a placeholder for the query word.<br />
    The code sends an HTTP GET request to the search URL using requests.get(), retrieves the response, and creates a BeautifulSoup object to parse the HTML content.<br />
    It finds all the img tags within the HTML using soup.find_all('img') and extracts the source URLs for the images.<br />
    It creates a target folder named "images" using os.makedirs() if it doesn't already exist.<br />
    The function iterates over the retrieved image URLs and downloads the images using requests.get(url).content. Each image is saved in the "images" folder with <br />
    a file name in the format "image_i.jpg", where i represents the index of the image.<br />
    The downloaded images are then displayed by calling the display_images function, passing the path of the target folder.<br />
<br />
<br />
https://github.com/Caleb5Mathew/Atlas/blob/0e60b180ca00df5e7a90e17d34ea159391550b9a/Atlas3.py#L39-L65
<br />
<br />

Prompting the User for Input:
    The program prompts the user to enter a query word, which is stored in the query_word variable.
<br />
<br />
https://github.com/Caleb5Mathew/Atlas/blob/0e60b180ca00df5e7a90e17d34ea159391550b9a/Atlas3.py#L68-L69
<br />
<br />

Setting the Maximum Number of Images:
    The maximum number of images to fetch is set to 40, stored in the max_images variable.
<br />
<br />
https://github.com/Caleb5Mathew/Atlas/blob/0e60b180ca00df5e7a90e17d34ea159391550b9a/Atlas3.py#L71-L72
<br />
<br />

Fetching and Displaying the Images:
    The fetch_and_display_images function is called, passing the query word and the maximum number of images as arguments.<br />
    That's the complete breakdown of the code. It prompts the user for a query word, fetches images from Google Images based on the query, downloads them, and then displays them in a Tkinter-based      image gallery.
<br />
<br />
https://github.com/Caleb5Mathew/Atlas/blob/0e60b180ca00df5e7a90e17d34ea159391550b9a/Atlas3.py#L74-L75
