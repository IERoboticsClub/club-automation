"""
Streamlit automation dashboard to schedule and monitor the automation process.
Makes use of cron to schedule running scripts which the user selects from the dashboard. with provided arguments.
"""
import streamlit as st
import yaml
import uuid

# automations.yaml
with open("automations.yaml") as f:
    automations = yaml.load(f, Loader=yaml.FullLoader)

automation_names = list(automations.keys())
automation_name = st.selectbox("Select an automation to schedule", automation_names)

#TODO add whatsapp message drafter

# automation arguments
automation = automations[automation_name]
args = automation["arguments"]
arg_values = {}
# get str between [type] from the arguments
arg_types = [ arg[arg.find("[")+1:arg.find("]")] for arg in args]
args = [ arg[:arg.find("[")].strip() for arg in args]
for arg in range(len(args)):
    arg_values[arg] = st.text_input(args[arg])

# schedule with a calendar and time picker
schedule = st.date_input("Select a date to schedule the automation")
# 5 min intervals
time = st.time_input("Select a time to schedule the automation", step=300)

# schedule the automation
if st.button("Schedule"):
    id = str(uuid.uuid4())
    # convert to cron format (runs once at the specified time)
    cron = f"{time.minute} {time.hour} {schedule.day} {schedule.month} *"
    script = automation["template"]
    i = 0
    for arg in args:
        val=arg_values[i]
        if arg_types[i] == "str":

            script = script.replace(f"{{{arg}}}", f"'{val}'")
        elif arg_types[i] == "list":
            # split by ,
            val = val.split(",")
            script = script.replace(f"{{{arg}}}", val.__repr__())
        i += 1
    self_destruct = f"import os\nos.remove('.{id}.py')\n"
    script = script + "\n" + self_destruct
    print(script)
    st.code(script)
    with open(f".{id}.py", "w") as f:
        f.write(script)


    import os
    current_path = os.getcwd()
    cron_path = os.path.join(current_path, "cron.txt")
    with open("cron.txt", "a") as f:
        f.write(f"{cron} python {current_path}/.{id}.py\n")
    os.system(f"crontab {cron_path}")
    st.write(f"Scheduled {automation_name} for {schedule} at {time}")
