import time #Iwish
import os
import json
import requests
import streamlit as st
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
import google.generativeai as genai


def main():
    # Set page configuration
    st.set_page_config(
        page_title="Alwrity - AI YouTube Script Generator (Beta)",
        layout="wide",
    )
    # Remove the extra spaces from margin top.
    st.markdown("""
        <style>
                ::-webkit-scrollbar-track {
        background: #e1ebf9;
        }

        ::-webkit-scrollbar-thumb {
            background-color: #90CAF9;
            border-radius: 10px;
            border: 3px solid #e1ebf9;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #64B5F6;
        }

        ::-webkit-scrollbar {
            width: 16px;
        }
        div.stButton > button:first-child {
            background: #1565C0;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            font-weight: bold;
        }
        </style>
    """
    , unsafe_allow_html=True)

    # Hide top header line
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    # Hide footer
    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

    st.title("Alwrity - AI YouTube Script Writer")
    st.markdown("Create engaging, high-converting YouTube scripts effortlessly with our AI-powered script generator. 🎬✨")
    
    with st.expander("**PRO-TIP** - Better input yield, better results. 📌", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        
        with col1:
            main_points = st.text_area(
                '**What is your video about? 🎥**',
                placeholder='Write a few lines on your video idea (e.g., "New trek, Latest in news, Finance, Tech...")',
                help="Describe the idea of the whole content in a single sentence. Keep it between 1-3 sentences."
            )
            tone_style = st.selectbox(
                '**Select Tone & Style 🎭**', 
                ['Casual', 'Professional', 'Humorous', 'Formal', 'Informal', 'Inspirational'],
                help="Choose the tone and style that best fits your video."
            )
            target_audience = st.multiselect(
                '**Select Video Target Audience 🎯 (One or Multiple)**',
                [
                    'Beginners', 'Marketers', 'Gamers', 'Foodies', 'Entrepreneurs', 'Students',
                    'Parents', 'Tech Enthusiasts', 'General Audience', 'News article', 'Finance Article'
                ],
                help="Select one or more target audiences for your video."
            )
        
        with col2:
            video_length = st.selectbox(
                '**Select Video Length ⏰**',
                [
                    'Short (1-3 minutes)', 'Medium (3-5 minutes)', 
                    'Long (5-10 minutes)', 'Very Long (10+ minutes)'
                ],
                help="Choose the desired length of your video."
            )
            language = st.selectbox(
                '**Select Language 🌐**',
                [
                    'English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Other'
                ],
                help="Select the language for your video script."
            )
            if language == 'Other':
                custom_language = st.text_input(
                    '**Enter your preferred language**', 
                    placeholder='e.g., Italian, Portuguese...',
                    help="Specify your preferred language if not listed above."
                )
                language = custom_language

            use_case = st.selectbox(
                '**YouTube Script Use Case 📚**',
                [
                    'Tutorials', 'Product Reviews', 'Explainer Videos', 'Vlogs', 'Motivational Speeches', 
                    'Comedy Skits', 'Educational Content'
                ],
                help="Select the use case that best describes your video."
            )

    if st.button('**Write YT Script 📝**'):
        with st.spinner("Assigning AI professional to write your YT script... ⏳"):
            if not main_points:
                st.error("🚫 Please provide all required inputs.")
            else:
                response = generate_youtube_script(target_audience, main_points, tone_style, video_length, use_case, language)
                if response:
                    st.subheader('**🧕👩 Your Final YouTube Script! 📜**')
                    st.write(response)
                    st.write("\n\n\n\n\n\n")
                else:
                    st.error("💥 Failed to write the script. Please try again!")


def generate_youtube_script(target_audience, main_points, tone_style, video_length, use_case, language):
    """ Generate YouTube script generator """
    prompt = f"""
    Please write a YouTube script in {language} for a video about {main_points} based on the following information:

    Target Audience: {', '.join(target_audience)}

    Main Points: {', '.join(main_points)}

    Tone and Style: {tone_style}

    Video Length: {video_length}

    Specific Instructions:

    * Include a strong hook to grab attention at the start.
    * Structure the script with clear sections and headings.
    * Provide engaging introductions and conclusions for each section.
    * Use clear and concise language, avoiding jargon or overly technical terms.
    * Tailor the language and tone to the target audience.
    * Include relevant examples, anecdotes, and stories to make the video more engaging.
    * Add questions to encourage viewer interaction and participation.
    * End the script with a strong call to action, encouraging viewers to subscribe, like the video, or visit your website.

    Use Case: {use_case}

    Output Format:

    Please provide the script in a clear and easy-to-read format. 
    Include clear headings for each section and ensure that all instructions are followed.
    """
    
    try:
        response = generate_text_with_exception_handling(prompt)
        return response
    except Exception as err:
        st.error(f"Exit: Failed to get response from LLM: {err}")
        return None


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_text_with_exception_handling(prompt):
    """
    Generates text using the Gemini model with exception handling.

    Args:
        api_key (str): Your Google Generative AI API key.
        prompt (str): The prompt for text generation.

    Returns:
        str: The generated text.
    """

    try:
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

        generation_config = {
            "temperature": 1,
            "top_p": 0.7,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)

        convo = model.start_chat(history=[])
        convo.send_message(prompt)
        return convo.last.text

    except Exception as e:
        st.exception(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
