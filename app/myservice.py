from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.0.173", 9559)
tts.say("Hej, jestem nao!")
