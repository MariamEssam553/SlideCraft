#Importing the libraries
import openai
import requests

# Set up your OpenAI API key
openai.api_key = 'sk-proj-TvxyJEp0VXWA0R9SGxfoT3BlbkFJpMSIRZXb5decwo7aEjBDcle'

def generate_image_from_text(sentence):
    response = openai.Image.create(
        prompt=sentence,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def save_image(image_url, file_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print("Failed to retrieve the image")
