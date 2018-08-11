import pandas as pd

import time

import math

from pox.core import core

from scipy.stats import chisquare

log = core.getLogger()

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

class chisStat(object):
	
	x,y = 0, 999999
	count = 0
	
	expTimeSec = 10 + time.time()
	expTimeDay = 40 + time.time()
        expBaseTime = 40 * 7 + time.time()
        
	ix = ['pst7','pst6','pst5','pst4','pst3','pst2','pst1','count10s','countday','last_access','countweek']
	chiTable = pd.DataFrame(index = ix)
	sortedTable = pd.DataFrame()
	
	def stats(self,element):
		self.count += 1
		
		if element not in list(self.chiTable.columns):
			self.chiTable[element] = [0,0,0,0,0,0,0,0,0,time.time(),0]
				
		self.chiTable.loc['count10s', element] += 1
		self.chiTable.loc['countday', element] += 1
		self.chiTable.loc['last_access', element] = time.time()				
		
		self.sortData()
		#print self.sortedTable.T

		if time.time() > self.expTimeSec:
			#updating table values every 10s
			#calculate chi-square first then reset the values
			if self.expBaseTime > time.time():
				pass
			else:
				self.calcChi()
			self.chiTable.loc['count10s'] = 0
			self.expTimeSec = time.time() + 10
		
		#self.sortData()
		#print self.sortedTable.T

	def sortData(self):
		df = pd.DataFrame([[int(math.log(i,2)) for i in range(1,len(list(self.chiTable.columns))+1)]], columns = list(self.chiTable.T.sort_values(by='countday', ascending = False).T.columns))
		t = df.append(self.chiTable, ignore_index = False)
		self.sortedTable = t.T.sort_values(by=0).T	

	def baseLine(self):	
	        if time.time() > self.expTimeDay :
			self.chiTable.T['pst7'] = self.chiTable.T['pst6']
			self.chiTable.T['pst6'] = self.chiTable.T['pst5']
			self.chiTable.T['pst5'] = self.chiTable.T['pst4']
			self.chiTable.T['pst4'] = self.chiTable.T['pst3']	
			self.chiTable.T['pst3'] = self.chiTable.T['pst2']
			self.chiTable.T['pst2'] = self.chiTable.T['pst1']
			self.chiTable.T['pst1'] = self.chiTable.T['countday']
			self.chiTable.T['countday'][:] = 0
			self.chiTable.T['countweek'] = self.chiTable.T['pst7'] + self.chiTable.T['pst6'] + self.chiTable.T['pst5'] + self.chiTable.T['pst4'] + self.chiTable.T['pst3'] + self.chiTable.T['pst2'] + self.chiTable.T['pst1']
			
			self.sortData()
			self.expTimeDay = time.time() + 40		

        #call this function just at the end of every 10s of data collection 
	def calcChi(self): 

		list1 = []
		list2 = []

		s = list(self.sortedTable.T[0])
		m = set(s)
		i = 0
		for x in m:
			#if len(self.sortedTable.T.groupby([0]).get_group(x)['count10s'])%2 -1:
			list1.append(self.sortedTable.T.groupby([0]).get_group(x)['count10s'].sum()/self.sortedTable.loc['count10s'].sum())
			list2.append((self.sortedTable.T.groupby([0]).get_group(x)['countweek'].sum() / (7*4.0))/(self.sortedTable.loc['countweek'].sum() / (7*float(4))))
			i += 1
		self.x, self.y = chisquare(list1,list2)
		#print "Chi-Square value is :", x,", p:", y, ".\n"
		log.info("Chi-Square Value = ")
		log.info(self.x)
		log.info(self.y)
	def __init__(self):
		pass	