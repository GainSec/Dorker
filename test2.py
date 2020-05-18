'''creates DB and table correct, inserts urls arguments correct, selects site properly
    Added some new arguments to make it similar'''

import argparse
import re 

parser = argparse.ArgumentParser()

parser.add_argument('--s', help='search for domain "in site"')
parser.add_argument('--f', help='search for a specific file type. note: use , for AND...use . for OR')
parser.add_argument('--e', help='search for file extension.       note: use , for AND...use . for OR')
parser.add_argument('--k', help='keyword                          note: use , for AND...use . for OR')
parser.add_argument('--a', help='all in url')
parser.add_argument('--i', help='in url')
parser.add_argument('--A', help='AND keyword')


args = parser.parse_args()

# print(args)
# print(type(args.k))
s             = args.s
f             = args.f
k             = args.k
a             = args.a
i             = args.i
e             = args.e
GLOBAL_STRING = ""
arg_count     = 0
dork_types    = 0
output_string = ""
# func that takes site as param and outputs a single dork

def dorks():
    global output_string
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
    # ---------------------------
    if s is not None:
        cat1_out += " site:{}".format(s)
        cat2_out += " allinurl:{}".format(s)
        cat3_out += " inurl:{}".format(s)
        c1G += " site:{}".format(s)
        c1Y += " site:{}".format(s)
        c1D += " site:{}".format(s)
        c1B += " site:{}".format(s)
        c1X += " site:{}".format(s)
        c1U += " site:{}".format(s)

        c2G += " allinurl:{}".format(s)
        c2Y += " url:{}".format(s)
        c2D += ""
        c2B += ""
        c2X += ""
        c2U += " allinurl:{}".format(s)

        c3G += " inurl:{}".format(s)
        c3Y += " inurl:{}".format(s)
        c3D += " inurl:{}".format(s)
        c3B += ""
        c3X += ""
        c3U += " inurl:{}".format(s)
    if f is not None:
        if ',' in f:
            x = f.split(',')
            for i in range(len(x)):
                c1G += " filetype:{}".format(x[i])
                c1Y += " filetype:{}".format(x[i])
                c1D += " filetype:{}".format(x[i])
                c1B += " filetype:{}".format(x[i])
                c1X += " filetype:{}".format(x[i])
                c1U += " filetype:{}".format(x[i])

                c2G += " ext:{}".format(x[i])
                c2Y += ""
                c2D += ""
                c2B += " ext:{}".format(x[i])
                c2X += ""
                c2U += ""

                c3G += " ext:{}".format(x[i])
                c3Y += ""
                c3D += ""
                c3B += " ext:{}".format(x[i])
                c3X += ""
                c3U += ""
                if i < len(x) - 1:
                    c1G += " AND"
                    c1Y += " AND"
                    c1D += " AND"
                    c1B += " AND"
                    c1X += " AND"
                    c1U += " AND"

                    c2G += " AND"
                    c2Y += ""
                    c2D += ""
                    c2B += " AND"
                    c2X += ""
                    c2U += ""

                    c3G += " AND"
                    c3Y += ""
                    c3D += ""
                    c3B += " AND"
                    c3X += ""
                    c3U += ""
        elif '.' in f:
            x = f.split('.')
            for i in range(len(x)):
                c1G += " filetype:{}".format(x[i])
                c1Y += " filetype:{}".format(x[i])
                c1D += " filetype:{}".format(x[i])
                c1B += " filetype:{}".format(x[i])
                c1X += " filetype:{}".format(x[i])
                c1U += " filetype:{}".format(x[i])

                c2G += " ext:{}".format(x[i])
                c2Y += ""
                c2D += ""
                c2B += " ext:{}".format(x[i])
                c2X += ""
                c2U += ""

                c3G += " ext:{}".format(x[i])
                c3Y += ""
                c3D += ""
                c3B += " ext:{}".format(x[i])
                c3X += ""
                c3U += ""
                if i < len(x) - 1:
                    c1G += " OR"
                    c1Y += " OR"
                    c1D += " OR"
                    c1B += " OR"
                    c1X += " OR"
                    c1U += " OR"

                    c2G += " OR"
                    c2Y += ""
                    c2D += ""
                    c2B += " OR"
                    c2X += ""
                    c2U += ""

                    c3G += " OR"
                    c3Y += ""
                    c3D += ""
                    c3B += " OR"
                    c3X += ""
                    c3U += ""
        else:
            cat2_out += " ext:{}".format(f)
            cat3_out += " ext:{}".format(f)
            c1G += " filetype:{}".format(f)
            c1Y += " filetype:{}".format(f)
            c1D += " filetype:{}".format(f)
            c1B += " filetype:{}".format(f)
            c1X += " filetype:{}".format(f)
            c1U += " filetype:{}".format(f)
            
            c2G += " ext:{}".format(f)
            c2Y += ""
            c2D += ""
            c2B += " ext:{}".format(f)
            c2X += ""
            c2U += ""

            c3G += " ext:{}".format(f)
            c3Y += ""
            c3D += ""
            c3B += " ext:{}".format(f)
            c3X += ""
            c3U += ""
    if k is not None:
        if ',' in k:
            x = k.split(',')
            for i in range(len(x)):
                cat1_out += ' "{}"'.format(x[i])
                cat2_out += ' "{}"'.format(x[i])
                cat3_out += ' "{}"'.format(x[i])
                if i < len(x) - 1:
                    c1G += " AND"
                    c1Y += " AND"
                    c1D += " AND"
                    c1B += " AND"
                    c1X += " AND"
                    c1U += " AND"

                    c2G += " AND"
                    c2Y += " AND"
                    c2D += " AND"
                    c2B += " AND"
                    c2X += " AND"
                    c2U += " AND"

                    c3G += " AND"
                    c3Y += " AND"
                    c3D += " AND"
                    c3B += " AND"
                    c3X += " AND"
                    c3U += " AND"
        elif '.' in k:
            x = k.split('.')
            for i in range(len(x)):
                cat1_out += ' "{}"'.format(x[i])
                cat2_out += ' "{}"'.format(x[i])
                cat3_out += ' "{}"'.format(x[i])
                c1G += ' "{}"'.format(x[i])
                c1Y += ' "{}"'.format(x[i])
                c1D += ' "{}"'.format(x[i])
                c1B += ' "{}"'.format(x[i])
                c1X += ' "{}"'.format(x[i])
                c1U += ' "{}"'.format(x[i])
                
                c2G += ' "{}"'.format(x[i])
                c2Y += ' "{}"'.format(x[i])
                c2D += ' "{}"'.format(x[i])
                c2B += ' "{}"'.format(x[i])
                c2X += ' "{}"'.format(x[i])
                c2U += ' "{}"'.format(x[i])

                c3G += ' "{}"'.format(x[i])
                c3Y += ' "{}"'.format(x[i])
                c3D += ' "{}"'.format(x[i])
                c3B += ' "{}"'.format(x[i])
                c3X += ' "{}"'.format(x[i])
                c3U += ' "{}"'.format(x[i]) 
                if i < len(x) - 1:
                    c1G += " OR"
                    c1Y += " OR"
                    c1D += " OR"
                    c1B += " OR"
                    c1X += " OR"
                    c1U += " OR"

                    c2G += " OR"
                    c2Y += " OR"
                    c2D += " OR"
                    c2B += " OR"
                    c2X += " OR"
                    c2U += " OR"

                    c3G += " OR"
                    c3Y += " OR"
                    c3D += " OR"
                    c3B += " OR"
                    c3X += " OR"
                    c3U += " OR"
        else:
            cat1_out += ' "{}"'.format(k)
            cat2_out += ' "{}"'.format(k)
            cat3_out += ' "{}"'.format(k)
            c1G += ' "{}"'.format(k)
            c1Y += ' "{}"'.format(k)
            c1D += ' "{}"'.format(k)
            c1B += ' "{}"'.format(k)
            c1X += ' "{}"'.format(k)
            c1U += ' "{}"'.format(k)

            c2G += ' "{}"'.format(k)
            c2Y += ' "{}"'.format(k)
            c2D += ' "{}"'.format(k)
            c2B += ' "{}"'.format(k)
            c2X += ' "{}"'.format(k)
            c2U += ' "{}"'.format(k)

            c3G += ' "{}"'.format(k)
            c3Y += ' "{}"'.format(k)
            c3D += ' "{}"'.format(k)
            c3B += ' "{}"'.format(k)
            c3X += ' "{}"'.format(k)
            c3U += ' "{}"'.format(k)

    if dork_types == 3:
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
    elif dork_types == 1:
        output_string += "GOOGLE:       {}\n".format(c1G)
        output_string += "YAHOO:        {}\n".format(c1Y)
        output_string += "DUCKDUCKGO:   {}\n".format(c1D)
        output_string += "BING:         {}\n".format(c1B)
        output_string += "YANDEX:       {}\n".format(c1X)
        output_string += "BAIDU:        {}\n".format(c1U)
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
    print("By GainSec https://github.com/GainSec/Dorker")
    print("")
    print("Credit to - JosephRC")
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
if s is not None or i is not None or a is not None:
    arg_count     += 1
    dork_types     = 3
    if s is not None:
        i = a = s
    elif i is not None:
        s = a = i
    elif a is not None:
        s = i = a 

# THIS IS ANOTHER FUNCTION
if f is not None or e is not None:
    arg_count += 1
    if dork_types < 2:
        dork_types = 2
    if f is not None:
        e = f
    elif e is not None:
        f = e

if k is not None:
    arg_count += 1
    if dork_types == 0:
        dork_types = 1

output()






# output(GLOBAL_STRING)