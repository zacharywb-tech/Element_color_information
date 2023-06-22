from PIL import Image, ImageDraw, ImageFont
import os

# Element data (symbol, atomic number, atomic name, atomic mass)
elements = [
    ("H", 1, "Hydrogen", 1.008),
    ("He", 2, "Helium", 4.0026),
    ("Li", 3, "Lithium", 6.94),
    ("Be", 4, "Beryllium", 9.0122),
    ("B", 5, "Boron", 10.81),
    ("C", 6, "Carbon", 12.01),
    ("N", 7, "Nitrogen", 14.01),
    ("O", 8, "Oxygen", 16.00),
    ("F", 9, "Fluorine", 19.00),
    ("Ne", 10, "Neon", 20.18),
    ("Na", 11, "Sodium", 22.99),
    ("Mg", 12, "Magnesium", 24.31),
    ("Al", 13, "Aluminum", 26.98),
    ("Si", 14, "Silicon", 28.09),
    ("P", 15, "Phosphorus", 30.97),
    ("S", 16, "Sulfur", 32.07),
    ("Cl", 17, "Chlorine", 35.45),
    ("K", 19, "Potassium", 39.10),
    ("Ar", 18, "Argon", 39.95),
    ("Ca", 20, "Calcium", 40.08),
    ("Sc", 21, "Scandium", 44.96),
    ("Ti", 22, "Titanium", 47.87),
    ("V", 23, "Vanadium", 50.94),
    ("Cr", 24, "Chromium", 52.00),
    ("Mn", 25, "Manganese", 54.94),
    ("Fe", 26, "Iron", 55.85),
    ("Ni", 28, "Nickel", 58.69),
    ("Co", 27, "Cobalt", 58.93),
    ("Cu", 29, "Copper", 63.55),
    ("Zn", 30, "Zinc", 65.38),
    ("Ga", 31, "Gallium", 69.72),
    ("Ge", 32, "Germanium", 72.63),
    ("As", 33, "Arsenic", 74.92),
    ("Se", 34, "Selenium", 78.97),
    ("Br", 35, "Bromine", 79.90),
    ("Kr", 36, "Krypton", 83.80),
    ("Rb", 37, "Rubidium", 85.47),
    ("Sr", 38, "Strontium", 87.62),
    ("Y", 39, "Yttrium", 88.91),
    ("Zr", 40, "Zirconium", 91.22),
    ("Nb", 41, "Niobium", 92.91),
    ("Mo", 42, "Molybdenum", 95.95),
    ("Tc", 43, "Technetium", 98.00),
    ("Ru", 44, "Ruthenium", 101.1),
    ("Rh", 45, "Rhodium", 102.9),
    ("Pd", 46, "Palladium", 106.4),
    ("Ag", 47, "Silver", 107.9),
    ("Cd", 48, "Cadmium", 112.4),
    ("In", 49, "Indium", 114.8),
    ("Sn", 50, "Tin", 118.7),
    ("Sb", 51, "Antimony", 121.8),
    ("I", 53, "Iodine", 126.9),
    ("Te", 52, "Tellurium", 127.6),
    ("Xe", 54, "Xenon", 131.3),
    ("Cs", 55, "Cesium", 132.9),
    ("Ba", 56, "Barium", 137.3),
    ("La", 57, "Lanthanum", 138.9),
    ("Ce", 58, "Cerium", 140.1),
    ("Pr", 59, "Praseodymium", 140.9),
    ("Nd", 60, "Neodymium", 144.2),
    ("Pm", 61, "Promethium", 145.0),
    ("Sm", 62, "Samarium", 150.4),
    ("Eu", 63, "Europium", 152.0),
    ("Gd", 64, "Gadolinium", 157.3),
    ("Tb", 65, "Terbium", 158.9),
    ("Dy", 66, "Dysprosium", 162.5),
    ("Ho", 67, "Holmium", 164.9),
    ("Er", 68, "Erbium", 167.3),
    ("Tm", 69, "Thulium", 168.9),
    ("Yb", 70, "Ytterbium", 173.0),
    ("Lu", 71, "Lutetium", 175.0),
    ("Hf", 72, "Hafnium", 178.5),
    ("Ta", 73, "Tantalum", 180.9),
    ("W", 74, "Tungsten", 183.8),
    ("Re", 75, "Rhenium", 186.2),
    ("Os", 76, "Osmium", 190.2),
    ("Ir", 77, "Iridium", 192.2),
    ("Pt", 78, "Platinum", 195.1),
    ("Au", 79, "Gold", 197.0),
    ("Hg", 80, "Mercury", 200.6),
    ("Tl", 81, "Thallium", 204.4),
    ("Pb", 82, "Lead", 207.2),
    ("Bi", 83, "Bismuth", 208.9),
    ("Po", 84, "Polonium", 209.0),
    ("At", 85, "Astatine", 210.0),
    ("Rn", 86, "Radon", 222.0),
    ("Fr", 87, "Francium", 223.0),
    ("Ra", 88, "Radium", 226.0),
    ("Ac", 89, "Actinium", 227.0),
    ("Pa", 91, "Protactinium", 231.0),
    ("Th", 90, "Thorium", 232.0),
    ("Np", 93, "Neptunium", 237.0),
    ("U", 92, "Uranium", 238.0),
    ("Am", 95, "Americium", 243.0),
    ("Pu", 94, "Plutonium", 244.0),
    ("Cm", 96, "Curium", 247.0),
    ("Bk", 97, "Berkelium", 247.0),
    ("Cf", 98, "Californium", 251.0),
    ("Es", 99, "Einsteinium", 252.0),
    ("Fm", 100, "Fermium", 257.0),
    ("Md", 101, "Mendelevium", 258.0),
    ("No", 102, "Nobelium", 259.0),
    ("Lr", 103, "Lawrencium", 262.0),
    ("Rf", 104, "Rutherfordium", 267.0),
    ("Db", 105, "Dubnium", 270.0),
    ("Sg", 106, "Seaborgium", 271.0),
    ("Bh", 107, "Bohrium", 270.0),
    ("Hs", 108, "Hassium", 277.0),
    ("Mt", 109, "Meitnerium", 276.0),
    ("Ds", 110, "Darmstadtium", 281.0),
    ("Rg", 111, "Roentgenium", 280.0),
    ("Cn", 112, "Copernicium", 285.0),
    ("Nh", 113, "Nihonium", 284.0),
    ("Fl", 114, "Flerovium", 289.0),
    ("Mc", 115, "Moscovium", 288.0),
    ("Lv", 116, "Livermorium", 293.0),
    ("Ts", 117, "Tennessine", 294.0),
    ("Og", 118, "Oganesson", 294.0),
]

# Color definitions for elements (in RGB format)
element_colors = {
    "H": (230, 230, 230),    # Light gray color for Hydrogen
    "He": (217, 255, 255),  # Pale cyan color for Helium
    "Li": (204, 128, 255),  # Pastel purple color for Lithium
    "Be": (194, 255, 0),    # Lime green color for Beryllium
    "B": (255, 181, 181),   # Light coral color for Boron
    "C": (0, 0, 0),         # Black color for Carbon
    "N": (30, 30, 255),     # Blue color for Nitrogen
    "O": (255, 13, 13),     # Red color for Oxygen
    "F": (144, 224, 24),    # Lime color for Fluorine
    "Ne": (182, 255, 255),  # Pale cyan color for Neon
    "Na": (50, 50, 255),    # Medium blue color for Sodium
    "Mg": (129, 255, 0),    # Chartreuse color for Magnesium
    "Al": (128, 128, 144),  # Slate gray color for Aluminum
    "Si": (255, 208, 0),    # Gold color for Silicon
    "P": (255, 128, 0),     # Orange color for Phosphorus
    "S": (255, 255, 48),    # Yellow color for Sulfur
    "Cl": (0, 255, 0),      # Green color for Chlorine
    "K": (143, 64, 212),    # Dark violet color for Potassium
    "Ar": (128, 209, 227),  # Light blue color for Argon
    "Ca": (61, 255, 0),     # Bright green color for Calcium
    "Sc": (230, 230, 230),  # Light gray color for Scandium
    "Ti": (191, 194, 199),  # Silver color for Titanium
    "V": (166, 166, 171),   # Gray color for Vanadium
    "Cr": (138, 153, 199),  # Blue-gray color for Chromium
    "Mn": (156, 122, 199),  # Purplish-pink color for Manganese
    "Fe": (192, 108, 132),  # Dark pink color for Iron
    "Ni": (80, 208, 80),    # Lime green color for Nickel
    "Co": (240, 144, 160),  # Salmon pink color for Cobalt
    "Cu": (184, 115, 51),   # Brown color for Copper
    "Zn": (212, 212, 229),  # Light gray color for Zinc
    "Ga": (194, 143, 143),  # Indian red color for Gallium
    "Ge": (102, 143, 143),  # Dark slate gray color for Germanium
    "As": (189, 128, 227),  # Medium purple color for Arsenic
    "Se": (255, 160, 0),    # Dark orange color for Selenium
    "Br": (166, 41, 41),    # Brown color for Bromine
    "Kr": (92, 184, 209),   # Deep sky blue color for Krypton
    "Rb": (112, 46, 176),   # Purple color for Rubidium
    "Sr": (0, 255, 0),      # Green color for Strontium
    "Y": (148, 255, 255),   # Light cyan color for Yttrium
    "Zr": (148, 224, 224),  # Pale cyan color for Zirconium
    "Nb": (115, 194, 201),  # Steel blue color for Niobium
    "Mo": (84, 181, 181),   # Dark cyan color for Molybdenum
    "Tc": (59, 158, 158),   # Dark turquoise color for Technetium
    "Ru": (36, 143, 143),   # Dark slate gray color for Ruthenium
    "Rh": (10, 125, 140),   # Dark cyan color for Rhodium
    "Pd": (0, 105, 133),    # Dark cyan color for Palladium
    "Ag": (192, 192, 192),  # Silver color for Silver
    "Cd": (255, 217, 143),  # Light goldenrod color for Cadmium
    "In": (166, 117, 115),  # Brown color for Indium
    "Sn": (102, 128, 128),  # Teal color for Tin
    "Sb": (158, 99, 181),   # Dark violet color for Antimony
    "Te": (212, 122, 0),    # Chocolate color for Tellurium
    "I": (148, 0, 148),     # Dark magenta color for Iodine
    "Xe": (66, 158, 176),   # Medium aquamarine color for Xenon
    "Cs": (87, 23, 143),    # Purple color for Cesium
    "Ba": (0, 201, 0),      # Green color for Barium
    "La": (112, 212, 255),  # Light steel blue color for Lanthanum
    "Ce": (255, 255, 199),  # Pale yellow color for Cerium
    "Pr": (217, 255, 199),  # Pale green color for Praseodymium
    "Nd": (199, 255, 199),  # Pastel green color for Neodymium
    "Pm": (163, 255, 199),  # Light green color for Promethium
    "Sm": (143, 255, 199),  # Pale green color for Samarium
    "Eu": (97, 255, 199),   # Pale green color for Europium
    "Gd": (69, 255, 199),   # Pale green color for Gadolinium
    "Tb": (48, 255, 199),   # Pale green color for Terbium
    "Dy": (31, 255, 199),   # Pale green color for Dysprosium
    "Ho": (0, 255, 156),    # Medium green color for Holmium
    "Er": (0, 230, 117),    # Medium sea green color for Erbium
    "Tm": (0, 212, 82),     # Medium sea green color for Thulium
    "Yb": (0, 191, 56),     # Medium sea green color for Ytterbium
    "Lu": (0, 171, 36),     # Medium sea green color for Lutetium
    "Hf": (77, 194, 255),   # Light sky blue color for Hafnium
    "Ta": (77, 166, 255),   # Light sky blue color for Tantalum
    "W": (33, 148, 214),    # Dodger blue color for Tungsten
    "Re": (38, 125, 171),   # Dark cyan color for Rhenium
    "Os": (38, 102, 150),   # Dark cyan color for Osmium
    "Ir": (23, 84, 135),    # Dark blue color for Iridium
    "Pt": (208, 208, 224),  # Light gray color for Platinum
    "Au": (255, 209, 35),   # Gold color for Gold
    "Hg": (184, 184, 208),  # Light gray color for Mercury
    "Tl": (166, 84, 77),    # Brown color for Thallium
    "Pb": (87, 89, 97),     # Dark gray color for Lead
    "Bi": (158, 79, 181),   # Dark violet color for Bismuth
    "Th": (0, 186, 255),    # Dodger blue color for Thorium
    "Pa": (0, 161, 255),    # Dodger blue color for Protactinium
    "U": (0, 143, 255),     # Dodger blue color for Uranium
    "Np": (0, 128, 255),    # Dodger blue color for Neptunium
    "Pu": (0, 107, 255),    # Dodger blue color for Plutonium
    "Am": (84, 92, 242),    # Medium blue color for Americium
    "Cm": (120, 92, 227),   # Medium blue color for Curium
    "Bk": (138, 79, 227),   # Medium blue color for Berkelium
    "Cf": (161, 54, 212),   # Dark violet color for Californium
    "Es": (179, 31, 212),   # Dark violet color for Einsteinium
    "Fm": (179, 31, 186),   # Dark violet color for Fermium
    "Md": (179, 13, 166),   # Dark violet color for Mendelevium
    "No": (189, 13, 135),   # Dark violet color for Nobelium
    "Lr": (199, 0, 102),    # Dark violet color for Lawrencium
    "Rf": (204, 0, 89),     # Dark red color for Rutherfordium
    "Db": (209, 0, 79),     # Dark red color for Dubnium
    "Sg": (217, 0, 69),     # Dark red color for Seaborgium
    "Bh": (224, 0, 56),     # Dark red color for Bohrium
    "Hs": (230, 0, 46),     # Dark red color for Hassium
    "Mt": (235, 0, 38),     # Dark red color for Meitnerium
    "Ds": (235, 0, 38),     # Dark red color for Darmstadtium
    "Rg": (235, 0, 38),     # Dark red color for Roentgenium
    "Cn": (235, 0, 38),     # Dark red color for Copernicium
    "Nh": (235, 0, 38),     # Dark red color for Nihonium
    "Fl": (235, 0, 38),     # Dark red color for Flerovium
    "Mc": (235, 0, 38),     # Dark red color for Moscovium
    "Lv": (235, 0, 38),     # Dark red color for Livermorium
    "Ts": (235, 0, 38),     # Dark red color for Tennessine
    "Og": (235, 0, 38),     # Dark red color for Oganesson
}

# Create the "elements" folder on the desktop if it doesn't exist
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
elements_folder_path = os.path.join(desktop_path, "elements")
if not os.path.exists(elements_folder_path):
    os.makedirs(elements_folder_path)

# Define font sizes
font_size_title = 72
font_size_info = 48

# Define font paths (change them according to your system)
font_path_bold = "/Library/Fonts/Arial Bold.ttf"
font_path_regular = "/Library/Fonts/Arial.ttf"

# Load fonts
font_title = ImageFont.truetype(font_path_bold, font_size_title)
font_info = ImageFont.truetype(font_path_regular, font_size_info)

# Loop through the elements
for element_data in elements:
    element_symbol, atomic_number, atomic_name, atomic_mass = element_data

    # Get the color for the element
    element_color = element_colors.get(element_symbol, (255, 255, 255))  # Default to white color

    # Create a new image
    image_width = 1000
    image_height = 1000
    image = Image.new("RGB", (image_width, image_height), element_color)
    draw = ImageDraw.Draw(image)

    # Calculate text sizes
    element_symbol_width, element_symbol_height = draw.textsize(element_symbol, font=font_title)
    atomic_number_width, atomic_number_height = draw.textsize(str(atomic_number), font=font_info)
    atomic_name_width, atomic_name_height = draw.textsize(atomic_name, font=font_info)
    atomic_mass_width, atomic_mass_height = draw.textsize(str(atomic_mass), font=font_info)

    # Define text positions
    symbol_position = ((image_width - element_symbol_width) // 2, (image_height - element_symbol_height - atomic_name_height) // 2)
    atomic_number_position = (20, 20)  # Top left corner with some padding
    atomic_mass_position = (image_width - atomic_mass_width - 20, image_height - atomic_mass_height - 20)  # Bottom right corner with some padding

    # Calculate the position for atomic name (centered below the symbol)
    atomic_name_x = (image_width - atomic_name_width) // 2
    atomic_name_y = symbol_position[1] + element_symbol_height
    atomic_name_position = (atomic_name_x, atomic_name_y)

    # Draw element symbol
    draw.text(symbol_position, element_symbol, fill="black", font=font_title)

    # Draw atomic number
    draw.text(atomic_number_position, str(atomic_number), fill="black", font=font_info)

    # Draw atomic name
    draw.text(atomic_name_position, atomic_name, fill="black", font=font_info)

    # Draw atomic mass
    draw.text(atomic_mass_position, str(atomic_mass), fill="black", font=font_info)

    # Save the image as element_symbol.jpg in the elements folder on the desktop
    file_path = os.path.join(elements_folder_path, f"{element_symbol}.jpg")
    image.save(file_path, "JPEG")

print("Element color images saved successfully!")