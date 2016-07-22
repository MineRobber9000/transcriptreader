import requests
class Transcript:
	def __init__(self,episode_title,wiki_basename,transcriptsuffix):
		self.episode_title = episode_title
		self.text = requests.get("http://{}.wikia.com/{}{}?action=raw".format(wiki_basename,episode_title.replace(" ","_"),transcriptsuffix)).text
		lines = self.text.splitlines()
		filter(lines,None)
		lines.remove(0)
		lines.remove(len(lines)-1)
		self.lines = []
		for line in lines:
			self.lines.append(line.replace("''","").replace("'''","").replace("[[","").replace("]]",""))

	def getLines(self):
		return self.lines

	def getName(self):
		return self.episode_title

class SUTranscript:
	def __init__(self,ep):
		super(type(self),self).__init__(ep,"steven-universe","/Transcript")
