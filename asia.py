import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import random
from PIL import ImageTk
from PIL import Image, ImageTk


#  news dataset
categories = ['Sports', 'Politics', 'Tech', 'Entertainment']
data = {'news': [], 'category': []}

for _ in range(100):
    category = random.choice(categories)
    if category == 'Sports':
        news = 'Sports news: ' + ' '.join(random.sample(['team', 'scored', 'match', 'victory','Athlete','Team','Player','Coach','Referee','Umpire','Captain','Squad','Roster','Draft','archer','athlete','athletics',
                                                         'baseball','basketball','bat','badminton','Cricket','t20','odi','test','bicycle','biking','boxer','champion','coach','exercise','fitness','football','innings',
                                                         'World cup','game','javelin','virat kholi','karate','kung fu','jordan','tyson fury','long jump','medal','usain bolt','olympic','Barcelona','intermiami fc' ,'messi' ,'ronaldo',
                                                         'al nasar','csk','MS Dhoni','AFC Champions League','League match','Liverpool star','won','Tournament','Championship','League','Cup','Playoffs','Fixture','Match','Game','Series','Exhibition'
                                                         ,'Stadium','Arena','Field','Court','Track','Pitch','Grandstand','Bleachers','Locker Room','Clubhouse','Jersey','Uniform','Helmet','Cleats','Racket','Ball','Bat','Gloves','Goalposts','Net',
                                                         'Training','Conditioning','Workout','Exercise','Drills','Fitness','Warm-up','Cool-down','Gym','Personal Trainer','Federation','Association','Committee','Governing Body','IOC (International Olympic Committee)',
                                                         'FIFA (Fédération Internationale de Football Association)','NFL (National Football League)','NBA (National Basketball Association)','MLB (Major League Baseball)','NHL (National Hockey League)','ICC(The International Criminal Court)',
                                                         'IPL(Indian Premier League)','Glenn Maxwell’s '], 3))
    elif category == 'Politics':
        news = 'Politics update: ' + ' '.join(random.sample(['election', 'government', 'policy', 'vote','Government Institutions','Parliament','Congress','Senate','House of Representatives','Executive Branch','Legislative Branch','Judicial Branch','Cabinet','Political Leaders','President','Prime Minister','Chancellor','Governor',
                                                             'Mayor','Dictator','Monarch','Leader','Head of State','Head of Government','Political Parties','Democrat','Republican','Liberal','Conservative','Socialist','Green Party','Nationalist','Independent','Third Party','Coalition','Elections','Election','Campaign'
                                                             ,'Candidate','Voter','Ballot','Polling','Primary','General Election','Electoral College','Swing State','accusation','anonymity','assail','authorotarian','career','claim','voting' ,'vote','engagement','greedy','influence','governor','Gov','President’s','Ranil Wickremesinghe'
                                                             ,'Governance','Public Administration','Bureaucracy','Public Service','Civil Service','Regulatory Body','Government Agency','Public Sector','Private Sector','Public Policy Analysis','violence','President'], 3))
    elif category == 'Tech':
        news = 'Tech news: ' + ' '.join(random.sample(['Ai','zoom','iphone','elon musk','twitter','laptop','keyboard','mouse','samsung','project','OnePlus','smart phone','laptop', 'computer,switch between mute','vibrate','switch','ringer sound','profiles','phone',
                                                       'handset','install','predecessor','Apple iPhone Series','Google Pixel Series','OnePlus','Xiaomi','Huawei','Sony Xperia Series','LG','Motorola','Realme','Oppo','vivo','redmi',
                                                       'Hardware','Processor','Memory (RAM)','Storage','Motherboard','Graphics Card','Central Processing Unit (CPU)','Peripheral','Input/Output (I/O)','Circuit Board','Chipset,Software','Application','Operating Syste(OS)','Code','Programming',
                                                       'Algorithm','Debugging','Software Development Kit (SDK)','User Interface (UI)','User Experience (UX)','Patch','Internet and Networking','Internet','Browser','Search Engine','Website','Server','Hosting','Router','Modem','Firewall','Bandwidth','Programming and Development',
                                                       'Coding','Programming Language','Developer','IDE (Integrated Development Environment)','Version Control','Agile','API (Application Programming Interface)','Framework','Repository','Artificial Intelligence (AI) and Machine Learning (ML)','WhatsApp','wireless charging technology',
                                                       'Android phones','5G','Edge Computing','Quantum Computing','Internet of Things (IoT)','Augmented Reality (AR)','Virtual Reality (VR)','Big Data','Automation','Digital Transformation','Robotics','Smartphone','Tablet','Wearable','Mobile App','Operating System (Mobile)','Augmented Reality (AR)',
                                                       'Virtual Reality (VR)','IoT (Internet of Things)','Smart Home','Smart Device','Artificial Intelligence','Machine Learning','Neural Network','Algorithm','Data Science','Deep Learning','Natural Language Processing (NLP)','Computer Vision','Predictive Analytics','AI Ethics'
                                                       ,'meta','face book','instagram','social media platform','study','Android 12-based','OxygenOS 14 update'], 3))
    else:
        news = 'Entertainment news: ' + ' '.join(random.sample(['Movies','Theatre','Circus,film,pic','3-D','Scence,episode','Music','the','has','in','Script','Director','Actor','Actress','Producer','Cinematography','Screenplay','Premiere','Box Office','Casting'
                                                                ,'Album','Song','Artist','Band','Concert','Tour','Recording','Producer','Lyrics','DJ','Video Game','Console','PC','Gaming','eSports','Virtual Reality (VR)','Game Developer','Gaming Community','Multiplayer',
                                                                'DLC (Downloadable Content)','Gameplay' ,'Author','Novel','Fiction','Non-fiction','Bestseller','Book Signing','Publisher','Editor','Literary Agent','Plot','Theater','Play','Stage','Actor','Director','Costume Design'
                                                                ,'Set Design','Intermission','Broadway','Rehearsal','Curtain Call' ,'Celebrity and Events','Red Carpet','Paparazzi','Awards Show','Premiere','Afterparty','Fanbase','Autograph','Fan Convention','Fame','Streaming and Digital Media',
                                                                'Streaming Service','Subscription','Content Creator','Vlog','Podcast','Web Series','Digital Distribution','Online Platform','Viral','Trending' ,'Art and Design','Visual Arts','Graphic Design','Art Gallery','Exhibition','Illustrator',
                                                                'Animation','Art Director','Set Design','Costume Design','Concept Art','Fashion','Fashion Show','Designer','Runway','Trend','Couture','Fashion Week','Model','Stylist','Wardrobe','Accessories' ,'Radio','Radio Show','RJ','Podcast','Broadcast',
                                                                'Frequency','Radio Station','Jingle','Host','Talk Show','Airtime','ticket','box office','release'], 3))
    data['news'].append(news)
    data['category'].append(category)

# Create a DataFrame
df = pd.DataFrame(data)

# Text preprocessing and vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['news'])
y = df['category']

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X, y)


# Create a Tkinter interface
def classify_news():
    input_text = input_text_widget.get("1.0", tk.END)
    input_text = input_text.strip()

    if input_text:
        # Preprocess the input text
        input_vector = vectorizer.transform([input_text])

        # Predict the category
        prediction = classifier.predict(input_vector)[0]

        result_label.config(text=f"Predicted Category: {prediction}")
    else:
        result_label.config(text="Please enter some news text.")


# Create the main window
root = tk.Tk()
root.geometry('1540x1080+0+0')
root.resizable(False,False)
root.title("News Classification System")

#img = ImageTk.PhotoImage(Image.open('bgimage.jpg').resize(100,200))
#l = tk.Label(root, image=img)
#l.place(x=0,y=0,width=100,height=300)

backgroudImage = ImageTk.PhotoImage(file=r"C:\Users\Mathushan\OneDrive\Desktop\News project\bg.jpg")


bgLabel = tk.Label(root,image=backgroudImage)
bgLabel.place(x=0,y=70,width=1720,height=780)

#backgroudImage1 = ImageTk.PhotoImage(file='bgimage1.jpg')
#bgLabel1 = tk.Label(root,image=backgroudImage1)
#bgLabel1.place(x=740,y=70,width=780,height=750)

bgLabel2 = tk.Label(root,text='News Classification System',font=('Times New Roman',35 ,'bold'),fg='#2E708E')
bgLabel2.place(x=540,y=5)

# Input text area
input_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=125, height=20)
input_text_widget.place(x=260,y=300)

# Classify button
classify_button = tk.Button(root, text="Classify", command=classify_news,width=30 ,height=2,border=0,bg='#2E708E',fg='white',font=('Simsun',15 ,'bold'),activebackground='#F3F7D7',activeforeground='#F85511')
classify_button.place(x=620,y=680)

# Result label
result_label = tk.Label(root, text="", font=("Simsun", 25))
result_label.place(x=500,y=200)

# Run the main loop
root.mainloop()
