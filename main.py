import os
import json
import logging
import requests 
import openai

from cache.redis_cache import RedisCache
from chat_api.chat import get_chat


MODEL_NAME = os.environ.get('MODEL_NAME')
REDIS_ENDPOINT = os.environ.get('REDIS_ENDPOINT')
API_KEY = os.environ.get('OPENAI_API_KEY')
SYSTEM_PROMPT = os.environ.get('SYSTEM_PROMPT')
ASSISTANT_PROMPT = os.environ.get('ASSISTANT_PROMPT')

openai.api_key = API_KEY

rc = RedisCache(redis_endpoint=REDIS_ENDPOINT)


def assistant_replies(request):
    """
    This is a cloud function which is triggered by HTTP requests for calling a Chat API

    Args:
        request (flask.Request): HTTP request object

    Returns:
        response (str): assistant response from Chat API
    """
    event = request.get_json(silent=True)

    try:
        if rc.check_key(event['id']):
            # If a conversation exists we will use the cached prompts
            messages = rc.get_key(event['id'])

            input_prompt = messages.append({ "role": "user", "content": event['message'] })

            response = get_chat(
                model_name=MODEL_NAME,
                input_prompt=input_prompt, 
            )

            # Update the Cache with the new conversation
            new_conversation = input_prompt.append(response)
            rc.update_key(event['id'], new_conversation)

            return response['content']
        
        else:
            # Starting a new conversation
            input_prompt = [
                { "role": "system", "content": SYSTEM_PROMPT },
                { "role": "assistant", "content": ASSISTANT_PROMPT },
                { "role": "user", "content": event['message'] }
            ]

            response = get_chat(model_name=MODEL_NAME, input_prompt=input_prompt)

            rc.add_key(event['id'], response)

            return response['content']
        

    except Exception as e:
        print(e)
