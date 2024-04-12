from g4f.client import Client
import time


def run_prompt(prompt,GPT):
    
    
    client = Client()
    max_retries = 5
    backoff_factor = 1.5
    retry_delay = 5 

    for i in range(max_retries):
        try:    
            response = client.chat.completions.create(
                model=GPT,
                messages=[{"role": "user", "content": prompt }],
            
            )
            result = (response.choices[0].message.content)
            return result
        except:
            print(f"Request failed, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= backoff_factor   

    result = "Can't find the solution to this question as too many users are using the site right now"
    return result