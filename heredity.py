import random, secrets

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
# import cairosvg
import svgutils.transform as sg
import sys 

roof_types_list = ["helipad", "garden", "bar", "lounge", "amusement", "patio", "pool"]
body_types_list = ["tubed", "tbd"]
base_types_list = ["garden", "parking", "coffeeshop"]
window_types_list = ["glass curtain wall"]
roof_colors_list = ["gold", "yellow", "silver", "grey", "bronze", "red", "white",
    "black", "green", "red", "light grey"]
body_colors_list = ["red", "dark red", "navy", "medium blue", "light blue", "dark grey",
    "medium grey", "light grey", "black", "brown", "beige", "turquoise"]
base_colors_list = ["red", "dark red", "navy", "medium blue", "light blue", "dark grey",
    "medium grey", "light grey", "black", "brown", "beige", "turquoise"]
window_colors_list = ["navy", "medium blue", "light blue", "dark grey", "medium grey",
    "light grey", "black", "brown", "beige", "turquoise", "white"]
texture_list = ["brick", "steel", "marble", "cement"]
height_list = ["low rise", "high rise", "skyscraper", "super-tall skyscraper", "mega-tall skyscraper"]
width_list = ["normal", "wide"]
style_list = ["modern", "Bauhaus", "International Style", "Postmodernism", "Structural Expressionism", 
    "Brutalist", "neo-futurism", "Revival", "Spanish", "Colonial Revival", "neo-gothic", "neo-classicism",
    'Historical', "Gothic", "Greek", "Romanesque", "Transitional", "art deco", "Chicago School", "Expressionism"]

# load matpotlib-generated figures
def vector(filepath):
    fig1 = sg.fromfile(filepath)
    plot1 = fig1.getroot()
    return plot1

# def svg_to_png(filepath):
#     cairosvg.svg2png(url= filepath, write_to='image.png')

types_list = [body_types_list, base_types_list, window_types_list]
colors_list = [roof_colors_list, body_colors_list, base_colors_list, window_colors_list]
ignore_list = [style_list, texture_list, height_list, width_list]

all_attrs = [roof_types_list, body_types_list, base_types_list, window_types_list, roof_colors_list, 
   body_colors_list, base_colors_list, window_colors_list, texture_list, height_list, width_list, style_list] 

# traits are either passed down randomly, or preserved and unchanged

#Which traits are preserved

#swappable traits:
rarity_levels = ["rare", "heirloom", "gem", "common", "local", "unique"]
rarity_dict = {"rare": 5, "heirloom": 15, "gem": 10, "local": 10, "unique": 1}
# create a dictionary of how rare any of these might be

def weightings(attr_list):
    extra_attrs = []
    for attr in attr_list:
        times = rarity_dict[attr]
        for i in range(times -1):
            extra_attrs.append(attr)
    all_attrs = attr_list + extra_attrs
    return all_attrs

def rand(attr_list):
    trait = secrets.choice(attr_list)
    return trait

def rand_construct():
    trait_list = []
    for attr in all_attrs:
        trait = rand(attr)
        trait_list.append(trait)
    return trait_list

def rand_color():
    color = secrets.token_hex(3)
    return color

def two_colors(hex1, hex2):
    hex_list = [hex1, hex2]
    selected = rand(hex_list)
    return selected

def colorconvert(val):
    if type(val) == tuple:
        rgb_tuple = val
        hex_code = '#%02x%02x%02x' % val
    elif type(val) == str:
        rgb_tuple = tuple(int(val[i:i+2], 16) for i in (0, 2 ,4))
        hex_code = "#" + val
    return rgb_tuple, hex_code

def svgimg(path):
    drawing = svg2rlg("file.svg")
    renderPDF.drawToFile(drawing, "file.pdf")
    renderPM.drawToFile(drawing, "file.png")

# def construct():
#     trait_list = []
#     # this will be determined not randomly
#     for build_type_list in types_list:
#         trait = rand(build_type)
#         trait_list.append(trait)
#     for color_list in colors_list:
#         trait = rand(color_list)
#         trait_list.append(trait)



def address():
    sample_wallet = "0x" + secrets.token_hex(20)
    return sample_wallet




url_create = []

