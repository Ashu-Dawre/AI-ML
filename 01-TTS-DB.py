import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import mysql.connector as mycon

speech_config = SpeechConfig(subscription="48eb9d0da9834f95v33b6e471bb44deb", region="eastus")
speech_config.speech_synthesis_voice_name="en-US-AriaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-MiaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-RyanNeural"
#speech_config.speech_synthesis_voice_name="en-US-JennyNeural"
#speech_config.speech_synthesis_voice_name="en-US-GuyNeural"
#speech_config.speech_synthesis_voice_name="en-IN-NeerjaNeural"
#speech_config.speech_synthesis_voice_name="en-IN-PrabhatNeural"
#speech_config.speech_synthesis_voice_name="en-CA-ClaraNeural"
#speech_config.speech_synthesis_voice_name="en-CA-LiamNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

no=int(input('Enter account number : '))

con=mycon.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()
curs.execute("select accnm,balance from accounts where accno=%d" %no)
rec=curs.fetchone()
try:
    text='Account Name is '+rec[0]+' and balance is '+str(rec[1])
    print(text)
except:
    text='account does not exist'

con.close()

result = speech_synthesizer.speak_text_async(text).get()


