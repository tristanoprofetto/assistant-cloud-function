import os
import logging
from openai import ChatCompletion


def get_chat(model_name: str, input_prompt: list) :
    """
    This function passes a given input prompt to the Chat API...
    For a given conversationID (sessionID), we append every user/assistant message to a list of messages required for prompting the correct response to the assistan

    Args:
        model_name (str): name of the model used to act as the assistant
        input_prompt (str): array of system, user, and assistant prompts required to trigger the required response

    Returns:
        response (dict): ChatGPT API response
    """
    response = ChatCompletion.create(
        model = model_name,
        messages = input_prompt
    )

    return response['choices'][0]['message']

    
if __name__ == "__main__":
    get_chat(str, list)
    


