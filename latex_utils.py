def make_preamble(student_id):
    """Return the LaTeX preamble for *student_id*'s report."""

    preamble = r"""
\documentclass[11pt]{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{textwidth = 6.5in, top = 1.1in}

\usepackage{color}
\usepackage{listings}
\usepackage[table]{xcolor}
\usepackage{colortbl}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{etoolbox}
\usepackage{multirow}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
backgroundcolor=\color{backcolour},   
commentstyle=\color{codegreen},
keywordstyle=\color{magenta},
numberstyle=\tiny\color{codegray},
stringstyle=\color{codepurple},
basicstyle=\ttfamily\footnotesize,
breakatwhitespace=false,         
breaklines=true,                 
captionpos=b,                    
keepspaces=true,                 
numbers=left,                    
numbersep=5pt,                  
showspaces=false,                
showstringspaces=false,
showtabs=false,                  
tabsize=2,
language = Python
}

\lstset{style=mystyle}

%\title{"""+student_id+r""" }
%\author{Midterm}% \\ \footnotesize{\textit{Midterm}}}
%\date{\today}

\begin{document}
%\maketitle
\pagenumbering{arabic}

\begin{center}
\Large{\textbf{"""+student_id+r"""} \\
\textit{Midterm Results}}
    
\bigskip 
% Include Columbia U crown
%\includegraphics[width = 4mm]{crown_dark.png}

\large\emph{\today}
\end{center}

"""
    return preamble

end = r"""
\end{document}"""