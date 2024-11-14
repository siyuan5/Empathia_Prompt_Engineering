import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from consult_letter.consult_letter import create_consult_letter
from openai_chat import chat_content



def comprehensive_test_consult_letter(consult_letter, user_info, specialty, note_content, note_date):

    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"You are a professional medical assistant of Obstetrics & Gynecology (ObGyn), \
your job is to verify the content of consult letter",
            },
            {
                "role": "user",
                "content": f"""\
The consult letter is as following, delimited by ```:
```
{consult_letter}
```
""",
            },
            {
                "role": "user",
                "content": f"""\
Make sure the letter contains the following information:
- The letter shall have doctor's name {user_info['name']}
- The letter shall mention patient name as {note_content['Patient Name']}, and the encounter happened at {note_date} (The exact format is irrelevant, as long as the date is correct)
- The information in {note_content} are all included. 
- The letter mentions that the patient is allergic to {note_content['Allergies']}.
As long as the letter contains these information, the letter is correct. 
""",
            },
            {
                "role": "user",
                "content": "Write me PASS **ONLY** if the consult letter contains all the information, and FAIL with reason if not",
            },
        ]
    )
    return result