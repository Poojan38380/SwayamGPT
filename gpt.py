# from g4f.client import Client
# from flask import Flask, render_template



# def run_gpt(question, GPT):

#     client = Client()
#     if "choices" in question and len(question["choices"]) > 0 and question["choices"] != "":

#         if "image_urls" in question and len(question["image_urls"]) > 0:
#             prompt = f"Can you please solve this question. {question['question_text']}. And here are the choices to the question, Choices: {', '.join(question['choices'])}. And here is the reference image url: '{question['image_urls'][0]}' "
#         else:

#             prompt = f"Can you please solve this question. {question['question_text']}. And here are the choices to the question, Choices: {', '.join(question['choices'])}."
#     else:

#         if "image_urls" in question and len(question["image_urls"]) > 0:
#             prompt = f"Can you please solve this question. {question['question_text']}. And here is the reference image url: '{question['image_urls'][0]}' "      

#         else:
#             prompt = f"Can you please solve this question. {question['question_text']}."

#     response = client.chat.completions.create(
#         model= GPT, messages=[{"role": "user", "content": prompt}]
#     )
#     result = {
#         "question": f"Question {question['question_number']}: {prompt} ",
#         "answer": f"Answer: {response.choices[0].message.content}",
#     }
#     return result
    
# retry method with exponential            
# import time
# from g4f.client import Client

# def make_request_with_retry():
#     client = Client()
#     max_retries = 5
#     backoff_factor = 1.5
#     retry_delay = 1  # start with 1 second

#     for i in range(max_retries):
#         try:
#             response = client.chat.completions.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": "Hello"}],  # ... other parameters ...
#             )
#             return response.choices[0].message.content
#         except g4f.errors.RetryProviderError as e:
#             print(f"Request failed, retrying in {retry_delay} seconds...")
#             time.sleep(retry_delay)
#             retry_delay *= backoff_factor
#     raise Exception("Max retries reached, unable to complete the request")


# print(make_request_with_retry())






from g4f.client import Client
import time



def run_gpt(question, GPT):

    client = Client()
    max_retries = 5
    backoff_factor = 1.5
    retry_delay = 5  # start with 1 second
    for i in range(max_retries):
        try:
            if "choices" in question and len(question["choices"]) > 0 and question["choices"] != "":

                if "image_urls" in question and len(question["image_urls"]) > 0:
                    prompt = f"Can you please solve this question, there may/may not be multiple answers. {question['question_text']}. And here are the choices to the question:    " +  ' , '.join([f'Option {i+1}: {choice}' for i, choice in enumerate(question["choices"])]) + f"  . And here is the reference image url:  {question['image_urls'][0]} "
                else:

                    prompt = f"Can you please solve this question, there may/may not be multiple answers. {question['question_text']}. And here are the choices to the question:    " +  ' , '.join([f'Choice {i+1} : {choice}' for i, choice in enumerate(question["choices"])])
            else:

                if "image_urls" in question and len(question["image_urls"]) > 0:
                    prompt = f"Can you please solve this question, there may/may not be multiple answers. {question['question_text']}. And here is the reference image url: '{question['image_urls'][0]}' "      

                else:
                    prompt = f"Can you please solve this question, there may/may not be multiple answers. {question['question_text']}."

            response = client.chat.completions.create(
                model= GPT, messages=[{"role": "user", "content": prompt}]
            )
            result = {
                "question": f"Question {question['question_number']}: {prompt} ",
                "answer": f"Answer: {response.choices[0].message.content}",
            }
            return result
        except:
            print(f"Request failed, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= backoff_factor   

    result = {
        "question": f"Can't find the solution to this question as too many users are using the site right now",
        "answer": f"Can't find the solution to this question as too many users are using the site right now",
    }
    return result

    
