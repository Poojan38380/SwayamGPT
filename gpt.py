from g4f.client import Client
import time



def run_gpt(question, GPT):

    client = Client()
    max_retries = 5
    backoff_factor = 1.5
    retry_delay = 5  # start with 1 second
    for i in range(max_retries):
        try:
            prompt = f"Can you please solve this question, there may/may not be multiple answers. {question['question_text']}."

            if "choices" in question and len(question["choices"]) > 0 and question["choices"] != "":

                if "image_urls" in question and len(question["image_urls"]) > 0:
                    prompt += f" And here are the choices to the question:    " +  ' , '.join([f'Choice {i+1}: {choice}' for i, choice in enumerate(question["choices"])]) + f"  . And here is the reference image url:  {question['image_urls'][0]} "

                else:
                    prompt += f" And here are the choices to the question:    " +  ' , '.join([f'Choice {i+1} : {choice}' for i, choice in enumerate(question["choices"])])

            else:

                if "image_urls" in question and len(question["image_urls"]) > 0:
                    prompt = f" And here is the reference image url: {question['image_urls'][0]} "      



            response = client.chat.completions.create(
                model= GPT, messages=[{"role": "user", "content": prompt}]
            )
            result = {
                "answer": f"Answer: {response.choices[0].message.content}",
            }
            return result
        except:
            print(f"Request failed, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= backoff_factor   

    return {
        "answer": f"Can't find the solution to this question as too many users are using the site right now",
    }
    

    
