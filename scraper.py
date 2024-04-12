import requests
from bs4 import BeautifulSoup
import json


def scraper_function(url):


    #add your cookie header string in a .txt file and add it here
    with open(r"cookies/switching_linear.txt", "r") as file:
        # Read the contents of the file and strip any leading or trailing whitespace
        
        cookies = file.read().strip()

    # Replace these with the actual URL and cookie header string
    cookie_header = {"Cookie": cookies}

    # Use a session for connection re-use and efficiency

    with requests.Session() as session:
        # Send a GET request to the specified URL with the provided headers

        response = session.get(url, headers=cookie_header)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            response.encoding = "utf-8"
            soup = BeautifulSoup(response.text, "html.parser")
            
            
            
            for script in soup.find_all('script'):
                if script.get('type') == 'math/tex':
                    script.replace_with(script.text.strip())
            # Find all question divs
            question_divs = soup.find_all(
                "div", class_=["qt-mc-question", "qt-nm-question"]
            )

            # Initialize list to store questions
            questions = []

            for question_number, question_div in enumerate(question_divs, start=1):
                question_text = question_div.find("div", class_="qt-question").get_text()         

                img_tags = question_div.find("div", class_="qt-question").find_all(
                    "img"
                )
                image_urls = [img["src"] for img in img_tags if "src" in img.attrs]
                choices_div = question_div.find("div", class_="qt-choices")
                choices = (
                    [
                        label.text.strip().replace("\t", "")
                        for label in choices_div.find_all("label")
                    ]
                    if choices_div
                    else []
                )
                questions.append(
                    {
                        "question_number": question_number,
                        "question_text": question_text,
                        "choices": choices,
                        "image_urls": image_urls,
                    }
                )

            # with open("scraped_data.json", "w") as file:
            #     json.dump(questions, file, indent=4)

            return questions

        else:
            print(f"Failed to scrape {url}. Status code: {response.status_code}")
            return []


# scraper_function(
#     "https://onlinecourses.nptel.ac.in/noc24_cs03/unit?unit=106&assessment=107"
# )
