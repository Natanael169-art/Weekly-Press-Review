import fitz  # PyMuPDF

input_pdf = "weekly_press_review 11.pdf"
tex_file = "press_review.tex"

doc = fitz.open(input_pdf)
lines = []

for page in doc:
    text = page.get_text("text")
    lines.extend(text.splitlines())

doc.close()

with open(tex_file, "w", encoding="utf-8") as f:
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

        if line.startswith("===") and line.endswith("==="):
            company = line.strip("= ").title()
            f.write(f"\\section*{{{company}}}\n")

        elif line.startswith("·"):
            article_title = line.strip("· ").replace("&", "\\&")
            f.write(f"\\subsection*{{{article_title}}}\n")

        elif "http" in line:
            f.write(f"\\href{{{line}}}{{Link}}\n\n")

        elif line:
            f.write(line.replace("&", "\\&") + "\n\n")

    f.write("\\end{document}")
