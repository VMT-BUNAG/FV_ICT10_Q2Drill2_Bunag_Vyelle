from pyscript import document, display

# List of Current ICT Club Members

Grade7 = {"Nuggets Zu", "Ate Nemo"}
Grade8 = {"Treszs Parker", "Kuya Nimo"}
Grade9 = {"Pritz Bondoc", "Hailey Fembi"}
Grade10 = {"Vyelle Bunag", "Prince Joshtin"}
All_Members = Grade7 | Grade8 | Grade9 | Grade10



def check_name(e):
    first = document.getElementById("first").value
    last = document.getElementById("last").value
    full_name = f"{first} {last}"
\

members_list = "<br>".join(sorted(All_Members))
display(len(All_Members))

