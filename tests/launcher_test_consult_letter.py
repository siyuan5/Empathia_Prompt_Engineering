import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from consult_letter.test_consult_letter import test_create_consult_letter
from comprehensive_test import comprehensive_test_consult_letter


pass_counter = 0
fail_counter = 0
reasons = []
for i in range(1):
    result = test_create_consult_letter()

    if(result.upper() == "PASS"):
        pass_counter += 1
    else:
        fail_counter += 1
        reasons.append(result)
print(f"Passed on {pass_counter} occasions")
print(f"failed on {fail_counter} occasions")
for sentence in reasons:
    print(f"• {sentence}")
