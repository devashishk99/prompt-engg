
# Know your CSV 
## LangChain-based App using OpenSource LLM

The application enables user to upload CSV file and get insights from it by supplying inputs. 
It leverages the Falcon LLM provided by HuggingFace and the LangChain framework.

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/devashishk99/prompt-engg.git
$ cd prompt-engg
$ python3 -m venv venv
```
### Activate virtual environment
Mac / Linux:
```
. venv/bin/activate
```
Windows:
```
venv\Scripts\activate
```
Install dependencies
```
$ pip install -r requirements.txt 
```
Create .env file 
```
HUGGINGFACEHUB_API_TOKEN = 'YOUR_HUGGINGFACEHUB_API_TOKEN'
```
### Run application
```
$ (venv) streamlit run falcon_csv_agent.py
```
