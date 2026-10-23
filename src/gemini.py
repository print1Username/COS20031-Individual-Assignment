import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv( 'GEMINI_API_KEY' )

if not api_key:
	raise ValueError( 'Can`t find GEMINI_API_KEY, please check your .env file.' )

genai.configure( api_key = api_key )

model = genai.GenerativeModel( 'gemini-1.5-flash-latest' )


def ask_question(question):
	answer = model.generate_content( question )

	if answer.parts:
		text = answer.text
		if text:
			return text.replace( '*', '' )
		else:
			return None
	else:
		return None
