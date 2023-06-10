# Know your CSV 
## LangChain-based App

The application enables user to upload CSV file and get insights from it by supplying inputs. 
It leverages the LLM provided by OpenAI and the LangChain framework.

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
OPENAI_API_KEY = 'YOUR_OPENAI_KEY'
```
### Run application
```
$ (venv) streamlit run agent_app.py
```

On opening the app in localhost, upload the CSV file and start interacting with the Agent to know more about the data it holds.

![Alt Text](https://github.com/devashishk99/prompt-engg/blob/main/openai/img/prmp1.png)

In the terminal, you can observe the way the csv agent thinks behind the output.

![Alt Text](https://github.com/devashishk99/prompt-engg/blob/main/openai/img/chain1.png)
