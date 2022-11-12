# install us package if not already installed locally
import us

raw_state_object_list = us.states.STATES
states = []
for state_object in raw_state_object_list:
    states.append(state_object.name.lower())

benefit_names = ['food stamps', 'medicaid']

string_for_yaml_file = ""

for state in states:
    state_formatted_with_plus = state.replace(" ", "+")
    state_formatted_with_dash = state.replace(" ", "-")
    for benefit_name in benefit_names:
        benefit_name_formatted_with_plus = benefit_name.replace(" ", "+")
        benefit_name_formatted_with_dash = benefit_name.replace(" ", "-")
        string_for_yaml_file += f"""
 - url: https://www.google.com/search?q={benefit_name_formatted_with_plus}+{state_formatted_with_plus}
   output: {benefit_name_formatted_with_dash}/{benefit_name_formatted_with_dash}-{state_formatted_with_dash}.png
   height: 1600
"""

with open(r'./shots.yml', 'w') as file:
    file.write(string_for_yaml_file)

print(string_for_yaml_file)
