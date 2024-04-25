# Guardian Vision

<p> <img src="https://user-images.githubusercontent.com/124444723/233845771-bd346166-71c1-4213-a015-9ce94515c755.jpg" alt="Guardian Vision Logo" width="100px" height="100px" style="background: #fff;"> </p>

<p> Violence detection ML model to detect suspicious activities in real-time through CCTV or any camera, and send immediate alert to the respective authorities. </p>

<p align='center'><img src="static\images\WhatsApp Image 2023-04-24 at 01.06.23.jpg" alt="Weapon Detection" width="800"></p>
## Overview 🤖

The project aims to develop a system for violence detection using CCTV footage and providing an immediate alert to the police. The system will use advanced image processing and machine learning techniques to analyze the CCTV footage in real-time and detect any violent behavior or actions. Once detected, an automatic alert will be sent to the police, enabling them to respond quickly and take appropriate action. The system has the potential to enhance public safety and reduce crime rates in public areas.

## Usage

To use this project, you need to have a webcam connected to your computer. The project will capture the video stream from the webcam and analyze it for any violent activities. If any violence is detected, the project will send an alert to the respective authorities with the location and timestamp of the incident.

## Features 🦾

- Weapon Detection
- Light/dark mode toggle
- Enhance the user experience creating highly reactive website.

## Flow of the Project 💻

<li>  Home Page</li>  
 <p>This page help new user to understand our facilities and how our guardian vision works.It provides offer and This deviate user to our 
 user login page.</p>

<li>  Create Account</li>  
<p> Helps us to create account  in our platform.</p>

<li>  User Login</li>  
<p>The user log in to the platform using their registered email and password.</p>

<li>  User Interface</li>  
<p>The logged in user ca use our services of using his Webcam for Real-time AI detection of physical violence or can upload a video where the AI detects if there is any physical violence present in it.</p>

<li>  Webcam Page</li>  
<p>The User can give the email of his friends and family. Once the webcam start if any voilence detected ,it sends alert to all respective authorities along with the given emails by the User.</p>

<li>  Video upload Page</li>  
<p>The User can upload any video in our website after which the AI detects if there is any violence in it. If there is any suspicious activity present in it, the AI sends a image of that particular frame.</p>

## Tech Stack 🧑🏻‍💻

### Client:
- Next JS
- HTML
- CSS
- JavaScript
- Bootstrap

### Server:
- JSON
- Node
- Twilio

### Machine Learning:
- Python
- Flask
- Yolo Models


## Installation

1. Install required packages for JSON server with npm \*Path should be the directory where Project is present

```bash
  npm i
  npm init -y
  npm install -g json-server
```

2. To Run the json-server

```bash
  npm start
```
Or
```bash
  json-server --watch ./database/db.json --port 8000
```

3. Install the Basic libaray in a **new terminal**

```bash
   pip install -r ./requirements.txt
```

4. Run app.py file

```bash
   python app.py
```
## Inspiration
The inspiration behind Guardian-Vision stemmed from the pressing need to enhance public safety and security in an increasingly complex world. With the rise in incidents involving concealed weapons and knives, we recognized the importance of developing a proactive solution to detect and mitigate such threats before they escalate.

## What it does

Guardian-Vision operates by analyzing video streams from surveillance cameras in real-time. The system employs state-of-the-art object detection algorithms to identify and flag potential threats, such as guns or knives, in the camera's field of view.

<p align="center">
  <img src="https://raw.githubusercontent.com/umeshSinghVerma/Guardian-Vision/main/Screenshot%202024-04-25%20204949.png" alt="Weapon Detection" width="400">
  <img src="https://raw.githubusercontent.com/umeshSinghVerma/Guardian-Vision/main/Screenshot%202024-04-25%20205059.png" alt="Knife Detection" width="400">
</p>



When a weapon or knife is detected, Guardian-Vision triggers immediate alerts, notifying designated authorities via email and WhatsApp. These alerts include a snapshot of the suspicious individual carrying the weapon, along with the system's confidence level in the detection accuracy.

<p align="center">
  <img src="https://raw.githubusercontent.com/umeshSinghVerma/Guardian-Vision/main/Screenshot%202024-04-25%20205014.png" alt="Weapon Detection" width="400">
  <img src="https://raw.githubusercontent.com/umeshSinghVerma/Guardian-Vision/main/Screenshot%202024-04-25%20205123.png" alt="Knife Detection" width="400">
</p>


Furthermore, Guardian-Vision offers seamless integration with existing security infrastructure, allowing for swift response and appropriate action. Authorities can access the real-time video feed and additional information to assess the situation and take necessary measures to ensure public safety.

## How we built it
We built Guardian-Vision using a combination of open-source computer vision libraries, machine learning frameworks, and API integrations. The system was trained on a diverse dataset of weapon images to ensure robust detection capabilities. Real-time camera feeds are analyzed for potential threats, and alerts are triggered accordingly. Integration with email and WhatsApp was achieved to enable seamless communication with authorities.

## Challenges we ran into
Building Guardian-Vision presented several challenges, including:
- *Data Collection:* Obtaining a diverse and representative dataset of weapon images for training proved to be challenging.
- *Model Optimization:* Fine-tuning the detection model to achieve high accuracy while maintaining real-time performance required extensive experimentation.
- *Integration Complexity:* Integrating email and WhatsApp functionality into the system posed integration challenges due to the need for real-time communication.

## Accomplishments that we're proud of
Despite the challenges, we successfully developed Guardian-Vision, a reliable and effective security solution. We're proud to have created a system that has the potential to significantly enhance public safety and security in various settings, from public spaces to high-security facilities.

## What we learned
Throughout the development process, we gained invaluable insights into the capabilities and limitations of computer vision algorithms for object detection. We also learned about the complexities of integrating multiple technologies, such as camera systems, email, and messaging platforms, into a cohesive solution.

## What's next for Guardian-Vision
Looking ahead, we plan to further refine and optimize Guardian-Vision to improve its detection accuracy and real-time performance. Additionally, we aim to explore opportunities for expanding its capabilities, such as integrating with existing surveillance systems and enhancing its scalability for deployment in various environments.
## Advantage of Guardian Vision

## Challenges in Real-world

1.Finding Database for ML model
2.Deployment of ML model on website.
3.Sending alert by sms and Emails.

## Solution

1.Creating/Finding and framming of database.
2.Deployment of ML model using Flask libaray.
3.Sending alert through Python libaray .

## Support

For support, email aviralofficial1729@gmail.com

## Team Members 🧑‍🤝‍🧑

- [@maskboyAvi](https://github.com/maskboyAvi)
- [@aks](https://github.com/atharvsawant2003)
- [@ayush_lion](https://github.com/Ayushlion8)
- [@umeshSinghVerma](https://github.com/umeshSinghVerma)

<p align='center'><img src="static\images\WhatsApp Image 2023-04-24 at 01.07.02.jpg" alt="Weapon Detection" width="800"></p>

## Team Members

You can reach out to us at aviralofficial1729@gmail.com where you can give feedbacks or report bugs.
