# SwayamGPT

Made to solve the assignments of Swayam Courses on National Programme on Technology Enhanced Learning(NPTEL) via premium LLMs like GPT-4 and GPT-4-TURBO. On every wednesday, everyone in our batch in our college starts to worry about the solutions of Swayam Courses assignments... and after getting less than half of total points in most assignments when solving the questions via free LLMs like GPT3.5 and Copilot, I got struck with the idea of this project.

Most [Institutions of National Importance in India](https://www.education.gov.in/institutions-national-importance) provides the students a way of getting extra credits via [Swayam Online Courses](https://onlinecourses.nptel.ac.in), and most of the students, if not all... study just one week before the final examinations. But every week, we get an assignment to solve, which has to be submitted before 11:59PM on Wednesday. That made me think... Why not make an app that solves the assignment automatically???

Here comes SwayamGPT into the frame!
With the power of GPT-4-TURBO and GPT-4, swayamGPT asks the user only for the assignment url and BOOM... one by one, the screen fills up with the most accurate answers of the assignment.

(There is also an added functionality to use premium GPTs for free.)

## Run Locally

Create a python virtual environment(optional)

<!--
Create a virtual python environment(optional)

```bash
    python -m venv name_of_virtual_environment
```

Run this command in a terminal with administrator privileges

```bash
    name_of_virtual_environment\Scripts\activate
``` -->

Clone the project

```bash
    git clone https://github.com/Poojan38380/SwayamGPT
```

Go to the project directory

```bash
    cd swayamGPT
```

Install dependencies

```bash
    pip install -r requirements.txt
```

Start the server

```bash
flask run --port=8080
```
--reload: Automatically reloads the Flask application when changes are detected in the source files. This is very useful during development as it saves you from manually restarting the server every time you make changes to your code.

If you want to automatically reload the server, then use the below command instead
```bash
flask run --reload --port=8080
```



## How it works

### Grabbing the url and storing the Scraped Data

```javascript
var url = document.getElementById("urlInput").value;
$.ajax({
  type: "POST",
  url: "/swayamGPT/scrape",
  data: { url: url },
  success: function (response) {
    storeQuestions(response);
    getResult();
    // displayQuestions(response);
  },
});
```

This code sends the entered url to /swayamGPT/scrape where the data from the url is scraped from the page without the need to log in to Swayam site.

The returned questions, along with the choices and image url are stored in the session storage.

### Sending each question to GPT and getting the response

```javascript
function getResult() {
  var questions = JSON.parse(sessionStorage.getItem("questionsData"));
  var index = 0;
  processQuestion(index, questions);
}

function processQuestion(index, questions) {
  var selectedOption = document.getElementById("gptoptions").value; // Retrieve selected option value
  if (index >= questions.length) {
    return;
  }
  displayQuestionNumber(index, selectedOption);
  var question = questions[index];

  $.ajax({
    type: "POST",
    url: "/swayamGPT/process_question",
    data: JSON.stringify({
      question: question,
      selectedOption: selectedOption,
    }), // Include selected option in data object
    contentType: "application/json",
    success: function (response) {
      displayResult(response, function () {
        processQuestion(index + 1, questions);
      });
    },
  });
}
```

This code grabs the data from the session storage and sends each question to the LLM model selected by the user and grabs the response from the GPT.

## Features

- ### Scraping with cookies, so that there is no need to login to [Swayam Course Site](https://onlinecourses.nptel.ac.in)

```python
    #add your cookie header string in a .txt file and add it here
    with open(r"cookies/switching_linear.txt", "r") as file:
        # Read the contents of the file and strip any leading or trailing whitespace

        cookies = file.read().strip()

    # Replace these with the actual URL and cookie header string
    cookie_header = {"Cookie": cookies}
```

Make sure to view scraper.py once to understand the complications of scraping a webpage that uses mathematical symbols in data

```python
            for script in soup.find_all('script'):
                if script.get('type') == 'math/tex':
                    script.replace_with(script.text.strip())
```

This code make sure to not ignore the mathematical symbols

- ### Using BACKOFF RELOADING to make sure that user gets the response if there are too many requests on the GPT models

```python
    max_retries = 5
    backoff_factor = 1.5
    retry_delay = 5
    for i in range(max_retries):
        try:
            #Code here
            return result
        except:
            print(f"Request failed, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= backoff_factor
```

Backoff reloading makes sure that requests are sent to GPT models in exponential times if it faces error like "Too many requests"

- Premium models like GPT-4 and GPT-4-TURBO also accepts image urls as input. Questions with images are also solved accurately with this feature.
- Results gets displayed on the same page one after other so that user can see live progress
- Usage of cookies, so that user doesn't have to log in to the [onlinecourses.nptel.ac.in site](https://onlinecourses.nptel.ac.in)
- Choose from premium LLMs like GPT-4, GPT-4-TURBO, GPT-3.5-TURBO and GPT-3.5 to solve the assignment
- Also get access to the premium LLMs for free
- Play small games while you wait for the solutions :)

<h2>💻 Built with</h2>

Technologies used in the project:

- Python
- AJAX
- HTML
- CSS
- Flask
- Javascript

## Authors

- [@Poojan38380](https://github.com/Poojan38380)

## Feedback

If you have any feedback, please reach out to us at poojangoyani@gmail.com
