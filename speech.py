import gtts
import playsound
text = input("enter something here:")
sound = gtts.gTTS(text, lang="en")
sound.save("ank.mp3")
playsound.playsound("ank.mp3")


