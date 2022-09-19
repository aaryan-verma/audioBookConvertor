import pyttsx3
import PyPDF2
book=open(input('Enter filename : '),'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print('no of pages : ',pages)
speaker= pyttsx3.init()
frmt=input('Enter the audio file format/extension : ')
OpFileName='test.'+frmt

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[int(input('Press 0 or 1 for male or female voice respectively : '))].id) #changing index changes voices but ony 0 and 1 are working here

newVolume=float(input('Enter the volume level in the range of 0.0 to 1.0 inclusive. (Defaults to 1.0.) : '))
volume = speaker.getProperty('volume')
speaker.setProperty('volume', newVolume)

speaker.setProperty('rate',int(input('Enter the speed (Defaults to 200 WPM) : ')))
for num in range(3, pages):
	page= pdfReader.getPage(num)
	text= page.extractText()
	speaker.save_to_file(text,OpFileName)
	print('Audio file generated & stored in .'+frmt,' format')
	speaker.say(text)
	speaker.runAndWait()