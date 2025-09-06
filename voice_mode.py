import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import tempfile, os

# Listen in Hindi
def listen_hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 कृपया हिंदी में अपना प्रश्न पूछें...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="hi-IN")
        print("✅ आपने कहा:", text)
        return text
    except:
        print("❌ माफ़ करें, समझ नहीं पाया।")
        return ""

# Speak in Hindi
def speak_hindi(text):
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tmp.close()
    gTTS(text=text, lang="hi").save(tmp.name)
    playsound(tmp.name)
    os.remove(tmp.name)

# Advisory answers
def advisory_answer(question: str) -> str:
    q = question.lower()
    
    # Greetings
    if "नमस्ते" in q or "हैलो" in q:
        return "नमस्ते! आपका स्वागत है। आप कैसे हैं?"
    
    # Crop advisory questions with full-line examples
    elif "मक्का" in q and ("कब बोना चाहिए" in q or "समय" in q):
        return "मक्का बोने का सबसे अच्छा समय अप्रैल से जून है।"
    elif "गेहूं" in q and ("कब बोना चाहिए" in q or "समय" in q):
        return "गेहूं बोने का सबसे अच्छा समय नवंबर है।"
    elif "चावल" in q and ("कब बोना चाहिए" in q or "समय" in q):
        return "चावल के लिए जुलाई का महीना सबसे अच्छा है।"
    elif "खाद" in q and ("कैसे दें" in q or "कितनी मात्रा" in q):
        return "खेती में संतुलित खाद का प्रयोग करें — यूरिया और डीएपी।"
    elif ("पानी" in q or "सिंचाई" in q) and ("कितनी बार" in q or "कैसे करें" in q):
        return "फसलों को हफ्ते में कम से कम 2 बार पानी दें।"
    elif ("कीट" in q or "कीट नियंत्रण" in q) and ("कैसे करें" in q or "रोकथाम" in q):
        return "कीटों से बचाव के लिए जैविक दवाओं का प्रयोग करें।"
    
    # General advice
    elif "सलाह" in q or "सुझाव" in q:
        return "मेरी सलाह है कि मौसम की जानकारी लेकर ही फसल करें और स्वास्थ्य का ध्यान रखें।"
    
    # Gratitude
    elif "धन्यवाद" in q or "शुक्रिया" in q:
        return "आपका स्वागत है! आपका दिन शुभ हो।"
    
    else:
        return "माफ़ करें, मेरे पास इस सवाल का उत्तर नहीं है।"

# Continuous demo run
if __name__ == "__main__":
    opening_statement = "🤖 नमस्ते! मैं आपका कृषि सलाहकार हूँ। आप मुझसे फसल, खाद, पानी या कीट नियंत्रण के बारे में पूछ सकते हैं। बोलकर 'बंद करो' कहकर इसे रोक सकते हैं।"
    
    # Speak the opening statement
    print(opening_statement)
    speak_hindi(opening_statement)
    
    while True:
        question = listen_hindi()
        if question:
            # Stop condition
            if any(word in question.lower() for word in ["बंद करो", "exit", "quit"]):
                goodbye = "ठीक है, बातचीत समाप्त कर रहे हैं। आपका दिन शुभ हो!"
                print("🤖", goodbye)
                speak_hindi(goodbye)
                break
            
            answer = advisory_answer(question)
            print("🤖 उत्तर:", answer)
            speak_hindi(answer)
