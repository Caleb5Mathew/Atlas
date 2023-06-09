import tkinter as tk
from PIL import Image, ImageTk
import os
import requests
from bs4 import BeautifulSoup


def display_images(image_folder):
    root = tk.Tk()
    root.title("Image Gallery")

    canvas_width = 500
    canvas_height = 500
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    x = 0
    y = 0
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    photo_images = []  # Store PhotoImage objects
    for filename in image_files:
        file_path = os.path.join(image_folder, filename)
        try:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            photo_images.append(photo)  # Store the PhotoImage object
            canvas.create_image(x, y, image=photo, anchor=tk.NW)
            x += 100
            if x >= canvas_width:
                x = 0
                y += 100
        except Exception as e:
            print(f"ERROR - Could not process {filename} - {e}")

    root.mainloop()



def fetch_and_display_images(query_word, max_images):
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # Fetch image URLs
    response = requests.get(search_url.format(q=query_word))
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')
    image_urls = [img['src'] for img in image_tags]

    # Create the target folder if it doesn't exist
    target_folder = "./images"
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Download and persist the images
    for i, url in enumerate(image_urls[:max_images]):
        try:
            image_content = requests.get(url).content
            file_path = os.path.join(target_folder, f"image_{i}.jpg")
            with open(file_path, 'wb') as f:
                f.write(image_content)
            print(f"SUCCESS - Saved {url} - as {file_path}")
        except Exception as e:
            print(f"ERROR - Could not download {url} - {e}")

    # Display the images
    display_images(target_folder)


# Prompt the user to enter a query word
query_word = input("Enter a query word: ")

# Set the maximum number of images to fetch
max_images = 40

# Fetch and display the images
fetch_and_display_images(query_word, max_images)