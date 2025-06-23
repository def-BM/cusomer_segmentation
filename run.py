import os
import subprocess

# Path to your notebook
notebook_path = "notebook/DSprojectSem6.ipynb"

# run the notebook 
print("Running the notebook...")
subprocess.run(["python","-m ","jupyter", "nbconvert", "--execute", "--inplace", notebook_path])

# Automatically run the Streamlit app
subprocess.run(["python","-m","streamlit", "run", "Scripts/app.py"])
