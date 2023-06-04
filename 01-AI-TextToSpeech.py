import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

speech_config = SpeechConfig(subscription="25eb8d0ba8934f59a33d8e274bb44bfb", region="westus")
#speech_config.speech_synthesis_voice_name="en-US-AriaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-MiaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-RyanNeural"
#speech_config.speech_synthesis_voice_name="en-US-JennyNeural"
#speech_config.speech_synthesis_voice_name="en-US-GuyNeural"
#speech_config.speech_synthesis_voice_name="en-IN-NeerjaNeural"
#speech_config.speech_synthesis_voice_name="en-IN-PrabhatNeural"
speech_config.speech_synthesis_voice_name="en-CA-ClaraNeural"
#speech_config.speech_synthesis_voice_name="en-CA-LiamNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

print("Type some text that you want to speak...")
text = input("Enter text : ")

result = speech_synthesizer.speak_text_async(text).get()


