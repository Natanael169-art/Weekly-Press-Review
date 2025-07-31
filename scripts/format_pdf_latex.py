import fitz  # PyMuPDF
import re

def escape_latex(text):
    replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
    }
    regex = re.compile('|'.join(re.escape(key) for key in replacements.keys()))
    return regex.sub(lambda match: replacements[match.group()], text)

input_pdf = "Weekly_Press_Review.pdf"
tex_file = "press_review.tex"

doc = fitz.open(input_pdf)
lines = []

for(tex_file, "w", encoding="utf-8") as f:
    f.write(r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{margin=2.5cm}
\title{Weekly Press Review}
\date{}
\begin{document}
\maketitle
""")

    for line in lines:
        line = line.strip()
        escaped_line = escape_latex(line)

        if line.startswith("===") and line.endswith("==="):
           {{{company}}}\n")

        elif line.startswith("·") or line.startswith("•"):
            article_title = escape_latex(line.strip("·• "))
            f.write(f"\\subsection*{{{article_title}}}\n")

        elif "http" in line:
            f.write(f"\\href{{{escaped_line}}}{{Link}}\n\n")

        elif line:
            f.write(escaped_line + "\n\n")

    f.write("\\end{document}")
