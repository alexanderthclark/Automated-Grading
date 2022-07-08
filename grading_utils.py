import numpy as np
import pandas as pd
import inspect
import sys

def highlight_wrong(s, solutions, props = ''):
    return np.where(s != solutions, props, '')

def test_function(student, f, inputs, unpack = False):
    
    df = pd.DataFrame()
    df.index.name = 'input'
    
    for i in inputs:
        j = str(i).replace("{",'\{').replace("}","\}")
        df.loc[j,'Expected Output'] = str(f(i))
        
        try:
            your_output = str(student(i))
            ex_value = ''
        except:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            your_output = ex_type.__name__
        
        df.loc[j, 'Your Output'] = your_output
            
        try:
            passed = f(i) == student(i) # might use `is` depending on application
        except:
            passed = False
            
        result = (passed) * (r"\cellcolor{green!10}" + r'passed')
        result += (not passed) * (r"\cellcolor{red!10}" + str(ex_value)[0:50])
        df.loc[j, 'Result'] = result   
        
    return df.style.to_latex(hrules = True)

def programming_output(temp, temp_answer, test_inputs, body): 
	table_tex = test_function(temp, temp_answer, test_inputs)
	body += table_tex

	body += r"""
\bigskip
\noindent Your Code
\begin{lstlisting}""" + """
""" + inspect.getsource(temp) + """
\end{lstlisting}"""

	body += r"""
\bigskip
\noindent One Solution
\begin{lstlisting}""" + """
""" + inspect.getsource(temp_answer) + """
\end{lstlisting}"""

	return body
