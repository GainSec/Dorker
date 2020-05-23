import argparse
import re 

parser = argparse.ArgumentParser()

parser.add_argument('--f', help='search for a specific file type. note: use , for AND...use . for OR')
parser.add_argument('--k', help='keyword                          note: use , for AND...use . for OR')
parser.add_argument('--d', help='domain searches')

args = parser.parse_args()

f             = args.f
k             = args.k
s             = args.d
GLOBAL_STRING = ""
arg_count     = 0
dork_types    = 0
output_string = ""
misc          = False
AND = '+'
OR  = ','
NOT = '?'
# func that takes site as param and outputs a single dork

def dorks():
    global output_string
    global AND
    global OR
    global NOT
    cat1_out = ""
    cat2_out = ""
    cat3_out = ""
    # FOR individual categorizing
    c1G = ""
    c1Y = ""
    c1D = ""
    c1B = ""
    c1X = ""
    c1U = ""
    
    c2G = ""
    c2Y = ""
    c2D = ""
    c2B = ""
    c2X = ""
    c2U = ""

    c3G = ""
    c3Y = ""
    c3D = ""
    c3B = ""
    c3X = ""
    c3U = ""

    c4G = ""
    c4Y = ""
    c4D = ""
    c4B = ""
    c4X = ""
    c4U = ""   

    c5G = ""
    c5Y = ""
    c5D = ""
    c5B = ""
    c5X = ""
    c5U = "" 

    c99G = ""
    c99Y = ""
    c99D = ""
    c99B = ""
    c99X = ""
    c99U = ""         
    # ---------------------------
    if s is not None:
        x = s.replace(AND,' AND site:')
        x = x.replace(OR,' OR site:')
        x = x.replace(NOT,' -site:')
        c1G += " site:{}".format(x)
        c1Y += " site:{}".format(x)
        c1D += " site:{}".format(x)
        c1B += " site:{}".format(x)
        c1X += " site:{}".format(x)
        c1U += " site:{}".format(x)

        x = s.replace(AND,' AND allinurl:')
        x = x.replace(OR,' OR allinurl:')
        x = x.replace(NOT,' -allinurl:')

        c2G += " allinurl:{}".format(x)
        
        x = s.replace(AND,' AND url:')
        x = x.replace(OR,' OR url:')
        x = x.replace(NOT,' -url:')

        c2Y += " url:{}".format(x)
        c2D += ""
        c2B += ""
        c2X += ""
        
        x = s.replace(AND,' AND allinurl:')
        x = x.replace(OR,' OR allinurl:')
        x = x.replace(NOT,' -allinurl:')

        c2U += " allinurl:{}".format(x)

        
        x = s.replace(AND,' AND inurl:')
        x = x.replace(OR,' OR inurl:')
        x = x.replace(NOT,' -inurl:')

        c3G += " inurl:{}".format(x)
        c3Y += " inurl:{}".format(x)
        c3D += " inurl:{}".format(x)
        c3B += ""
        c3X += ""
        c3U += " inurl:{}".format(x)
        
        x = s.replace(AND,' AND cache:')
        x = x.replace(OR,' OR cache:')
        x = x.replace(NOT,' -cache:')

        c99G += " cache:{}".format(x)
        c99Y += ""
        
        x = s.replace(AND,' AND domain ')
        x = x.replace(OR,' OR domain ')
        x = x.replace(NOT,' -domain ')

        c99D += " domain {}".format(x)
        c99B += ""
        c99X += ""
        
        x = s.replace(AND,' AND inanchor:')
        x = x.replace(OR,' OR inanchor:')
        x = x.replace(NOT,' -inanchor:')

        c99U += " inanchor:{}".format(x) 
    if f is not None:
        x = f.replace(AND,' AND filetype:')
        x = x.replace(OR,' OR filetype:')
        x = x.replace(NOT,' -filetype:')
        c1G += " filetype:{}".format(x)
        c1Y += " filetype:{}".format(x)
        c1D += " filetype:{}".format(x)
        c1B += " filetype:{}".format(x)
        c1X += " filetype:{}".format(x)
        c1U += " filetype:{}".format(x)

        y = f.replace(AND,' AND ext:')
        y = y.replace(OR,' OR ext:')
        y = y.replace(NOT,' -ext:')
        
        c2G += " ext:{}".format(y)
        c2Y += ""
        c2D += ""
        c2B += " ext:{}".format(y)
        c2X += ""
        c2U += ""

        c3G += " ext:{}".format(y)
        c3Y += ""
        c3D += ""
        c3B += " ext:{}".format(y)
        c3X += ""
        c3U += ""
    if k is not None:
        x = k.replace(AND,'" AND "')
        x = x.replace(OR,'" OR "')
        x = x.replace(NOT,'" -"')
        c1G += ' "{}"'.format(x)
        c1Y += ' "{}"'.format(x)
        c1D += ' "{}"'.format(x)
        c1B += ' "{}"'.format(x)
        c1X += ' "{}"'.format(x)
        c1U += ' "{}"'.format(x)

        x = k.replace(AND,' AND intext:')
        x = x.replace(OR,' OR intext:')
        x = x.replace(NOT,' -intext:')

        c2G += ' intext:{}'.format(x)
        c2Y += ' {}'.format(x)
        c2D += ' {}'.format(x)

        x = k.replace(AND,' AND inbody:')
        x = x.replace(OR,' OR inbody:')
        x = x.replace(NOT,' -inbody:')
        c2B += ' inbody:{}'.format(x)
        c2X += ' {}'.format(x)
        c2U += ' {}'.format(x)

        x = k.replace(AND,' AND allintext:')
        x = x.replace(OR,' OR allintext:')
        x = x.replace(NOT,' -allintext:')

        c3G += ' allintext:{}'.format(x)
        c3Y += ' "{}"'.format(x)
        c3D += ' "{}"'.format(x)
        c3B += ' "{}"'.format(x)
        c3X += ' "{}"'.format(x)
        c3U += ' "{}"'.format(x)

        x = k.replace(AND,' AND intitle:')
        x = x.replace(OR,' OR intitle:')
        x = x.replace(NOT,' -intitle:')

        c4G += ' intitle:{}'.format(x)
        c4Y += ' intitle:{}'.format(x)
        c4D += ' intitle:{}'.format(x)
        c4B += ' intitle:{}'.format(x)
        c4X += ' "{}"'.format(x)
        c4U += ' "{}"'.format(x)

        x = k.replace(AND,' AND allintitle:')
        x = x.replace(OR,' OR allintitle:')
        x = x.replace(NOT,' -allintitle:')

        c5G += ' allintitle:{}'.format(x)
        c5Y += ' "{}"'.format(x)
        c5D += ' "{}"'.format(x)
        c5B += ' "{}"'.format(x)
        c5X += ' "{}"'.format(x)
        c5U += ' "{}"'.format(x)

    if dork_types == 7:
        output_string += "GOOGLE:       {}\n".format(c1G) # G
        output_string += "YAHOO:        {}\n".format(c1Y) # Y
        output_string += "DUCKDUCKGO:   {}\n".format(c1D) # D
        output_string += "BING:         {}\n".format(c1B) # B
        output_string += "YANDEX:       {}\n".format(c1X) # X
        output_string += "BAIDU:        {}\n".format(c1U) # U
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c2G)
        output_string += "BING:         {}\n".format(c2B)
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c3G)
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c4G)
        output_string += "YAHOO:        {}\n".format(c4Y)
        output_string += "DUCKDUCKGO:   {}\n".format(c4D)
        output_string += "BING:         {}\n".format(c4B)
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c5G)
        output_string += "\n"

        if misc:
            output_string += "GOOGLE:       {}\n".format(c99G)
            output_string += "YAHOO:        {}\n".format(c99Y)
            output_string += "DUCKDUCKGO:   {}\n".format(c99D)
            output_string += "BING:         {}\n".format(c99B)
            output_string += "YANDEX:       {}\n".format(c99X)
            output_string += "GOOGLE:       {}\n".format(c99U)
    if dork_types == 4:
        output_string += "GOOGLE:       {}\n".format(c1G) # G
        output_string += "YAHOO:        {}\n".format(c1Y) # Y
        output_string += "DUCKDUCKGO:   {}\n".format(c1D) # D
        output_string += "BING:         {}\n".format(c1B) # B
        output_string += "YANDEX:       {}\n".format(c1X) # X
        output_string += "BAIDU:        {}\n".format(c1U) # U
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c2G)
        output_string += "YAHOO:        {}\n".format(c2Y)
        output_string += "DUCKDUCKGO:   {}\n".format(c2D)
        output_string += "BING:         {}\n".format(c2B)
        output_string += "YANDEX:       {}\n".format(c2X)
        output_string += "BAIDU:        {}\n".format(c2U)
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c3G)
        output_string += "YAHOO:        {}\n".format(c3Y)
        output_string += "DUCKDUCKGO:   {}\n".format(c3D)
        output_string += "BING:         {}\n".format(c3B)
        output_string += "YANDEX:       {}\n".format(c3X)
        output_string += "BAIDU:        {}\n".format(c3U)
        output_string += "\n"
        if misc:
            output_string += "GOOGLE:       {}\n".format(c99G)
            output_string += "YAHOO:        {}\n".format(c99Y)
            output_string += "DUCKDUCKGO:   {}\n".format(c99D)
            output_string += "BING:         {}\n".format(c99B)
            output_string += "YANDEX:       {}\n".format(c99X)
            output_string += "GOOGLE:       {}\n".format(c99U)
    elif dork_types == 2:
        output_string += "GOOGLE:       {}\n".format(c1G)
        output_string += "YAHOO:        {}\n".format(c1Y)
        output_string += "DUCKDUCKGO:   {}\n".format(c1D)
        output_string += "BING:         {}\n".format(c1B)
        output_string += "YANDEX:       {}\n".format(c1X)
        output_string += "BAIDU:        {}\n".format(c1U)
        output_string += "\n"
        output_string += "GOOGLE:       {}\n".format(c2G)
        output_string += "YAHOO:        {}\n".format(c2Y)
        output_string += "DUCKDUCKGO:   {}\n".format(c2D)
        output_string += "BING:         {}\n".format(c2B)
        output_string += "YANDEX:       {}\n".format(c2X)
        output_string += "BAIDU:        {}\n".format(c2U)

    return output_string

def output():
    out = dorks()
    print("")
    print("")
    print("")
    print("  _____   ____  _____  _  ________ _____  ")
    print(" |  __ \ / __ \|  __ \| |/ /  ____|  __ \ ")
    print(" | |  | | |  | | |__) | ' /| |__  | |__) | ")
    print(" | |  | | |  | |  _  /|  < |  __| |  _  / ")
    print(" | |__| | |__| | | \ \| . \| |____| | \ \ ")
    print(" |_____/ \____/|_|  \_\_|\_\______|_|  \_\ ")
    print("")
    print("")
    print("By GainSec https://gainsec.com")
    print("https://github.com/GainSec/Dorker")
    print("")
    print("Credit to - JosephRC & GainSec")
    print("")
    print("")
    print("")
    print("Formatted Dork Strings")
    print("---------------------------------")
    print(out)
    print("---------------------------------")
    print("")

# determine what params are being used
# THIS IS ONE FUNCTION
if s is not None: #or i is not None or a is not None or d is not None:
    arg_count     += 1
    dork_types     = 4
    misc           = True

# THIS IS ANOTHER FUNCTION
if f is not None: # or e is not None:
    arg_count += 1
    if dork_types < 2:
        dork_types = 2

if k is not None:
    arg_count += 1
    if dork_types < 7:
        dork_types = 7        

output()






# output(GLOBAL_STRING)