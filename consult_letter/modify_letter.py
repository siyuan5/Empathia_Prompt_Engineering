import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from consult_letter.consult_letter import create_consult_letter
from openai_chat import chat_content

def modify_letter(consult_letter, feedback):
    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"You are a professional medical assistant your job is to modify the consult letter according to feedback",
            },
            {
                "role": "user",
                "content": f"""\
The consult letter is as following, delimited by ```:
```
{consult_letter}
```
The feedback is as following, delimited by ```:
```
{feedback}
```
""",
            },
            {
                "role": "user",
                "content": f"""\
Keep the same structure as the orginal letter, but add or modify information according to feedback.
""",
            }
        ]
    )
    return result
