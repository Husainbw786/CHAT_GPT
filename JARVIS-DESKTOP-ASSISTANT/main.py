import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
from config import apikey
import random

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Husain: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    #  with open(f"Openai/prompt- {random.randint(1, 78484627482)}") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)



def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ********************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
  #  print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
  #  with open(f"Openai/prompt- {random.randint(1, 78484627482)}") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"



if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am Jarvis")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],
                 ["chatgpt","https://chat.openai.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} ")
                webbrowser.open(site[1])
        if "the time" in query:
            curr_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {curr_time}")

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower() :
            chatStr = ""

        else:
            print("chatting")
            chat(query)



