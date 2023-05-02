Project Description:
Introduction: 
The use of computers and technology is increasing rapidly, and people are spending more and more time in front of their screens. This can lead to physical and mental health issues, which a friendly companion bot can help alleviate by reminding people to take breaks, exercise, provide entertainment and engage in other activities. Additionally, the market demand for desktop companion bots is growing, as people are recognizing the value of having a helpful and interactive tool to assist them while they work. The success of companies like Anki is evidence of this trend. Overall, a desktop companion bot is a feasible and timely project that offers a unique opportunity to learn and apply a variety of skills and technologies while exploring the potential of AI technology. Thus, we have come up with our desktop companion bot “Baymin-1.0”

Working Procedure in Brief:
As soon as the system (Pi OS) is turned on, a few programs are running, one of which takes a picture every second. Another program checks the pictures after a while to see if there are any humans in them. If there is a human, it updates a record in a file. The other programs check this file, make various decisions based on it, and if there is any output to be given, they send signal to the servo motor through GPIO pins for a specific output and simultaneously provide audio output through the speaker. The scheduled alerts are given by triggering the OS time with crontab.

Features:
The desktop companion bot-
    1. Welcomes the user with a friendly greeting usually on each reboot and after specific period of the user’s absence
    2. Notifies the user to take a break from work after a particular amount of time (typically 15-20 minutes) and ensures that the break lasts at least 5 minutes. It is a Pomodoro Technique implementation. However, if the user is attending a meeting, the alarm can be manually postponed.
    3. Reminds the user every hour to drink water.
    4. Celebrates by dancing (along with a song) after detecting a "V" symbol displayed by the user every time he achieves something. As the target group of users is specially coders, developers, freelancers etc.
    5. Notifies the user when it is time (set by the user himself) to go to bed.
Used Components: 
For hardware set up we have used the following materials. The list is included with component model along with quantity:
    1. Raspberry Pi 4 Model B × 1
    2. CPU Cooling Fan (30×30×7mm) × 1
    3. Mini Servo SG90 × 4
    4. External Stereo Speaker × 1
    5. Web Cam 1080p × 1
    6. Jumper Wire Male to Male × 8
    7. Jumper Wire Male to Female × 5
    8. Power Supply 5V-2A (5.5mm Jack) × 2
    9. Power Supply 5V-3A (USB Type-C) × 1
    10. DC Barrel Jack (5.5mm) × 2
    11. Craft Boards
    12. Popsicle Sticks × 2
For software set up we have used the following technologies:
    • Operating System: Raspberry Pi OS Legacy (Buster)
    • Language Used: Python
    • Library and Tools: OpenCV, Tensorflow Lite, Mediapipe, Crontab, Pigpio, Thonny Python IDE
