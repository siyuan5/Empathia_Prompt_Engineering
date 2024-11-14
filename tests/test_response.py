import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from consult_letter.consult_letter import create_consult_letter

response = create_consult_letter(
        # user_info = {
        # "name": "Dr. John Doe",
        # "email": "drjohndoe@clinic.com",
        # },
        # specialty = "Otolaryngology",
        # note_content =  {
        #     "Patient Name": "Betty",
        #     "Chief Complaint": "Ear pain",
        #     "History of Present Illness": "\n• Left-sided ear pain\n• No drainage noted\n• Intermittent hearing loss reported\n• Pain worsens with chewing\n• Inconsistent use of mouthpiece for teeth clenching\n• Pain relief when lying on contralateral side",
        #     "Social History": "\n• Occasional Reactive use for allergies\n• Allergy to salt",
        #     "The Review of Systems": "\n• Intermittent hearing loss\n• No swallowing issues\n• No nasal congestion\n• Allergies present, takes Reactive occasionally",
        #     "Current Medications": "\n• Reactive for allergies",
        #     "Allergies": "\n• Allergic to salt",
        #     "Physical Examination": "\n• Right ear canal clear\n• Right tympanic membrane intact\n• Right ear space aerated\n• Left ear canal normal\n• Left eardrum normal, no fluid or infection\n• Nose patent\n• Paranasal sinuses normal\n• Oral cavity clear\n• Tonsils absent\n• Good dentition\n• Pain along pterygoid muscles\n• Heart and lungs clear\n• No neck tenderness or lymphadenopathy",
        #     "Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist"
        # },
        # note_date = "2022-01-01",
        user_info={"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"},
        specialty="Obstetrics & Gynecology (ObGyn)",
        note_date="2022/01/01",
        note_content={
            "Patient Name": "Jane",
            "Patient Age": None,
            "Gender": "female",
            "Chief Complaint": "OB consultation for pregnancy management with planned repeat cesarean section.",
            "History of Present Illness": None,
            "Past Medical History": "The patient had COVID-19 in 2021, after which she experienced heart pain, but subsequent evaluations by her family doctor and hospital visits confirmed that everything was okay.",
            "Past Surgical History": "The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.",
            "Family History": None,
            "Social History": "Jane is employed part-time as a banker, working two to three days per week. She and her spouse reside in a non-specified location without nearby family support. However, they have a local friend network. Postpartum, Jane's mother will assist, and they intend to employ a babysitter for two months.",
            "Obstetric History": "The patient is currently pregnant with her third child. She has had one previous live birth via cesarean section and one abortion due to fetal health issues. Her first child was born slightly premature at approximately 37 weeks, weighing 2.5 kilograms.",
            "The Review of Systems": "The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.",
            "Current Medications": None,
            "Allergies": "The patient is allergic to minocycline.",
            "Vital Signs": None,
            "Physical Examination": None,
            "Investigations": None,
            "Problem": "1. Previous cesarean section (654.21)",
            "Differential Diagnosis": None,
            "Plan": "• Scheduled repeat cesarean section at 39 weeks gestation\n• Instructed patient to present to City Medical Center for emergency cesarean section if labor begins prior to scheduled date\n• Advised patient to walk daily for 20 to 30 minutes to improve blood pressure and baby's health\n• Arranged follow-up appointment in three weeks, with subsequent visits every two weeks, then weekly as due date nears",
            "Surgery Discussion": "• Purpose of the Surgery: The purpose of the repeat cesarean section is to safely deliver the baby, given the patient's previous cesarean delivery and her choice for a planned cesarean this time.\n• Risks and Complications: The risks of cesarean section include bleeding, infection, or injury to the bladder or bowel. These risks are small but not zero.\n• Anesthesia: Spinal anesthesia will be used during the procedure, which will prevent pain but allow the patient to be awake.\n• Alternatives: N/A",
        }
        
        
        
        )

print(response)