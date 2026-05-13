import json
import os
from config import OUTPUTS

def save_summary_to_json(summary):
    os.makedirs(os.path.dirname(OUTPUTS["json"]), exist_ok=True)

    with open(OUTPUTS["json"], "w") as f:
        json.dump(summary, f, indent=4)