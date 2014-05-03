# #!/usr/bin/python
# -*- coding:utf-8 -*-

import sys,commands

class yandexDisk:
	propertiesDict = {}
	STATUS_ERROR = 2
	STATUS_RUNNING = 1
	STATUS_STOPPED = 0
	status = ''

	def __init__(self):
		self.updateInfo()

	def updateInfo(self):
		self.propertiesDict = {}
		yandexDaemonStatus = unicode(commands.getoutput("yandex-disk status"), "utf-8")

		if(yandexDaemonStatus.find(u"Ошибка") != -1):
			self.status = self.STATUS_ERROR
			return

		if(yandexDaemonStatus.find(u"демон не запущен") == -1):
			self.status = self.STATUS_RUNNING
		else:
			self.status = self.STATUS_STOPPED
			return

		properties = yandexDaemonStatus.split("\n")
		i = 0
		for p in properties:
			i = i + 1
			pair = p.split(":")
			if(len(pair) > 1):
				key = p.split(":")[0].strip()
				value = p.split(":")[1].strip()
				if(value == ''):
					value = properties[i:]
					self.propertiesDict[key] = value
					break
				self.propertiesDict[key] = value

	def start(self):
		return commands.getoutput("yandex-disk start")
	
	def stop(self):
		return commands.getoutput("yandex-disk stop")
	
	def getProperty(self, propertyName):
		if propertyName in self.propertiesDict:
			return self.propertiesDict[propertyName]
		else:
			return False

	def getError(self):
		if(self.status == 0):
			return u"Демон не запущен"
		else:
			return False

	def getStatus(self):
		return self.getProperty(u"Статус ядра синхронизации")

	def getProgress(self):
		return self.getProperty(u"Статус синхронизации")

	def getSize(self):
		return self.getProperty(u"Всего")

	def getFree(self):
		return self.getProperty(u"Свободно")

	def getLastsynchronized(self):
		return self.getProperty(u"Последние синхронизированные пути")

	def getBasket(self):
		return self.getProperty(u"Размер корзины")

	def getUsed(self):
		return self.getProperty(u"Занято")

	def getPath(self):
		return self.getProperty(u"Путь к папке Яндекс.Диска")