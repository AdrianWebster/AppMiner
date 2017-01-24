class Applicant:
	'''
	this contains all the data for each user
	'''
	def __init__(self, name='', ip='', appdate='',status='', game='', firstreg='', why='', age='', live='', software='', rules='', events='', findout='', fother='', steam='', nco='', acceptdate=''):
			
			self.myName = name
			self.myIp = ip
			self.myAppdate = appdate
			self.status = status
			self.game = game
			self.first = firstreg
			self.joinReason = why
			self.age = age
			self.region = live
			self.software = software
			self.TOS = rules
			self.events = events
			self.who = [findout , fother]
			self.steamURL = steam
			self.NCO = [nco , acceptdate]
