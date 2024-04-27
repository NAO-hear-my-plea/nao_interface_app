from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.0.3", 9559)
tts.say("Jestem nao!")
