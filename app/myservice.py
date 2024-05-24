from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule 

import time

# define 'global' variables here, everything that will be used across the program
ip = "192.168.0.174"
port = 9559
vocabulary = ['tak', 'nie', 'prosze', 'dziekuje', 'witam', 'przepraszam']
human_interactor = None # will be used for storing human interactive module instance
speech_rec = None
memory = None

tts = ALProxy("ALTextToSpeech", ip, port)
tts.say("Hej, jestem nao!")

class HumanInteractiveModule(ALModule):
    """Module to provide all kind of interaction to humans by NAO
    methods provided underneath will be invoked when when one or more
    of initialised below variables (proxies to modules) will respond to subscribed events
    """
    def __init__(self, name):
        ALModule.__init__(self, name)

    global memory
    memory = ALProxy("ALMemory")

#TODO: create broker for interactions with memory and speech recognitions module

asr = ALProxy("ALSpeechRecognition", ip, port)

asr.setLanguage("Polish")
current_lang = asr.getLanguage()
available_langs = asr.getAvailableLanguages()
print(available_langs)
asr.pause(True)
asr.setVocabulary(vocabulary, False)
asr.subscribe("Test_ASR")
time.sleep(10)
asr.unsubscribe("Test_ASR")

