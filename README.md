## Alwrity: AI YouTube Script Writer 🎬✨ 

**Effortlessly create engaging and high-converting YouTube scripts with Alwrity's AI-powered script generator.** 

This Streamlit app uses Google's Gemini AI to help you turn your video ideas into polished YouTube scripts, complete with a captivating hook, clear structure, engaging introductions and conclusions, and a compelling call to action. 

**Features:**

* **AI-Powered Script Generation:** Let Gemini AI do the heavy lifting, crafting YouTube scripts tailored to your video's content and target audience.
* **Customizable Settings:**  Fine-tune your script by selecting the desired tone, style, video length, language, and target audience. 
* **Engaging Storytelling:** Gemini AI will generate scripts with a strong hook, clear sections, engaging introductions, and a call to action. 
* **User-Friendly Interface:** The Streamlit app makes it easy for anyone to create professional-quality YouTube scripts.

**Getting Started:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/alwrity-youtube-script-writer.git
   ```
2. **Install Dependencies:**
   ```bash
   cd alwrity-youtube-script-writer
   pip install -r requirements.txt
   ```
3. **Create a `.env` File:**
   - Create a file named `.env` in the project directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
     ```
4. **Run the App:**
   ```bash
   streamlit run main.py
   ```

**Usage:**

1. **Provide Your Video Details:**
   - **What is your video about? 🎥:**  Write a brief description of your video's content (e.g., "New trek, Latest in news, Finance, Tech..."). 
   - **Select Tone & Style 🎭:**  Choose the tone that best fits your video (e.g., "Casual," "Professional," "Humorous," etc.).
   - **Select Video Target Audience 🎯:**  Choose one or more target audiences for your video (e.g., "Beginners," "Gamers," "Foodies," etc.).
   - **Select Video Length ⏰:** Choose the desired length of your video.
   - **Select Language 🌐:**  Select the language for your video script.
   - **YouTube Script Use Case 📚:**  Select the type of video you're creating (e.g., "Tutorials," "Product Reviews," "Explainer Videos," etc.).

2. **Click "Write YT Script 📝":**  The app will use Gemini to generate a YouTube script based on your input.

3. **Review and Edit:**  The AI-generated script will be displayed, allowing you to review and make any necessary changes.

**Additional Notes:**

* This app requires a Google Gemini API key.
* You can adjust the AI's behavior and output by modifying the prompt in the `generate_youtube_script` function. 
* The app is currently in beta, so you may encounter some limitations.  Feedback is always welcome!

**Contributing:**

Contributions to this project are welcome! Feel free to open an issue or submit a pull request.
