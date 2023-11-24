import streamlit as st
import requests



st.title('Potentia P4')

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

api_choice = st.selectbox("Choose your API", ["gpt4", "claude2"])

use_default_prompt = st.checkbox("Default Prompt", value=True)

default_text = """Cite an example of having had to make business decisions that conflicted with your values during your career.
    · The scenario/ context
    · What was the situation/ issue/ problem/ challenge
    · Who else was involved
    · The decision you had to make/ action you had to take
    · The personal value(s) you hold dear had to be ignored/ compromised  in the process
    · The reason why you had to do it (e.g., perhaps, in the interest of a larger business goal)
    · What was the impact of your decision or action

    I would like you to help me provide the following requirements for a student's response that will be given. IF you do not have enough information for any of these requirement, you can leave that empty. 
    First Name) The first name of the student mentioned in the response
    Last Name) The last name or surname of student mentioned in the response
    Email id) The email id of student mentioned in the response
    Student ID) The eight digit PGID ID of the student mentioned in the response.
    Case summary)   Case summary in 2-4 sentences
    Student’s values)   Student’s values visible through the narrative
    Value Conflict) The Value Conflict the student faced in the given scenario
    Attribution)    The moral or ethical compromise in the case can be attributed to which of the seven moral disengagement mechanisms, viz. Moral Justification, Advantageous Comparison, Displacement of responsibility, Diffusion of responsibility, Distorting consequences, Dehumanization (Reduced identification with the victims), or Attribution of blame to victims
    Excerpt values) 1-4 sentence excerpt that highlights the importance of values for the student
    Excerpt succumb)    1-4 sentence excerpt that denotes the aspect on which the student succumbed 
    Excerpt Rationale)  1-4 sentence excerpt that highlights the rationale provided by the student that justified her/ his moral disengagement
    Excerpt impact) 1-4 sentence excerpt that demonstrates the internal/ emotional/ psychological impact on the individual
    Evaluate the student on a 10-point scale keeping in view the clarity and coherence of the narrative considering the following 
    Understandability Evaluation) Understandability for the reader – the scenario/ context, the situation/ problem/ issue, other actors involved, the decision they had to take  score the student out of 3 points
    Identification evaluation)  Identification or indication of the value they held that got compromised and authentic/ coherent expression of it score the student out of 3 points
    rationale evaluation).  The rationale they had to do it                 ,score the student out of 2 points
    impact evaluation)  The impact it had on them and their organisation    ,score the student out of 2 points
    total marks) The sum of understandability evaluation, identification evaluation, rationale evaluation and impact evaluation.
    Feedback)   2-4 sentence feedback for the student, including what they may have done to score even better"""

default_open_ai_key = "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"
default_anthropic_key = "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"


if use_default_prompt:
    prompt_text = st.text_area("requirement", value=default_text, disabled=True)
    open_ai_key = st.text_area("Open AI key", value=default_open_ai_key, disabled=True)
    anthropic_key = st.text_area("Anthropic Key", value=default_anthropic_key, disabled=True)
else:
    prompt_text = st.text_area("requirement", value=f"{default_text}")
    open_ai_key = st.text_area("Prompt Text", value=f"{default_open_ai_key}")
    anthropic_key = st.text_area("Prompt Text", value=f"{default_anthropic_key}")


def call_api_and_get_csv(uploaded_files, api_url):
    # Prepare the files for uploading
    files = [('files', (uploaded_file.name, uploaded_file, uploaded_file.type)) for uploaded_file in uploaded_files]


    # Making a POST request to the API
    response = requests.post(api_url, files=files)

    return response

api_url = f"http://34.234.91.27/upload_files_c4/?passed_engine={api_choice}&passed_key_openai={open_ai_key}&passed_key_anthropic={anthropic_key}&passed_requirement={prompt_text}"



if st.button("Submit"):
    if uploaded_files:
        try:
            response = call_api_and_get_csv(uploaded_files, api_url = api_url)
            st.download_button(label="Download CSV file", data=response.content, file_name="downloaded_file.csv", mime='text/csv')
        except:
            try:
                response = call_api_and_get_csv(uploaded_files, api_url = api_url)
                st.download_button(label="Download CSV file", data=response.content, file_name="downloaded_file.csv", mime='text/csv')
            except:
                try:
                    response = call_api_and_get_csv(uploaded_files, api_url = api_url)
                    st.download_button(label="Download CSV file", data=response.content, file_name="downloaded_file.csv", mime='text/csv')
                except:
                    try:
                        response = call_api_and_get_csv(uploaded_files, api_url = api_url)
                        st.download_button(label="Download CSV file", data=response.content, file_name="downloaded_file.csv", mime='text/csv')
                    except:
                        try:
                            response = call_api_and_get_csv(uploaded_files, api_url = api_url)
                            st.download_button(label="Download CSV file", data=response.content, file_name="downloaded_file.csv", mime='text/csv')
                        except:
                            st.write("failed due to incorrect number of columns from LLM")
                            
