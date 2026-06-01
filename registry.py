# --- CONSOLIDATED GEOGRAPHICAL CONFIGURATION ---
# Updated with Karu, Keffi, and Kokona LGAs
LGA_WARD_DATA = {
    "KARU": [
        "ASO/KODAPE",
        "BAGAJI/AGADA",
        "GITATA",
        "GURKU/KABUSU",
        "KARSHI I",
        "KARSHI II",
        "KARU",
        "KAFIN SHANU/BETTI",
        "PANDA/KARE",
        "TATTARA/KONDORO",
        "UKE",
    ],
    "KEFFI": [
        "ANG. RIMI",
        "GANGARE TUDU",
        "JIGWADA",
        "KOFAR GORIYA",
        "LIMAN ABAJI",
        "MAKERA",
        "RINJI",
        "SABON GARI",
        "YARGARE",
        "YELWA",
    ],
    "KOKONA": [
        "AGWADA",
        "AMBA",
        "BASSA",
        "DARI",
        "GARAKU",
        "HADARI",
        "KOKONA",
        "KOYA/KANA",
        "NINKORO",
        "KOFAR GWARI",
        "YELWA",
    ],
}

# The Column structure remains optimal and unchanged
COLUMNS_STRUCTURE = [
    "NIN",
    "VIN",
    "Name",
    "LGA",
    "Ward",
    "Status",
    "Category",
    "Skill_Interest",
    "Custom_Skill",
    "Gender",
    "DOB",
    "Disability_Status",
    "Prior_Palliative",
    "Academic_Qual",
    "Admission_Year",
    "Admission_Letter",
    "Phone",
    "Leader_Name",
    "Leader_Contact",
    "Leader_NIN",
    "Leader_LGA",
    "Leader_Ward",
    "Leader_Portfolio",
    "Voucher_Code",
    "Remarks",
    "Timestamp",
]


def get_wards(lga_name):
    """Helper function to dynamically retrieve wards based on LGA selection."""
    return LGA_WARD_DATA.get(lga_name.upper(), [])
