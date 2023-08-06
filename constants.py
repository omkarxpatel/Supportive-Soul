#- []( \"Hovertext\")

RESOURCES = """
- Crisis Text Line: Text 'HOME' to `741741`
- Suicide Prevention Hotline: `1-800-273-TALK` (1-800-273-8255)
- SAMHSA National Helpline: `1-800-662-HELP` (1-800-662-4357)
- National Alliance on Mental Illness (NAMI)
- Mental Health America (MHA)
- Anxiety and Depression Association of America (ADAA)
- National Institute of Mental Health (NIMH)
- American Foundation for Suicide Prevention (AFSP)
- Crisis Connections: `866-427-4747` (Washington State)
- RAINN (Rape, Abuse & Incest National Network) National Sexual Assault Hotline: `1-800-656-HOPE` (1-800-656-4673)
- Trevor Project Lifeline (LGBTQ+ Youth): `1-866-488-7386`
- Trans Lifeline: `1-877-565-8860`
- Veterans Crisis Line: `1-800-273-8255` (Press 1)

**More**
- [Crisis Text Line](https://www.crisistextline.org/text-us/ \"Hovertext\")
- [Other Hotlines/Text Lines](https://teenlineonline.org/youth-yellow-pages/cutting-and-self-injury/ \"Hovertext\")
"""





ADHD_BASE = """
Attention deficit hyperactivity disorder (ADHD) is a mental health disorder that can cause above-normal levels of hyperactive and impulsive behaviors. People with ADHD may also have trouble focusing their attention on a single task or sitting still for long periods of time. Both adults and children can have ADHD.

ADHD often begins in childhood and can persist into adulthood. It may contribute to low self-esteem, troubled relationships, and difficulty at school or work.

**Status**
- Very Common: Over 3 million US cases reported per year.
- Treatments: Treatment can help, but ADHD cannot be cured.
- Notes: Medical diagnosis required.
"""

ADHD_RESOURCES = """
- [ADHD Facts and more](https://www.aacap.org/AACAP/Families_and_Youth/Resource_Centers/ADHD_Resource_Center/Home.aspx \"Hovertext\")
- [Types of ADHD](https://www.additudemag.com/slideshows/add-vs-adhd/#:~:text=ADHD%20is%20the%20official%2C%20medical,lack%20of%20focus%2C%20and%20forgetfulness. \"Hovertext\")
- [CHADD Organization](https://chadd.org/ \"Hovertext\")
- [CDC Article](https://www.cdc.gov/ncbddd/adhd/facts.html \"Hovertext\")
"""

ADHD_COPING = """
- [Living with ADHD](https://www.verywellmind.com/living-well-with-adhd-20480 \"Hovertext\")
- [80 Coping Strategies](https://www.additudemag.com/dealing-with-adhd-80-coping-strategies/ \"Hovertext\")
- [For Parents](https://kidshealth.org/en/parents/adhd.html \"Hovertext\")
"""





DEPRESSION_BASE = """
Clinical Depression
What is Clinical Depression?
Clinical Depression is a mental health disorder characterized by persistently depressed mood or loss of interest in activities, causing significant impairment in daily life.

The persistent feeling of sadness or loss of interest that characterizes major depression can lead to a range of behavioral and physical symptoms. These may include changes in sleep, appetite, energy level, concentration, daily behavior, or self-esteem. Depression can also be associated with thoughts of suicide.

Status
Very Common- Over 3 million US cases reported per year.
Treatments- Can be treated by a medical professional. This condition is medium-term, and usually resolves within months.
Notes: Medical diagnosis is required.
"""

DEPRESSION_RESOURCES = """
Resources
- [NIMH Resources](https://www.nimh.nih.gov/health/topics/depression/index.shtml \"Hovertext\")
- [Twelve tips for dealing with depressive episodes](https://www.medicalnewstoday.com/articles/322495#twelve-tips \"Hovertext\")
- [Depression Fact Sheed](https://www.hopefordepression.org/depression-facts/ \"Hovertext\")
"""

DEPRESSION_COPING = """
Coping with Depression
- [Coping Skills](https://www.helpguide.org/articles/depression/coping-with-depression.htm \"Hovertext\")
- [8 Tips for Living With Depression](https://www.verywellmind.com/tips-for-living-with-depression-1066834 \"Hovertext\")

Hotlines
- National Suicide Prevention Hotline: 800-273-8255
- The Samaritans Hotline: 212-673-3000
"""




SELF_HARM_BASE = """
Nonsuicidal self-injury, often simply called self-harm, is the act of deliberately harming your own body, such as cutting or burning yourself. It's typically not meant as a suicide attempt. Rather, this type of self-injury is a harmful way to cope with emotional pain, intense anger and frustration.

**Resisting The Urge**
Call a friend and talk about something completely different
-Take a shower (make sure you don't have razors in the shower)
Go for a walk or run, take a bike ride, dance like crazy, or get some other form of exercise
Play with a pet
Watch TV (change the channel if the show gets upsetting or features cutting)
"""

SELF_HARM_RESOURCES = """
- [The Butterfly Project](https://www.adolescentselfinjuryfoundation.com/the-butterfly-project \"Hovertext\")
- [How can I get Support for Self Harm](https://nami.zendesk.com/hc/en-us/articles/360024565894-How-can-I-get-help-support-for-self-harm- \"Hovertext\")
- [What is Self Harm](https://www.cardinalinnovations.org/Resources/Live-your-best-life/Mental-Health/Self-harm \"Hovertext\")
- [Tips on how to Stop](https://www.helpguide.org/articles/anxiety/cutting-and-self-harm.htm \"Hovertext\")

**Talking About It**
- [Crisis Text Line](https://www.crisistextline.org/text-us/ \"Hovertext\")
- [Other Hotlines/Text Lines](https://teenlineonline.org/youth-yellow-pages/cutting-and-self-injury/ \"Hovertext\")
"""





# for suicide intent api
HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded', 
    'X-RapidAPI-Key': '',
    'X-RapidAPI-Host': 'suicidal-ideation-detection.p.rapidapi.com',
}
INTENT_API_URL = 'https://suicidal-ideation-detection.p.rapidapi.com/api/v1/predictions'

# Also reply to the message in the correct language (the language the message is in). 
DETECTION_PROMPT = "I am going to attach the message of a discord user along with their username followed by a colon and then the message content. This message was flagged for self-harm and self-harm/intent. Craft a response that will encourage this user but keep it short and simple. Here is the message:\n\n"
# CHATBOT_PROMPT = "In the following lines, im going to attatch a list of 10 messages, 5 sent by you and 5 sent by the person you are talking to. The messages in the list with the prefix of 'YOU:' are the ones sent by you. Craft response towards this user based off of their previous messages and your responses. Note, this user may be suicidal or have intent of self harm. Reply with a message to encourage this user to keep pushing but keep it short and simple.:\n\n"
CHATBOT_PROMPT = "I am going to attach the message of a discord user along with their username followed by a colon and then the message content. Note that this user may be suicidal or have intent of self harm. Craft a response that will encourage this user but keep it short and simple.\n\n"
