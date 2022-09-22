#!/usr/bin/env python3

# Written by Zac the Wise

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from simple_term_menu import TerminalMenu
import sys
import os.path

console = Console()

README_PATH = sys.argv[-1]
if not os.path.exists(README_PATH):
    print("Please specify the file location of the git-cheatsheet README file as an arguement!")
    sys.exit()


def get_main_options() ->  list:
    headings = []
    lines = get_content()
    for l in lines:
        # get h2 i.e. '##' headings
        if l.startswith("## "):
            l = l.replace("\n", "")
            l = l.replace("## ", "")
            headings.append(l)
    return headings


def get_sub_options(main_heading) -> list:
    sub_headings = []
    lines = get_content(no_newlines=True)
    line_index = lines.index(f"## {main_heading}")
    lines = lines[line_index:]
    for i, l in enumerate(lines):
        # get h3 i.e. '###' headings
        if l.startswith("## ") and i != 0:
            break
        if l.startswith("### "):
            l = l.replace("\n", "")
            l = l.replace("### ", "")
            sub_headings.append(l)
    return sub_headings


def render_main_menu():
    choices = get_main_options()
    main_menu = TerminalMenu(choices, title="Git topics:")
    result = main_menu.show()

    sub_choices = get_sub_options(choices[result])
    sub_menu = TerminalMenu(sub_choices, title="Available info:")
    sub_result = sub_menu.show()

    print_data(target=sub_choices[sub_result])


code_themes = [
    "default", "bw", "sas", "staroffice",
    "xcode", "github-dark"
]

def get_content(no_newlines=False):
    with open(README_PATH) as f:
        lines = f.readlines()
    if no_newlines:
        old_lines = lines
        lines = []
        for l in old_lines:
            l = l.replace("\n", "")
            lines.append(l)
            #for i in range(1,6):
            #    header = "#"*i
            #    if l.startswith(f"{header} "):
            #        l = l.replace(f"{header} ", "")
            #no_heading_lines.append(l)
        #return no_heading_lines
    return lines


def get_heading(target):
    lines = get_content()
    md_heading = f"### {target}"
    for l in lines:
        if md_heading in l:
            return lines.index(f"{md_heading}\n"), lines


def print_data(target):
    heading_line_no, lines = get_heading(target)
    lines = lines[heading_line_no:]
    good_lines = ""
    for i, l in enumerate(lines):
        if l.startswith("###"):
            l = l.replace("###", "##")  # make the heading h2
            if i != 0:  # the next command has been detected
                break
        good_lines += l
    # code themes https://pygments.org/styles/ [not all work, idk why]
    md = Markdown(good_lines,code_theme="native", style="justify left")
    console.print(md)


render_main_menu()
