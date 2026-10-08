from pyscript import document

# ==========================================
# 1. ICT CLUB MEMBER LIST
# ==========================================
CLUB_MEMBERS = [
    "Kathryn Bernardo", "Daniel Padilla", "Alden Richards", "Maine Mendoza",
    "Marian Rivera", "Dingdong Dantes", "Anne Curtis", "Erwan Heussaff",
    "Sarah Geronimo", "Matteo Guidicelli", "Kim Chiu", "Paulo Avelino",
    "Nadine Lustre", "James Reid", "Liza Soberano", "Enrique Gil",
    "Bea Alonzo", "Gerald Anderson", "Julia Barretto", "Joshua Garcia",
    "Andrea Brillantes", "Francine Diaz", "Seth Fedelin", "Donny Pangilinan",
    "Belle Mariano", "Anthony Jennings", "Coco Martin", "Julia Montes",
    "Piolo Pascual", "Judy Ann Santos", "Ryan Agoncillo", "Vice Ganda",
    "Jhong Hilario", "Billy Crawford", "Luis Manzano", "Toni Gonzaga",
    "Alex Gonzaga", "Vhong Navarro", "Robin Padilla", "Bea Binene",
    "Angel Locsin", "Angelica Panganiban", "Iza Calzado", "Carla Abellana",
    "Jennylyn Mercado", "Dennis Trillo", "Tom Rodriguez", "Jericho Rosales",
    "Carlo Aquino", "Alessandra De Rossi", "Arjo Atayde", "Ria Atayde",
    "Sharon Cuneta", "Regine Velasquez", "Ogie Alcasid", "Gary Valenciano",
    "Rico Blanco", "Lea Salonga"
]

# Set comprehension to normalize the names for case-insensitive checking
NORMALIZED_MEMBERS = {member.lower().strip() for member in CLUB_MEMBERS}

def verify_candidate(event):
    # 3. Get the first and last name entered by the user and combine them
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()
    
    full_name = f"{first_name} {last_name}"
    normalized_query = full_name.lower().strip()

    # 4. Check whether the full name is in the club members list and store in a variable
    is_member = normalized_query in NORMALIZED_MEMBERS

    # 5. Display a message based on the result (Using Dictionaries to avoid conditional statements)
    response_messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    # Map the boolean check result directly to CSS classes to change colors without using if statements
    css_classes = {
        True: "has-result success",
        False: "has-result error"
    }

    output_div = document.querySelector("#result-area")
    
    # Retrieve the correct message and styling based strictly on the True/False boolean value
    output_div.innerText = response_messages[is_member]
    output_div.className = css_classes[is_member]
