import pytest
from typing import List, Optional, Dict


@pytest.fixture
def chat_user_input():
    user_input = {
        'role': 'user',
        'content': 'What is the meaning of life?'
    }
    return user_input


@pytest.fixture
def chat_response_message():
    message = {
        'role': 'assistant',
        'content': 'yes absolutely'
    }
    return message


@pytest.fixture
def chat_response_choices(chat_response_message):
    choices = [
        {
            'message': chat_response_message,
            'finish_reason': 'stop',
            'index': 0
        }
    ]
    return choices


@pytest.fixture
def chat_response_usage():
    usage = {
        'prompt_tokens': 56,
        'completion_tokens': 31,
        'total_tokens': 87
    }
    return usage


@pytest.fixture
def chat_response(chat_response_choices, chat_response_usage):
    response = {
        'id': '1',
        'object': 'chat.completion',
        'created': 1234,
        'model': 'gpt-3.5-turbo',
        'usage': chat_response_usage,
        'choices': chat_response_choices
    }

    return response