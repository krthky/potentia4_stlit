import streamlit as st
import requests

gpt_prompt = """I teach a course, “Corporate Governance and Business Ethics”, to Executive MBA students who bring about 6-16 years of work experience in Managerial and leadership positions. 
I gave them the following assignment.

Cite an example of having had to make business decisions that conflicted with your values during your career.
· The scenario/ context
· What was the situation/ issue/ problem/ challenge
· Who else was involved
· The decision you had to make/ action you had to take
· The personal value(s) you hold dear had to be ignored/ compromised  in the process
· The reason why you had to do it (e.g., perhaps, in the interest of a larger business goal)
· What was the impact of your decision or action

I would like you to help me provide the following for a student's response. 
'First Name') The First Name of the student
'Last Name' ) The last name or surname mentioned in response if available else blank
'Email') Identify the email id which is mentioned in the document, if not found leave empty
'Student ID') The 8-digit student PGID of the student mentioned in the response
'Case Summary')	Case summary in 2-4 sentences
'Company Name') The name of the company associated with the student if mentioned else leave empty
'Industry Segment') Industry segment if available else leave empty 
'Student Values')	Student’s values visible through the narrative, separated by a comma
'Value Conflict')	The Value Conflict the student faced in the given scenario
'Attribution')	The moral or ethical compromise in the case can be attributed to which of the seven moral disengagement mechanisms, viz. Moral Justification, Advantageous Comparison, Displacement of responsibility, Diffusion of responsibility, Distorting consequences, Dehumanization (Reduced identification with the victims), or Attribution of blame to victims
'Excerpt Values')	1-4 sentence excerpt that highlights the importance of values for the student
'Excerpt Succumb')	1-4 sentence excerpt that denotes the aspect on which the student succumbed 
'Excerpt Rationale')	1-4 sentence excerpt that highlights the rationale provided by the student that justified her/ his moral disengagement
'Excerpt Impact')	1-4 sentence excerpt that demonstrates the internal/ emotional/ psychological impact on the individual

Evaluate the student on a 10-point scale keeping in view the clarity and coherence of the narrative considering the following elements of Evaluation 
'Understandability Evaluation'.	Understandability for the reader – the scenario/ context, the situation/ problem/ issue, other actors involved, the decision they had to take  -- out of 3 points
'Value Identification Evaluation'.	Identification or indication of the value they held that got compromised and authentic/ coherent expression of it 			-- out of 3 points
'Rationale Evaluation'.	The rationale they had to do it 				-- out of 2 points
'Impact Evaluation'.	The impact it had on them and their organisation 	-- out of 2 points
'Total Score' This is the sum of the scores for 'Impact Evaluation', 'Rationale Evaluation', 'Value Identification Evaluation' and 'Understandability Evaluation'

'Feedback')	2-4 sentence feedback for the student, including what they may have done to score even better

Response of student is provided enclosed in brackets"""
claude_prompt = """I teach a course, “Corporate Governance and Business Ethics”, to Executive MBA students who bring about 6-16 years of work experience in Managerial and leadership positions. 
I gave them the following assignment enclosed in angled brackets <Cite an example of having had to make business decisions that conflicted with your values during your career.
· The scenario/ context
· What was the situation/ issue/ problem/ challenge
· Who else was involved
· The decision you had to make/ action you had to take
· The personal value(s) you hold dear had to be ignored/ compromised  in the process
· The reason why you had to do it (e.g., perhaps, in the interest of a larger business goal)
· What was the impact of your decision or action

>. 
I shall also provide the Students response enclosed in brackets and I need you to provide the following strictly in JSON format without adding any other text - [
1)'First Name' - The First Name of the student
2) 'Last Name' - The last name or surname mentioned in response if available else blank
3)'Email' - Identify the email id which is mentioned in the document, if not found leave empty
4)'Student ID' - The 8-digit student PGID of the student mentioned in the response
5)'Case Summary' - Case summary in 2-4 sentences
6)'Company Name' - The name of the company associated with the student if mentioned else leave empty
7)'Industry Segment' - Industry segment if available else leave empty 
8)'Student Values' - Student’s values visible through the narrative, separated by a comma
9)'Value Conflict' -  The Value Conflict the student faced in the given scenario
10) 'Attribution' - The moral or ethical compromise in the case can be attributed to which of the seven moral disengagement mechanisms, viz. Moral Justification, Advantageous Comparison, Displacement of responsibility, Diffusion of responsibility, Distorting consequences, Dehumanization (Reduced identification with the victims), or Attribution of blame to victims
11)'Excerpt Values' -  1-4 sentence excerpt that highlights the importance of values for the student
12)'Excerpt Succumb' -  1-4 sentence excerpt that denotes the aspect on which the student succumbed 
13)'Excerpt Rationale' - 1-4 sentence excerpt that highlights the rationale provided by the student that justified her/ his moral disengagement
14)'Excerpt Impact' - 1-4 sentence excerpt that demonstrates the internal/ emotional/ psychological impact on the individual

 Evaluate the student on a 10-point scale keeping in view the clarity and coherence of the narrative considering the following elements of Evaluation 
15)'Understandability Evaluation' - Understandability for the reader – the scenario/ context, the situation/ problem/ issue, other actors involved, the decision they had to take  -- out of 3 points
16) 'Value Identification Evaluation' - Identification or indication of the value they held that got compromised and authentic/ coherent expression of it           -- out of 3 points
17) 'Rationale Evaluation' - The rationale they had to do it                 -- out of 2 points
18) 'Impact Evaluation' - The impact it had on them and their organisation    -- out of 2 points
19) 'Total Score' - This is the sum of the scores for 'Impact Evaluation', 'Rationale Evaluation', 'Value Identification Evaluation' and 'Understandability Evaluation'

20) 'Feedback') 2-4 sentence feedback for the student, including what they may have done to score even better
Response of student is provided enclosed in the square brackets
]"""

st.title('Potentia P4')

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

api_choice = st.selectbox("Choose your API", ["OpenAI GPT-4-Turbo", "Claude - 2"])

use_default_prompt = st.checkbox("Default Prompt", value=True)

default_text = f"{gpt_prompt}" if api_choice == "OpenAI GPT-4-Turbo" else f"{claude_prompt}"


if use_default_prompt:
    prompt_text = st.text_area("Prompt Text", value=default_text, disabled=True)
else:
    prompt_text = st.text_area("Prompt Text", value=f"{default_text}")

def call_api_and_get_csv(uploaded_files, prompt, api_url):
    # Prepare the files for uploading
    files = [('files', (uploaded_file.name, uploaded_file, uploaded_file.type)) for uploaded_file in uploaded_files]

    # Add the prompt if available
    data = {'prompt': prompt}

    # Making a POST request to the API
    response = requests.post(api_url, files=files, data=data)

    return response

api_url = 'http://54.206.196.250/uploadfiles_openai_csv' if api_choice == "OpenAI GPT-4-Turbo" else 'http://54.206.196.250/uploadfiles_claude_csv'

if st.button("Submit"):
    if uploaded_files:
        response = call_api_and_get_csv(uploaded_files, prompt = prompt_text, api_url = api_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Create a download button for the CSV file
            st.download_button(label="Download CSV file", data=response.content, file_name="downloaded_file.csv", mime='text/csv')
        else:
            st.error(f"Failed to download CSV file. Status code: {response.status_code}")
