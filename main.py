from pyscript import document

# List of Current ICT Club Members
Grade7 = {"Nuggets Zu", "Ate Nemo"}
Grade8 = {"Treszs Parker", "Kuya Nimo"}
Grade9 = {"Pritz Bondoc", "Hailey Fembi"}
Grade10 = {"Vyelle Bunag", "Prince Joshtin"}

# Combine all grade levels
All_Members = Grade7 | Grade8 | Grade9 | Grade10

# Display the initial member list
members_list = "<br>".join(sorted(All_Members))

# Function to add a new member
def add_member(event):
    global All_Members

    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    new_member = first_name + " " + last_name

    # Add the new member using a set operator
    All_Members = All_Members | {new_member}

    # Sort the member names
    members_list = "<br>".join(sorted(All_Members))

    # Display the updated results
    document.getElementById("member-results").innerHTML = f"{members_list}"
    document.getElementById("member-total").innerHTML = f"TOTAL MEMBERS: {len(All_Members)}"
    document.getElementById("members-box").style.display = "block"
