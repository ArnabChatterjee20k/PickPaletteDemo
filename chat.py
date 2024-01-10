import os
from langchain_core.prompts import ChatPromptTemplate
os.environ["GOOGLE_API_KEY"] = "AIzaSyBrRcLffeRKKOChBjlnxJS_Wo6eSZ0x44s"
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
def chat(description):
  model = ChatGoogleGenerativeAI(model="gemini-pro")

  prompt = ChatPromptTemplate.from_template(""" I am giving you a json of data.
        "description": "Check out logos designed by AI every time you click the generate button or refresh the page.",
        "title": "There is a LOGO for that - Product Information, Latest Updates, and Reviews 2024 | Product Hunt",
        "palette": [
          "#2c2d3f",
          "#b55a5e",
          "#f1f7f7",
          "#91afc4",
          "#4c6bc6",
          "#5dacdb",
          "#d09e4b",
          "#d0a199",
          "#f0cba4",
          "#c0dee7"
        ]
      
        "description": "FlowGPT: Share, discover, and learn about the most useful ChatGPT prompts that help you streamline your tasks and increase productivity.",
        "title": "Fast & Free AI & GPTs Bots store | FlowGPT",
        "palette": [
          "#3f231d",
          "#bcc4d4",
          "#76402f",
          "#b27c4c",
          "#f4f2f6",
          "#d7b383",
          "#7388be",
          "#a4818b",
          "#c9b4a1",
          "#bfedf8"
        ]
      
        "description": "FlowGPT: Share, discover, and learn about the most useful ChatGPT prompts that help you streamline your tasks and increase productivity.",
        "title": "Fast & Free AI & GPTs Bots store | FlowGPT",
        "palette": [
          "#d8dce5",
          "#462720",
          "#894d37",
          "#b78550",
          "#dfbe8e",
          "#7a8dc8",
          "#b7918d",
          "#5a9ce1",
          "#a4d6e8",
          "#c1aebb"
        ]
      
        "description": "Calendar Review creates a year-end review of your Google Calendar and gives you insights on how much time you spent on meetings in 2022, your most attended meeting, longest meetings, etc. It helps you reflect back on how you spent your time in meetings in the year 2022.",
        "title": "Calendar Review — 2023",
        "palette": [
          "#f2eae5",
          "#f48f5d",
          "#4e518f",
          "#ec6e6a",
          "#eeba9c",
          "#e9a78b",
          "#9f9fa0",
          "#f3b5b4",
          "#bbbbbe",
          "#72747d"
        ]
      
        "description": "Join other founders and get weekly, curated startup design & growth insight delivered straight to your inbox.",
        "title": "Designing Growth | Weekly Design & Growth Insight",
        "palette": [
          "#151515",
          "#ebebe3",
          "#646fe1",
          "#61d4e5",
          "#f2d276",
          "#c09b58",
          "#88582e",
          "#8893ad",
          "#b9c4c7",
          "#b39e90"
        ]
        "description": "Join other founders and get weekly, curated startup design & growth insight delivered straight to your inbox.",
        "title": "Designing Growth | Weekly Design & Growth Insight",
        "palette": [
          "#151515",
          "#ebebe3",
          "#646fe1",
          "#61d4e5",
          "#f2d276",
          "#c09b58",
          "#88582e",
          "#8893ad",
          "#b9c4c7",
          "#b39e90"
        ]
        "description": "Introducing terminalGPT, powered by OpenAI's GPT. It's a chatbot for your terminal that can understand and respond to a wide range of topics and questions in real-time. Whether you want to chat or need help with a task, terminalGPT has you covered. Try it out and see the power of GPT for yourself!",
        "title": "GitHub - jucasoliveira/terminalGPT at producthunt",
        "palette": [
          "#242b2d",
          "#f2f8f8",
          "#9c5c41",
          "#3975c3",
          "#d59e5c",
          "#56afd4",
          "#93b2c9",
          "#f3d59b",
          "#c8a998",
          "#bfe5eb"
        ]
        "description": "We're excited to introduce Muglaunch.com. For Amazon, Etsy, and Shopify sellers who want to design and sell print on demand products with ease. Design, Upload, Sell, Print FilesFulfillment. All done in one platform.",
        "title": "MugLaunch | Start Your Own Print On Demand Business Today!",
        "palette": [
          "#2664e8",
          "#f6f5f8",
          "#242837",
          "#96b0c6",
          "#916057",
          "#c48b63",
          "#cbc5cd",
          "#6dbaf6",
          "#f2cc9d",
          "#cfa797"
        ]
  "description": "Write personalized, insightful, and relevant LinkedIn intro messages to anyone in just one click. Simply log in through LinkedIn, visit another user's profile, and click a button.",
        "title": "SayHi: Persuasive LinkedIn Message Writer",
        "palette": [
          "#2288c9",
          "#f3f3f2",
          "#1d1320",
          "#97adc3",
          "#eba94c",
          "#9b5528",
          "#c2dce8",
          "#bea4a7",
          "#f3d296",
          "#594e43"
        ]
        "description": "An app that can quickly and efficiently detect whether an essay is ChatGPT or human written.",
        "title": "Streamlit"
        "description": "Harken is a Spotify tool that lets you find all the songs you thought were lost in generated playlists. Can't remember the name of that song you heard in a playlist and can't find it in the playlist anymore? Let Harken find it for you!",
        "title": "Harken | Find the Spotify songs you thought were lost!",
        "palette": [
          "#3db45f",
          "#23232a",
          "#f8f9f8",
          "#a86637",
          "#cfa866",
          "#715c5d",
          "#3d75b7",
          "#34894d",
          "#243b7a",
          "#4b3235"
        ]
        "description": "dataTile for Simulator is a productivity tool that helps iOS developers save time while debugging. The app is an Xcode \"companion\" that adds both brains and beauty to developing for the iPhone. It requires no 3rd party code dependencies.",
        "title": "",
        "palette": [
          "#fbebec",
          "#2d3b3c",
          "#d73ba2",
          "#28b6e5",
          "#9f8bad",
          "#4e63cc",
          "#adb2b6",
          "#c8c0cd",
          "#7c7c7c",
          "#bcb4b4"
        ]
        "description": "#2 Hardware product of the year\nMore recipients →",
        "title": "Apple",
        "palette": [
          "#0e0d0c",
          "#f2f2f2",
          "#7b6b61",
          "#959b9e",
          "#898e66",
          "#c4cdd2",
          "#558bb5",
          "#4173a2",
          "#b8a694",
          "#c3b9a2"
        ]
        "description": "#2 Hardware product of the year\nMore recipients →",
        "title": "Apple",
        "palette": [
          "#0e0d0c",
          "#f2f2f2",
          "#7b6b61",
          "#959b9e",
          "#898e66",
          "#c4cccf",
          "#558bb5",
          "#4173a2",
          "#b8a694",
          "#c3b9a2"
        ]
        "description": "Rate your day to help identify trends in the bad days. With a simple scale from 1 to 10, add notes about what made it a good or bad day to get a better understanding to what's causing your bad days and make changes to improve your well-being.",
        "title": "Them Days on the App Store",
        "palette": [
          "#f5f5f6",
          "#323d41",
          "#8a8989",
          "#9aabaa",
          "#080909",
          "#bfee42",
          "#04149b",
          "#2d7dcc",
          "#c71a3f",
          "#5d6f4f"
        "id": "de8c",
        "description": "The addicting circle drawing game by Matt Round has a new home on neal.fun! How steady are your hands?",
        "title": "Draw a Perfect Circle ⭕️💯",
        "palette": [
          "#131313",
          "#e2eacb",
          "#6af23b",
          "#6e6e69",
          "#3c3c35",
          "#4484c4",
          "#3c4c59",
          "#446c1c",
          "#264419",
          "#141840"
        ]
        "description": "This Interactive template with scientifically proven exercises will help you generate new and innovative ideas for any project or problem you're working on. With prompts and exercises like freewriting, word association, and the \"What if?\" game, you'll never run out of ideas.",
        "title": "Idea Spark",
        "palette": [
          "#040405",
          "#c5cabb",
          "#5aa2db",
          "#1f60a8",
          "#554c40",
          "#bc7831",
          "#924411",
          "#081b5c",
          "#300d0b",
          "#244b6d"
        ]
        "description": "This Interactive template with scientifically proven exercises will help you generate new and innovative ideas for any project or problem you're working on. With prompts and exercises like freewriting, word association, and the \"What if?\" game, you'll never run out of ideas.",
        "title": "Idea Spark",
        "palette": [
          "#d0d4c2",
          "#040505",
          "#5ba3df",
          "#1e59a3",
          "#974a12",
          "#c88338",
          "#612517",
          "#091c5e",
          "#2e100f",
          "#2a4c6f"
        ]
      Suggest me a single color palette for the following description - {description}   
      """)
  chain = prompt | model | JsonOutputParser()
  ans = chain.invoke({"description":description})
  return ans