# Screen Interpreting Assistant (SIA)

> A voice-based assistant designed to enhance web accessibility for visually impaired users.  

---

## Project Overview

Web accessibility remains a challenge for visually impaired users.  
Traditional **Screen Readers (SRs)** are often either too verbose or unable to capture all webpage content.  
To overcome this, **Screen Interpreting Assistant (SIA)** combines:

-  **Voice Recognition**  
-  **Natural Language Processing (NLP)**  
-  **Web Automation (Selenium)**  

allowing users to **interact with websites using only voice commands**.  

---

##  Features

- **Website Analysis**:  
  Understands diverse webpage structures, designs, and HTML elements.  

- **Content Understanding**:  
  Uses NLP to comprehend and summarize information.  

- **Voice Interaction**:  
  Hands-free browsing with intuitive voice commands.  

- **Task Execution**:  
  Perform actions like navigation, search, and interaction with webpage elements.  

- **Adaptive Learning**:  
  Learns user preferences for improved experience.  

- **Contextual Awareness**:  
  Maintains context for meaningful interactions.  

- **Accessibility Across Platforms**:  
  Works with e-commerce, social media, educational, and government portals.  

---

##  Target Users

- **Visually Impaired Users**: Navigate websites using only voice.  
- **Users with Motor Disabilities**: Voice-only control for accessibility.  
- **E-commerce Users**: Inclusive online shopping experience.  
- **General Web Users**: Hands-free browsing with voice.  
- **Multilingual Users**: Interaction in different languages.  

---

##  Technologies Used

- Python  
- SpeechRecognition  
- pyttsx4 (Text-to-Speech)  
- Selenium (Web Automation)  
- Raspberry Pi + Microphone + Speaker  

---

##  System Requirements

- Raspberry Pi (≥ 2GB RAM)  
- Microphone 
- Speaker 
- Stable Internet Connection 

---

##  Algorithm (Step by Step)

1. Start  
2. Capture user voice command  
3. Analyze command using NLP  
4. If clarification needed → ask user → return to step 2  
5. If quit command → stop  
6. Open browser / connect to the internet  
7. Load and analyze webpage  
8. Perform requested action (navigation, search, interaction)  
9. Give output through voice response  
10. Return to step 2  

---

##  Design Components

- **Use Case Diagram**: Shows interaction between user, assistant, and webpage.  
- **State Diagram**: Represents assistant’s listening, analyzing, executing, and responding states.  
- **Sequence Diagram**: Flow of commands from user → assistant → webpage → response.  
- **Flowchart**: Algorithm execution steps.  

---

##  Implementation

- Speech commands processed with **SpeechRecognition**  
- Browser controlled with **Selenium**  
- Text-to-Speech handled with **pyttsx4**  
- Hardware setup: **Raspberry Pi + Mic + Speaker**  
- Cloud connectivity for portability  

---

##  Outputs

- Successful interaction with **Amazon e-commerce website**  
- Voice-controlled navigation and product search  
- Responses generated vocally through the assistant  

---

##  Non-Functional Requirements

- **Performance**: Response time < 1 second, scalable system.  
- **Usability**: Intuitive and user-friendly interface with customizable preferences.  
- **Reliability**: High availability, error handling, and data backup support.  

---

##  Results

- Works effectively for **Amazon** and similar structured websites.  
- Hardware device developed to run independently without a PC.  

---

##  Current Limitations

-  Cannot handle **CAPTCHA**  
-  Difficulty with **OTP authentication**  
-  Struggles with **dynamic elements** (dropdowns, popups, sliders)  
-  Password & sensitive data handling challenges  

---

##  Future Scope

- Extend support to multiple websites 
- Real-time **object detection and recognition**  
- Act as a **personal assistant** for visually impaired users  

---

##  References

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)  
- [Selenium](https://pypi.org/project/selenium/)  
- [pyttsx4](https://pypi.org/project/pyttsx4/)  
- [ChromeDriver](https://chromedriver.chromium.org/downloads)  
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#content)  
- [Chrome User Manual](https://support.google.com/a/users/answer/9310144?hl=en)  
- [Output Reference Video](https://drive.google.com/file/d/10U0--IDorKX5XFFJA7IJmIxuA2mIG0E8/view?usp=drive_link)  

---

##  Author

**Uday Sankar Gottipalli**  
B.Tech CSE, RGUKT Srikakulam

---

##  Installation & Setup

Clone the repository:

```bash
git clone https://github.com/usagopro/SIA.git

