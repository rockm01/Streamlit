READ ME

1.	Understanding Streamlit:
1.1.	Streamlit is a python library that runs python code and displays in a browser window. The user interacts through the browser via prompted inputs. 
NOTE: the code executed is referencing the python file in real time. If the browser is open and the file is being edited, the browser functionality will update in real time as the code is edited. In other words, you don’t have to run a new instance of Streamlit to capture changes to code. This also means the execution can fail while the file is being updated.
2.	How streamlit works and how to get started:
2.1.	Install the streamlit package
2.1.1.	This can be done the same as any other streamlit package install. Go to your command prompt (CTRL+r, “cmd”) and type: pip install streamlit
2.2.	Create a python file
2.2.1.	This is what houses the code that is executed. It contains the streamlit API as an imported python package
2.3.	From the command prompt, run streamlit, pointing at the python file created above
EX: if the python file you created is “My_Streamlit_File”, then you’d run:
streamlit run My_Streamlit_File.py
2.3.1.	Once this script is ran, a local Streamlit server will be created in a new tab on your default web browser. This is where the user interaction occurs. This browser page is the GUI.
2.3.2.	You can also pass a URL. This allows you to connect to GitHub
streamlit run https://www.github.com/user/My_streamlit_file.py
2.3.3.	




Streamlit needs to be ran through the command prompt or anaconda prompt to setup the local URL. At time of execution, the python file needs to be specified.
