import random
import webbrowser

adict = {
	"00_fb_L_ac" : "watch?v=zgNRJsGzDh4",
	"01_fb_L_a"  : "watch?v=Z-A1zl8Laes",
	"02_fb_L_l"  : "watch?v=oJs7hzlHWco",
	"03_fb_L_uc" : "watch?v=n-gj7ZOHrU0",
	"04_fb_L_u"  : "watch?v=wCbI4zEbW5M",
	"05_fb_L_u"  : "watch?v=31GQrtI6ivI",
	"06_fb_L_uc" : "watch?v=F4f8Ny82h88",
	"07_fb_L_ac" : "watch?v=EkWBqgXUXDY",
	"08_fb_L_ac" : "watch?v=IFB_au89KWE",
	"09_fb_L_l"  : "watch?v=LyeuYIGTPJk",
	"10_fb_L_ac" : "watch?v=M2pfvVdk6N0",
	"11_fb_L_u"  : "watch?v=31GQrtI6ivI",
	"12_fb_L_l"  : "watch?v=UgcwcPmhmb0",
	"13_fb_L_a"  : "watch?v=Q89MwOlSuhg",
	"14_fb_L_tc" : "watch?v=7f9XpgN9f6k",
	"15_fb_L_ac" : "watch?v=ohGC3AXIlRw",
	"16_fb_L_ac" : "watch?v=pNZe01hqMW8",
	"17_fb_L_t"  : "watch?v=EJK4RuUz0yI",
	"18_fb_L_tc" : "watch?v=uNrqrk2xcAo",
	"19_fb_L_t"  : "watch?v=tTl6MgjL2E8",
	"20_fb_L_t"  : "watch?v=QiuJ3ZFAiBg",
	"21_fb_L_tc" : "watch?v=wmF2m6cEgEw",
	"22_fb_L_t"  : "watch?v=siIicrZ4gng",
	"23_fb_L_tc" : "watch?v=juh98840e5I",
	"24_fb_L_uc" : "watch?v=TSDS8KixaQ0",
	"25_fb_L_uc" : "watch?v=j7HnFtNmDl4",
	"26_fb_L_l"  : "watch?v=tTl6MgjL2E8",
	"27_fb_L_l"  : "watch?v=UgcwcPmhmb0",
	"28_fb_L_l"  : "watch?v=vYV6wt7U4nI",
	"29_fb_L_x"    : "watch?v=PBHBhvv-Lhg",
	"30_fb_L_x"    : "watch?v=jLi5CcyTFgQ",
	"31_fb_L_l"  : "watch?v=-_yK_PDR8mc",
	"32_fb_L_l"  : "watch?v=11JXbBBgfWg",
	"33_fb_L_lc" : "watch?v=EWoxVdAd-HI",
	"34_fb_L_l"  : "watch?v=LTJesxB1aZY",
	"01_fb_S_tc" : "watch?v=rzoqO3ENKNk",
	"02_fb_S_a"  : "watch?v=nBFdBnIbZRo",
	"03_fb_S_ac" : "watch?v=sCw3xdmoxHQ",
	"04_fb_S_l"  : "watch?v=zpbmLb4CLFU",
	"05_fb_S_l"  : "watch?v=VLm89huAEYA",
	"06_fb_S_u"  : "watch?v=xRt4LSANIoU",
	"07_fb_S_a"  : "watch?v=0CQ7riVMNJc",
	"08_fb_S_l"  : "watch?v=C8X96ItgyOg",
	"09_fb_S_w"    : "watch?v=R0mMyV5OtcM",
	"10_fb_S_w"    : "watch?v=Ie4ZTuMh_K0",
	"11_fb_S_w"    : "watch?v=ERdZqyorGfk",
	"12_fb_S_w"    : "watch?v=hsGgI0ThLG8"
}
			 
dictkey = "w: warm up, a: abs, u: upper, l: lower, t:total, c: cardio"

def preface():
	print 'Hello,'
	print 'What kind of workout for the day?'
	print dictkey
	while 1:
		type = raw_input('>')
		if all([x in 'waultc' for x in type]):
			break
	
	print 'anything you don\'t want to do?'
	print dictkey
	while 1:
		ew = raw_input('>')
		if ew[0].lower() == 'n':
			ew = 'n'
			break
		elif all([x in 'waultc' for x in ew]):
			break
	
	
	print 'Long or Short workout?' 
	print '(Warm up videos are short)'
	
	while 1:
		length = raw_input('>')
		length = length[0].upper()
		if length == 'L' or length == 'S':
			break
		print 'Make up your mind!'

	return length, type, ew


def selectvideo((alength, atype, anew)):
	if anew == 'n':
		video = [adict.get(x) for x in adict if alength in x and all([y in x for y in atype])]
	else:
		video = [adict.get(x) for x in adict if alength in x and all([y in x for y in atype]) and not any([y in x for y in anew])]
	
	if len(video) == 0:
		selectvideo(preface())
	else:
		webbrowser.open('https://www.youtube.com/' + random.choice(video))
		print 'Enjoy!'

	

selectvideo(preface())
