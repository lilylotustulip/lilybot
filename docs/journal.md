# 📑 Engineering Journal & Dev Log

In this journal, I’ll be tracking the progress, challenges, troubles, solutions, and key takeaways from building **Lilybot**.

---

## 💡 Phase 1: Research & Hardware Design

### **DAY 1: June 16, 2026 -- The Idea**
* **The Problem:** I use AI a lot to learn and test my skills, but AI consumes a massive amount of energy, requires the internet, and relies on cloud computing where your voice data leaves your device to be processed on remote servers. 

* **The Mission:** solve all these problems by creating a local, offline bot.

* **Progress:** I researched the necessary hardware and programming languages, needed for this project.
Since I already studied C/C++ and Python, I knew I could handle the coding. *(If interested, check out my other repositories to see some projects in each language!)*

* **Milestone:** Finished the initial robot design and created the shopping list.

### **DAY 2: June 17, 2026 -- Shopping & Research**
* **The Hustle:** Spent hours searching local electronics shops until I finally found one that had what I needed. 

* **The Bottleneck:** Got most components, but couldn't start building because I couldn't find the specific Class 10 MicroSD card I wanted.

* **Progress:** I didn't let the setback stop me. I spent the rest of the day studying the Raspberry Pi hardware architecture, to have a better understanding of the hardware i''ll be working with.

---

## 🛠️ Phase 2: Hardware Assembly & Troubleshooting

### **DAY 3: June 18, 2026 -- First Boot**
* **Progress:** got the MicroSD card, Installed the OS, configured the Wi-Fi, and set up the system foundation.

* **Reality Check:** This part sounds incredibly easy on paper, but I ran into several configuration troubles and actually had to wipe everything and restart all over again. 

* **Protip:** if you want to use Raspberry pi zero 2 w like i did, i recommand using a small size OS, i used the "Raspberry PI OS Lite (64-bit)"

### **DAY 4: June 19, 2026 -- The Solder Surprise**
* **Progress:** not much but found out the components had to be soldered.

* **The Surprise:** Today was supposed to be the day I tested the components, but to my surprise, I realized I had to solder header pins onto the components before using them. 

* **Action Plan:** Had to go buy a soldering iron tool.


### **DAY 5: June 20, 2026 -- First Major Failure**
* **The Disaster:** Not gonna lie, this was the worst out of all the days so far. I had zero soldering experience and completely ruined the component on my first attempt. It was my first "actual" failure. because that problem was early in the journey and it seemed more like a stopping wall then a normal problem.

* **The Risk:** I couldn't even test it on my Raspberry Pi to see if it was completely dead because I risked shorting out and damaging the Pi itself.

* **The Solution:** Buying a new one was the only way forward. Since the shop was far away, I had to find someone to deliver it. Finally got the replacement module safely soldered!

### **DAY 6: June 22, 2026 -- The Smoke Test**
* **Progress:** Got all components in hand, soldered cleanly, and ready to use.

* **The Dilemma:** When wiring, I realized the microphone and audio amplifier both needed to share **GPIO 19**. There were many ways to do that , and I assume I chose the absolute worst one: *the manual wire splice*.

* **The plot:** The amplifier worked, but the microphone didn't. while i was thinking that the microphone was the one to refuse to work, **I literally smelt burning plastic!** it came from the amplifier!
I unplugged everything immediately. 
started looking for solutions, eventually found that a breadboard is a safe way out of all the troubles.


### **DAY 7: June 24, 2026 -- Isolation Troubleshooting**
* **Progress:** After the Day 6 problem, I had to take a break because the hardware issues were getting frustrating. Today, I decided to split the tasks: instead of plugging everything in, at once, I isolated the microphone on the breadboard to troubleshoot it alone. (because i didnt have the breadboard yet, and testing one component will not need a breadboard)

* **Breakthrough:** After a few hours of testing... **The microphone successfully worked!**

* **Protip:** this day i was almost sure that organisation was important. so try to organize and plan before taking an action, but dont let the planning take over your time, keep balance.

### **DAY 8: June 25, 2026 -- Complete Assembly**
* **Reflection:** I originally thought I had nothing to write about and wanted to wait until the hardware was 100% finished, then writing this journal. But looking back at all the writing I did today, I realized how much progress happens daily. Next time, I will most likely start writing from Day 1 rather than waiting!

* **Status:** Got the breadboard and fully assembled the entire system. I tested all components together. 

* **Result:** Everything works! congrats, hardware phase is done.

---

## 💻 Phase 3: The Coding Phase

### **DAY 9: June 27, 2026 -- The Microphone Battle**
* **The Strategy:** I usually like coding by just "going with the flow" without a roadmap, but this time I actually planned a sequential process: `speaker.py` ➡️ `brain.py` ➡️ `microphone.py` ➡️ `main.py` (the manager to keep RAM usage low on the Pi Zero).

* **The Reality:** I immediately broke my plan and started working on `microphone.py` instead. 

* **The Struggle:** Spent **4 hours and 48 minutes** of straight screen time coding it. I learned some new Python concepts, but it was incredibly hard. I debugged, erased, and restarted from scratch multiple times. For an "easy" script, it was a hard start.

* **Reset:** I ended the day by erasing all the file's code to start fresh with a plan I will actually follow. so i had an empty file at the end of the day.

### **DAY 10: June 28, 2027 -- Speaker Logic**
* **Success:** Today I finished `speaker.py`! It does exactly what I want it to do.

* **Lesson Learned:** Even for just the speaker, I had to debug several times.
I learned a very good debugging tip today: **Spamming `print()` everywhere.** When you don't know where a bug is, putting print statements everywhere lets you track exactly where the interpreter stops, which shows the exact location of the error.

### **DAY 11: June 29, 2027 -- Microphone Success & Optimization**
* **Success:** `microphone.py` is officially done for now! 

* **Design Choice:** Its done but doesnt have a wake word yet. we will look throught that later. at least we got a functional peice of code.

### **DAY 12: July 1, 2026 -- Giving Lilybot a Brain**
* **Progress:** Successfully compiled and got `llama.cpp` running locally on the Raspberry Pi Zero 2 W!

* **Optimization:** Because of my strict RAM limitations, I chose to use the quantized **Q3_K_S** model format as the brain. 
And did set up a fresh roadmap to clear up my next steps.

### **DAY 13: July 2, 2026 -- Logical Anomalies**
* **The Frustration:** The amount of hours spent debugging today was brutal. But it makes sense—the brain is the most complex part of the robot. 

* **The Bug:** I thought I have finished, but when I tested the brain and asked it what `5 * 5` was, it literally looked at me and said `20`. that wasnt my biggest concern. my biggest concern was that whenever i talked more specifically "asked" my bot it wouldnt answer me twice. 

* **The Diagnosis:** I suspect there is a logical error hidden inside my `listen()` function. When the script calls that function, the execution completely stops without throwing a standard syntax error. This means the code is doing exactly what it's told to do, but not what I actually *wanted* it to do. Time to step back and let my brain's Default Mode Network (DMN) process the problem while I rest.

### **DAY 14: July 3, 2026 -- The Breakthrough & Self-Taught Tips**
* **Success:** The brain code is fully functional! It's currently sitting safely in my debugging file while I make a few final adjustments before moving it into `brain.py`.

* **My C++ Debugging Method:** When working on a complex project full of functions, I keep a separate "holding" file nearby. If I hit a bug, I move all the code to the holding file, then cut and paste it back into the debugging file piece by piece. Once a single piece compiles perfectly, I move it into the permanent main file. If this fails, I turn to AI for assistance.

### **DAY 15, July 4, 2026 -- Main, the manager file**
* **plot:** after having main (the last code file) done, i wanted to test it but of course i wun into problems and alot of bugs again. so it would listen, answer but not speak its answer. i then went back to speaker.py, i thought maybe its because the voice is missing. eventually that was the problem. 
the funny thing is that the hardest in the hardware phase was the microphone, and the hardest to code (out of the 2, mic and speaker), was the speaker.

* **Success:** i eventually heard my bots first words, but it was static i told it what to say to see if its working.

### **DAY 16, July 5, 2026 -- THE FINALE**
* **Success:** not gonna lie i spent hours and hours debugging, it was hard but anyways, i finally got it to work, the bot is done!

* **following:** well i finished the bot after 16 DAYS!! this period of time is realistic, i did not count the rest days only the days i worked. it is a first time project i had no previous experience in hardware, not have i ever build a bot. it make take way less for someone whith better experience, and after all the things i learned from my experience i can say that if i try to do it next time it will most likely take way less time to accomplish.

with all that being said i still have to polish the repository and make the bot's container from clay decorate it and only then will i be officially done with this bot. 

note: i will draw the shape of the lilyBot, a "lily" flower as its name shows, and make it from clay, paint it myself aswell.
i am thinking to add a LED to change colors when the bot is thinking, speaking or listening, but this is just some additional things to do.

the following week will be about this _designing, building the body with clay, editing_ and then the project will be officialy done.
As for the bot it is already done, just gonna add more details to make it feel more complete.

> 💡 **My Tips as a Self-Taught Programmer:**
> I use AI as a personal tutor to teach me complex topics. I ask as many questions as it takes until the concept clicks. I ask it to generate exercises for me—starting with highly specific topic exercises, and moving up to complex, multi-topic challenges. I make sure to practice both *writing* code from scratch and *reading/analyzing* some code.


