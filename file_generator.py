import os, sys
from sys import argv
try:
	script, tvshow_avi, tvshow_srt, n = argv
	def gen(tvshow_var, n):
		tvshow = tvshow_var
		tvn = int(n)+1
		#tvshow = "TVShow.EpisodeName.Credit.DVDRIP.S01E01.srt"
		#tvshow = "TVShow.EpisodeName.S01E01.avi"
		tvshow_split = tvshow.split('.')
		tvshow_list = []
		for x in range(1,tvn):
			data = 'S01E%d' %(x)
			tvshow_list.append(tvshow.replace(tvshow_split[-2], data ))
			single_file = tvshow.replace(tvshow_split[-2], data )
			file = open(tvshow.replace(tvshow_split[-2], data ) , 'w')
			file.write(tvshow.replace(tvshow_split[-2], data ))
			file.close()


	gen(tvshow_avi, n)
	gen(tvshow_srt, n)


except:
	print ""	
	print "		File Generator"
	print "		It creates several files basead on the two filenames and the number of files"
	print "		file_generator.py filename1 filenamediff1 number_of_files"
	print "		Ex:"
	print "		file_generator.py TVShow.EpisodeName.S01E01.avi TVShow.EpisodeName.Credit.DVDRIP.S01E01.srt 10"
	print ""




