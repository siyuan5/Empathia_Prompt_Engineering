"""
Your task is to implement `create_consult_letter` function to generate a consult letter based on the SOAP note.

The input parameters are:
- user_info: a dictionary contains the bio of the doctor, such as
    {
        "name": "Dr. John Doe", # the name of the doctor
        "email": "drjohndoe@clinic.com", # the email of the doctor
    }
- specialty: a string represents the specialty of the doctor, such as "Obstetrics and Gynecology"
- note_content: a dictionary contains the content of the SOAP note, where the key is the section name and the value is the content of the section, such as
    {
        "Chief Complaint": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        "History of Present Illness": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        ...
    }
- note_date: a string represents the date of the SOAP note, such as "2022-01-01"
"""

import json
from typing import Optional

from openai_chat import chat_content


def create_consult_letter(
    user_info: dict, specialty: str, note_content: dict[str, Optional[str]], note_date: str
) -> str:
    """
    Your prompts here
    """
    # Convert None values to "Not provided" for clearer prompting
    formatted_content = {
        k: "Not provided" if v is None else v 
        for k, v in note_content.items()
    }
    # List of information that should be included in note_content
    required_fields = ["Patient Name", "Patient Age", "Gender", "Chief Complaint", "History of Present Illness", 
                       "Past Medical History", "Past Surgical History", "Family History", "Social History", "Obstetric History", "The Review of Systems", 
                       "Current Medications", "Allergies", "Vital Signs", "Physical Examination", "Investigations", 
                       "Problem", "Differential Diagnosis", "Plan", "Surgery Discussion"]
    
    # Find out if the information is missing
    missing_keys = [key for key in required_fields if key not in formatted_content]
    
    # First part of the prompt
    myprompt = f"""Please generate a response to the family doctor who has referred you this patient. The letter should contain the following information:

                DOCTOR INFORMATION:
                - Name: {user_info['name']}
                - Email: {user_info['email']}
                - Specialty: {specialty}
                - Date of Consultation: {note_date}

                PATIENT INFORMATION:
                - Name: {formatted_content['Patient Name']}"""
    
    # Parse patient information and add to prompt            
    if 'Patient Age' in formatted_content:
        myprompt += f"\n- Age: {formatted_content['Patient Age']}"
        del formatted_content['Patient Age']
    if 'Gender' in formatted_content:
        myprompt += f"\n- Gender: {formatted_content['Gender']}"
        del formatted_content['Gender']
    
    
    # Parse formatted content, which is updated from note content, and add to prompt    
    myprompt += "\n\nCLINICAL DETAILS:"
    
    for k,v in formatted_content.items():
        myprompt += f"\n- {k}: {v}"
    
    # Explicitly add the missing info into the prompt
    myprompt += """ 
                    MISSING INFO: 
                    
                    """
    for item in missing_keys:
        myprompt += f"\n- {item}"
    
    # Final part of the prompt: instruction to write the letter.     
    myprompt += f"""
                    The letter should be formatted as follows: 
                    0. Do not use {user_info['name']} in the heading
                    1. First paragraph should be a thank you note to the family doctor for the referral of the patient, including {formatted_content['Patient Name']}, the {specialty} and {note_date}
                    2. Second paragraph should be patient's complaint and history, be specific with date or year of patient's history, and be sure to mention any allergies. 
                    3. Third paragraph should be the result of the examination.
                    4. Fourth paragraph should be the plan
                    5. Fifth paragraph is optional. If there are things missing from the SOAP note, then say these items are "not provided in the SOAP note. Therefore, these details are not included in this consultation letter."
                    6. Sign with Doctor Information, including {user_info['name']}, {specialty}, {user_info['email']}
                    """
                    
                    

    response  = chat_content(
        messages=[
        {"role": "system", "content": "You are a specialist doctor"},
        {"role": "user", "content": myprompt}
        ],
        temperature=0,
    )
    
    
    return response