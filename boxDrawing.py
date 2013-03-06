#MenuTitle: boxDrawing

from math import sqrt, sin, asin, radians


__doc__ = '''

This script will draw the range of Box Drawing Characters and Block Elements into a font file.
It makes use of the Robofab Python library (http://robofab.org); make sure it is installed and working.
The script was successfully tested in RoboFont, Glyphs and FontLab.
You can even run this script straight from the command line, given that Robofab can be imported.
The box-drawing itself is done using combinations of simple drawing commands; listed in the long dictionary below.

'''

# ----------------------------------------------------------------
# Edit these values if you want:
width       = 600		# Glyph width.
height      = 1400 		# Height for line elements, including overlap.
median      = 300 		# Median line.
thickness   = 30 		# General line thickness.
fat         = 2 		# Multiplication factor for drawing 'fat' lines; will multiply line thickness.
radius      = width/2 	# Radius for arc elements.
blockHeight = 1000 		# Height for block elements.

# Those following values are for block elements, and are dependent of the values above.
blockOrigin = (0,median-blockHeight/2)
blockTop = (width,median+blockHeight/2)


# Nothing below here _needs_ to be edited, but feel free to do so:
# ----------------------------------------------------------------


# Checking which application we are in:

inRF = False
inFL = False
inGlyphs = False
inShell = False

if not any((inRF, inFL, inGlyphs)):
	try:
		import RoboFont
		inRF = True
	except ImportError:
		pass

if not any((inRF, inFL, inGlyphs)):
	try:
		import GlyphsApp
		inGlyphs = True
	except ImportError:
		pass

if not any((inRF, inFL, inGlyphs)):
	try:
		import flsys
		inFL = True
	except ImportError:
		pass

if not any((inRF, inFL, inGlyphs)):
	inShell = True
	import os, time



if not inRF:
	from robofab.world import RFont, CurrentFont



# Check if a font is open, if not create a new one.
# Unless in Glyphs, where I do not know how to do that.

fontExists = False
f = CurrentFont()

if f != None:
	fontExists = True
else:
	if not inGlyphs:
		f = RFont()
		fontExists = True

	if inGlyphs:
		print 'Please open font first.'

if fontExists and inGlyphs:
	Doc = Glyphs.currentDocument
	GlyphsFont = Doc.font 
	FontMaster = GlyphsFont.fontMasters()[0]


names = { 
	# List of glyphs and their drawing recipes.
	
	('lighthorzbxd', '2500'): ['horBar()'],
	('heavyhorzbxd', '2501'): ['horBar(fat)'],
	('lightvertbxd', '2502'): ['vertBar()'],
	('heavyvertbxd', '2503'): ['vertBar(fat)'],
	('lighttrpldashhorzbxd', '2504'): ['dashedHorLine(boxPen, 3, width, thickness)'],
	('heavytrpldashhorzbxd', '2505'): ['dashedHorLine(boxPen, 3, width, thickness*fat)'],
	('lighttrpldashvertbxd', '2506'): ['dashedVertLine(boxPen, 3, blockHeight, thickness)'],
	('heavytrpldashvertbxd', '2507'): ['dashedVertLine(boxPen, 3, blockHeight, thickness*fat)'],
	('lightquaddashhorzbxd', '2508'): ['dashedHorLine(boxPen, 4, width, thickness)'],
	('heavyquaddashhorzbxd', '2509'): ['dashedHorLine(boxPen, 4, width, thickness*fat)'],
	('lightquaddashvertbxd', '250A'): ['dashedVertLine(boxPen, 4, blockHeight, thickness)'],
	('heavyquaddashvertbxd', '250B'): ['dashedVertLine(boxPen, 4, blockHeight, thickness*fat)'],
	('lightdnrightbxd', '250C'): ['horHalfBar("right")', 'vertHalfBar("bottom")'],
	('dnlightrightheavybxd', '250D'): ['horHalfBar("right", fat)', 'vertHalfBar("bottom")'],
	('dnheavyrightlightbxd', '250E'): ['horHalfBar("right")', 'vertHalfBar("bottom", fat, buttT = thickness)'],
	('heavydnrightbxd', '250F'): ['horHalfBar("right", fat)', 'vertHalfBar("bottom", fat, buttT = thickness*fat)'],
	('lightdnleftbxd', '2510'): ['horHalfBar("left")', 'vertHalfBar("bottom")'],
	('dnlightleftheavybxd', '2511'): ['horHalfBar("left", fat)', 'vertHalfBar("bottom")'],
	('dnheavyleftlightbxd', '2512'): ['horHalfBar("left")', 'vertHalfBar("bottom", fat, buttT = thickness)'],
	('heavydnleftbxd', '2513'): ['horHalfBar("left", fat)', 'vertHalfBar("bottom", fat, buttT = thickness*fat)'],
	('lightuprightbxd', '2514'): ['horHalfBar("right")', 'vertHalfBar("top")'],
	('uplightrightheavybxd', '2515'): ['horHalfBar("right", fat)', 'vertHalfBar("top")'],
	('upheavyrightlightbxd', '2516'): ['horHalfBar("right")', 'vertHalfBar("top", fat, buttB = thickness)'],
	('heavyuprightbxd', '2517'): ['horHalfBar("right", fat)', 'vertHalfBar("top", fat, buttB = thickness*fat)'],
	('lightupleftbxd', '2518'): ['horHalfBar("left")', 'vertHalfBar("top")'],
	('uplightleftheavybxd', '2519'): ['horHalfBar("left", fat)', 'vertHalfBar("top")'],
	('upheavyleftlightbxd', '251A'): ['horHalfBar("left")', 'vertHalfBar("top", fat, buttB = thickness)'],
	('heavyupleftbxd', '251B'): ['horHalfBar("left", fat)', 'vertHalfBar("top", fat, buttB = thickness*fat)'],
	('lightvertrightbxd', '251C'): ['horHalfBar("right")', 'vertBar()'],
	('vertlightrightheavybxd', '251D'): ['horHalfBar("right", fat)', 'vertBar()'],
	('upheavyrightdnlightbxd', '251E'): ['horHalfBar("right")', 'vertHalfBar("top", fat, buttB = thickness)', 'vertHalfBar("bottom")'],
	('dnheavyrightuplightbxd', '251F'): ['horHalfBar("right")', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat, buttT = thickness)'],
	('vertheavyrightlightbxd', '2520'):  ['horHalfBar("right")', 'vertBar(fat)'],
	('dnlightrightupheavybxd', '2521'): ['horHalfBar("right", fat)', 'vertHalfBar("top", fat, buttB = thickness*fat)', 'vertHalfBar("bottom")'],
	('uplightrightdnheavybxd', '2522'): ['horHalfBar("right", fat)', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat, buttT = thickness*fat)'],
	('heavyvertrightbxd', '2523'): ['horHalfBar("right", fat)', 'vertBar(fat)'],
	('lightvertleftbxd', '2524'): ['horHalfBar("left")', 'vertBar()'],
	('vertlightleftheavybxd', '2525'): ['horHalfBar("left", fat)', 'vertBar()'],
	('upheavyleftdnlightbxd', '2526'): ['horHalfBar("left")', 'vertHalfBar("top", fat, buttB = thickness)', 'vertHalfBar("bottom")'],
	('dnheavyleftuplightbxd', '2527'): ['horHalfBar("left")', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat, buttT = thickness)'],
	('vertheavyleftlightbxd', '2528'):  ['horHalfBar("left")', 'vertBar(fat)'],
	('dnlightleftupheavybxd', '2529'): ['horHalfBar("left", fat)', 'vertHalfBar("top", fat, buttB = thickness*fat)', 'vertHalfBar("bottom")'],
	('uplightleftdnheavybxd', '252A'): ['horHalfBar("left", fat)', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat, buttT = thickness*fat)'],
	('heavyvertleftbxd', '252B'): ['horHalfBar("left", fat)', 'vertBar(fat)'],
	('lightdnhorzbxd', '252C'): ['horBar()', 'vertHalfBar("bottom")'],
	('leftheavyrightdnlightbxd', '252D'): ['horHalfBar("left", fat)', 'horHalfBar("right")', 'vertHalfBar("bottom")'],
	('rightheavyleftdnlightbxd', '252E'): ['horHalfBar("left")', 'horHalfBar("right", fat)', 'vertHalfBar("bottom")'],
	('dnlighthorzheavybxd', '252F'): ['horBar(fat)', 'vertHalfBar("bottom")'],
	('dnheavyhorzlightbxd', '2530'): ['horBar()', 'vertHalfBar("bottom", fat)'],
	('rightlightleftdnheavybxd', '2531'): ['horHalfBar("left", fat)','horHalfBar("right")', 'vertHalfBar("bottom", fat, buttT = thickness*fat)'],
	('leftlightrightdnheavybxd', '2532'): ['horHalfBar("left")', 'horHalfBar("right", fat)', 'vertHalfBar("bottom", fat, buttT = thickness*fat)'],
	('heavydnhorzbxd', '2533'): ['horBar(fat)', 'vertHalfBar("bottom", fat)'],
	('lightuphorzbxd', '2534'): ['horBar()', 'vertHalfBar("top")'],
	('leftheavyrightuplightbxd', '2535'): ['horHalfBar("left", fat)', 'horHalfBar("right")', 'vertHalfBar("top")'],
	('rightheavyleftuplightbxd', '2536'): ['horHalfBar("left")', 'horHalfBar("right", fat)', 'vertHalfBar("top")'],
	('uplighthorzheavybxd', '2537'): ['horBar(fat)', 'vertHalfBar("top")'],
	('upheavyhorzlightbxd', '2538'): ['horBar()', 'vertHalfBar("top", fat)'],
	('rightlightleftupheavybxd', '2539'): ['horHalfBar("left", fat)','horHalfBar("right")', 'vertHalfBar("top", fat, buttB = thickness*fat)'],
	('leftlightrightupheavybxd', '253A'): ['horHalfBar("left")', 'horHalfBar("right", fat)', 'vertHalfBar("top", fat, buttB = thickness*fat)'],
	('heavyuphorzbxd', '253B'): ['horBar(fat)', 'vertHalfBar("top", fat)'],
	('lightverthorzbxd', '253C'): ['horBar()', 'vertBar()'],
	('leftheavyrightvertlightbxd', '253D'): ['horHalfBar("left", fat)', 'horHalfBar("right")', 'vertBar()'],
	('rightheavyleftvertlightbxd', '253E'): ['horHalfBar("left")', 'horHalfBar("right", fat)', 'vertBar()'],
	('vertlighthorzheavybxd', '253F'): ['horBar(fat)', 'vertBar()'],
	('upheavydnhorzlightbxd', '2540'): ['horBar()', 'vertHalfBar("top", fat)', 'vertHalfBar("bottom")'],
	('dnheavyuphorzlightbxd', '2541'): ['horBar()', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat)'],
	('vertheavyhorzlightbxd', '2542'): ['horBar()', 'vertBar(fat)'],
	('leftupheavyrightdnlightbxd', '2543'): ['horHalfBar("left", fat, buttR = thickness*fat)', 'horHalfBar("right")', 'vertHalfBar("top", fat)', 'vertHalfBar("bottom")'],
	('rightupheavyleftdnlightbxd', '2544'): ['horHalfBar("left")', 'horHalfBar("right", fat, buttL = thickness*fat)', 'vertHalfBar("top", fat)', 'vertHalfBar("bottom")'],
	('leftdnheavyrightuplightbxd', '2545'): ['horHalfBar("left", fat, buttR = thickness*fat)', 'horHalfBar("right")', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat)'],
	('rightdnheavyleftuplightbxd', '2546'): ['horHalfBar("left")', 'horHalfBar("right", fat, buttL = thickness*fat)', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat)'],
	('dnlightuphorzheavybxd', '2547'): ['horBar(fat)', 'vertHalfBar("top", fat)', 'vertHalfBar("bottom")'],
	('uplightdnhorzheavybxd', '2548'): ['horBar(fat)', 'vertHalfBar("top")', 'vertHalfBar("bottom", fat)'],
	('rightlightleftvertheavybxd', '2549'): ['horHalfBar("left", fat)', 'horHalfBar("right")', 'vertBar(fat)'],
	('leftlightrightvertheavybxd', '254A'): ['horHalfBar("left")', 'horHalfBar("right", fat)', 'vertBar(fat)'],
	('heavyverthorzbxd', '254B'): ['horBar(fat)', 'vertBar(fat)'],
	('lightdbldashhorzbxd', '254C'): ['dashedHorLine(boxPen, 2, width, thickness)'],
	('heavydbldashhorzbxd', '254D'): ['dashedHorLine(boxPen, 2, width, thickness*fat)'],
	('lightdbldashvertbxd', '254E'): ['dashedVertLine(boxPen, 2, blockHeight, thickness)'],
	('heavydbldashvertbxd', '254F'): ['dashedVertLine(boxPen, 2, blockHeight, thickness*fat)'],
	('dblhorzbxd', '2550'): ['horSplitBar()'],
	('dblvertbxd', '2551'): ['vertSplitBar()'],
	('dnsngrightdblbxd', '2552'): ['horSplitHalfBar("right")', 'vertHalfBar("bottom", buttT = 3*thickness)'],
	('dndblrightsngbxd', '2553'): ['horHalfBar("right")', 'vertSplitHalfBar("bottom", buttT = thickness)'],
	('dbldnrightbxd', '2554'): ['outerCorner("right", "bottom")', 'innerCorner("right", "bottom")'],
	('dnsngleftdblbxd', '2555'): ['horSplitHalfBar("left")', 'vertHalfBar("bottom", buttT = 3*thickness)'],
	('dndblleftsngbxd', '2556'): ['horHalfBar("left")', 'vertSplitHalfBar("bottom", buttT = thickness)'],
	('dbldnleftbxd', '2557'): ['outerCorner("left", "bottom")', 'innerCorner("left", "bottom")'],
	('upsngrightdblbxd', '2558'): ['horSplitHalfBar("right")', 'vertHalfBar("top", buttB = 3*thickness)'],
	('updblrightsngbxd', '2559'): ['horHalfBar("right")', 'vertSplitHalfBar("top", buttB = thickness)'],
	('dbluprightbxd', '255A'): ['outerCorner("right", "top")', 'innerCorner("right", "top")'],
	('upsngleftdblbxd', '255B'): ['horSplitHalfBar("left")', 'vertHalfBar("top", buttB = 3*thickness)'],
	('updblleftsngbxd', '255C'): ['horHalfBar("left")', 'vertSplitHalfBar("top", buttB = thickness)'],
	('dblupleftbxd', '255D'): ['outerCorner("left", "top")', 'innerCorner("left", "top")'],
	('vertsngrightdblbxd', '255E'): ['horSplitHalfBar("right")', 'vertBar()'],
	('vertdblrightsngbxd', '255F'): ['horHalfBar("right", buttL = thickness*-1)', 'vertSplitBar()'],
	('dblvertrightbxd', '2560'): ['vertLine(boxPen, (width/2-thickness,median-height/2), (width/2-thickness,median+height/2), thickness)', 'innerCorner("right", "top")', 'innerCorner("right", "bottom")'],
	('vertsngleftdblbxd', '2561'): ['horSplitHalfBar("left")', 'vertBar()'],
	('vertdblleftsngbxd', '2562'): ['horHalfBar("left", buttR = thickness*-1)', 'vertSplitBar()'],
	('dblvertleftbxd', '2563'): ['vertLine(boxPen, (width/2+thickness,median-height/2), (width/2+thickness,median+height/2), thickness)', 'innerCorner("left", "top")', 'innerCorner("left", "bottom")'],
	('dnsnghorzdblbxd', '2564'): ['horSplitBar()', 'vertLine(boxPen, (width/2, median-height/2), (width/2, median-thickness), thickness)'],
	('dndblhorzsngbxd', '2565'): ['horBar()', 'vertSplitHalfBar("bottom")'],
	('dbldnhorzbxd', '2566'): ['horLine(boxPen, (0,median+thickness), (width,median+thickness), thickness, thickness, thickness)', 'innerCorner("left", "bottom")', 'innerCorner("right", "bottom")'],
	('upsnghorzdblbxd', '2567'): ['horSplitBar()', 'vertLine(boxPen, (width/2, median+thickness), (width/2, median+height/2), thickness)'],
	('updblhorzsngbxd', '2568'): ['horBar()', 'vertSplitHalfBar("top")'],
	('dbluphorzbxd', '2569'): ['horLine(boxPen, (0,median-thickness), (width,median-thickness), thickness, thickness, thickness)', 'innerCorner("left", "top")', 'innerCorner("right", "top")'],
	('vertsnghorzdblbxd', '256A'): ['horSplitBar()', 'vertBar()'],
	('vertdblhorzsngbxd', '256B'): ['horBar()', 'vertSplitBar()'],
	('dblverthorzbxd', '256C'): ['innerCorner("left", "top")', 'innerCorner("right", "top")', 'innerCorner("left", "bottom")', 'innerCorner("right", "bottom")'],
 	('lightarcdnrightbxd', '256D'): ['arc(boxPen, (width/2,median-height/2), (width,median), "TL", thickness, radius, thickness)'],
	('lightarcdnleftbxd', '256E'): ['arc(boxPen, (width/2,median-height/2), (0,median), "TR", thickness, radius, thickness)'],
	('lightarcupleftbxd', '256F'): ['arc(boxPen, (width/2,median+height/2), (0,median), "BR", thickness, radius, thickness)'],
	('lightarcuprightbxd', '2570'): ['arc(boxPen, (width/2,median+height/2), (width,median), "BL", thickness, radius, thickness)'],
	('lightdiaguprightdnleftbxd', '2571'): ['diagonalBottomUp(boxPen, (0,median-blockHeight/2), (width,median+blockHeight/2), thickness)'],
	('lightdiagupleftdnrightbxd', '2572'): ['diagonalTopDown(boxPen, (0,median+blockHeight/2), (width,median-blockHeight/2), thickness)'],
	('lightdiagcrossbxd', '2573'): ['diagonalTopDown(boxPen, (0,median+blockHeight/2), (width,median-blockHeight/2), thickness)', 'diagonalBottomUp(boxPen, (0,median-blockHeight/2), (width,median+blockHeight/2), thickness)'],
	('lightleftbxd', '2574'): ['horHalfBar("left")'],
	('lightupbxd', '2575'): ['vertHalfBar("top", buttB = thickness)'],
	('lightrightbxd', '2576'): ['horHalfBar("right")'],
	('lightdnbxd', '2577'): ['vertHalfBar("bottom", buttT = thickness)'],
	('heavyleftbxd', '2578'): ['horHalfBar("left", fat)'],
	('heavyupbxd', '2579'): ['vertHalfBar("top", fat, buttB = thickness)'],
	('heavyrightbxd', '257A'): ['horHalfBar("right", fat)'],
	('heavydnbxd', '257B'): ['vertHalfBar("bottom", fat, buttT = thickness)'],
	('lightleftheavyrightbxd', '257C'): ['horHalfBar("left")', 'horHalfBar("right", fat)'],
	('lightupheavydnbxd', '257D'): ['vertHalfBar("top")', 'vertHalfBar("bottom", fat, buttT = thickness)'],
	('heavyleftlightrightbxd', '257E'): ['horHalfBar("right")', 'horHalfBar("left", fat)'],
	('heavyuplightdnbxd', '257F'): ['vertHalfBar("bottom")','vertHalfBar("top", fat, buttB = thickness)'],
	('uphalfblock', '2580'): ['box(boxPen, (blockOrigin[0], median), blockTop)'],
	('dneighthblock', '2581'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*1/8))'],
	('dnquarterblock', '2582'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*1/4))'],
	('dnthreeeighthsblock', '2583'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*3/8))'],
	('dnhalfblock', '2584'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*1/2))'],
	('dnfiveeighthsblock', '2585'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*5/8))'],
	('dnthreequartersblock', '2586'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*3/4))'],
	('dnseveneighthsblock', '2587'): ['box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*7/8))'],
	('fullblock', '2588'): ['box(boxPen, blockOrigin, blockTop)'],
	('leftseveneighthsblock', '2589'): ['box(boxPen, blockOrigin, (width*7/8, blockTop[1]))'],
	('leftthreequartersblock', '258A'): ['box(boxPen, blockOrigin, (width*3/4, blockTop[1]))'],
	('leftfiveeighthsblock', '258B'): ['box(boxPen, blockOrigin, (width*5/8, blockTop[1]))'],
	('lefthalfblock', '258C'): ['box(boxPen, blockOrigin, (width*1/2, blockTop[1]))'],
	('leftthreeeighthsblock', '258D'): ['box(boxPen, blockOrigin, (width*3/8, blockTop[1]))'],
	('leftquarterblock', '258E'): ['box(boxPen, blockOrigin, (width*1/4, blockTop[1]))'],
	('lefteighthblock', '258F'): ['box(boxPen, blockOrigin, (width*1/8, blockTop[1]))'],
	('righthalfblock', '2590'): ['box(boxPen, (width/2, blockOrigin[1]), blockTop)'],
	('lightshade', '2591'):  ['stripedShade(boxPen, "25")'],
	('mediumshade', '2592'): ['stripedShade(boxPen, "50")'],
	('darkshade', '2593'):  ['stripedShade(boxPen, "75")'],
	('upeighthblock', '2594'): ['box(boxPen, (blockOrigin[0], blockOrigin[1]+blockHeight*7/8), blockTop)'],
	('righteighthblock', '2595'): ['box(boxPen, (width*7/8, blockOrigin[1]), blockTop)'],
	('dnleftquadrant', '2596'): ['box(boxPen, blockOrigin, (width*1/2, blockOrigin[1]+blockHeight*1/2))'],
	('dnrightquadrant', '2597'): ['box(boxPen, (width/2, blockOrigin[1]), (blockTop[0], median))'],
	('upleftquadrant', '2598'): ['box(boxPen, (blockOrigin[0], median), (width*1/2, blockTop[1]))'],
	('upleftdnleftdnrightquadrant', '2599'): ['box(boxPen, blockOrigin, (width*1/2, blockTop[1]))', 'box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*1/2))'],
	('upleftdnrightquadrant', '259A'): ['box(boxPen, (width/2, blockOrigin[1]), (blockTop[0], median))', 'box(boxPen, (blockOrigin[0], median), (width*1/2, blockTop[1]))'],
	('upleftuprightdnleftquadrant', '259B'): ['box(boxPen, blockOrigin, (width*1/2, blockTop[1]))', 'box(boxPen, (blockOrigin[0], median), blockTop)'],
	('upleftuprightdnrightquadrant', '259C'): ['box(boxPen, (width/2, blockOrigin[1]), blockTop)', 'box(boxPen, (blockOrigin[0], median), blockTop)'],
	('uprightquadrant', '259D'): ['box(boxPen, (width/2, median), blockTop)'],
	('uprightdnleftquadrant', '259E'): ['box(boxPen, blockOrigin, (width*1/2, blockOrigin[1]+blockHeight*1/2))', 'box(boxPen, (width/2, median), blockTop)'],
	('uprightdnleftdnrightquadrant', '259F'): ['box(boxPen, (width/2, blockOrigin[1]), blockTop)', 'box(boxPen, blockOrigin, (width, blockOrigin[1]+blockHeight*1/2))'],
}


def drawRect(pen, BL, BR, TR, TL):
	"General drawing function for a rectangle."

	pen.moveTo(BL) 
	pen.lineTo(BR)
	pen.lineTo(TR)
	pen.lineTo(TL)
	pen.closePath() 


def drawArc(pen, start1, start2, end1, end2, IAstart, IApoint1, IApoint2, IAend, OAstart, OApoint1, OApoint2, OAend):
	"General drawing function for an arc."

	pen.moveTo(start1)
	pen.lineTo(start2) 
	pen.lineTo(IAstart) 
	pen.curveTo(IApoint1, IApoint2, IAend) 
	pen.lineTo(end1)
	pen.lineTo(end2)
	pen.lineTo(OAstart) 
	pen.curveTo(OApoint1, OApoint2, OAend)

	pen.closePath() 


def horLine(pen, start, end, thickness, buttL=0, buttR=0): 
	"General drawing function for a horizontal line."

	startX = start[0]
	startY = start[1]
	endX = end[0]
	endY = end[1]

	BL = (startX-buttL/2, endY-thickness/2)
	BR = (endX+buttR/2, endY-thickness/2)
	TR = (endX+buttR/2, endY+thickness/2)
	TL = (startX-buttL/2, startY+thickness/2)

	drawRect(pen, BL, BR, TR, TL)


def vertLine(pen, start, end, thickness, buttB=0, buttT=0): 
	"General drawing function for a vertical line."

	startX = start[0]
	startY = start[1]
	endX = end[0]
	endY = end[1]
		
	BL = (startX-thickness/2, startY-buttB/2)
	BR = (startX+thickness/2, startY-buttB/2)
	TR = (startX+thickness/2, endY+buttT/2)
	TL = (startX-thickness/2, endY+buttT/2)

	drawRect(pen, BL, BR, TR, TL)


def box(pen, start, end, buttH=0, buttV=0):
	"A box."

	startX = start[0]
	startY = start[1]
	endX = end[0]
	endY = end[1]
	
	BL = (startX-buttH/2, startY-buttV/2)
	BR = (endX+buttH/2, startY-buttV/2)
	TR = (endX+buttH/2, endY+buttV/2)
	TL = (startX-buttH/2, endY+buttV/2)

	drawRect(pen, BL, BR, TR, TL)


def dashedHorLine(pen, step, width, thickness):
	"Dashed horizontal bar."

	stepLength = width/step
	gap = stepLength/step
	for w in range(0, width, stepLength):
		if w+stepLength-gap < width:
			w = w+gap/2 # centering the dashed line in the glyph
			horLine(boxPen, (w,median), (w+stepLength-gap,median), thickness)


def dashedVertLine(pen, step, length, thickness):
	"Dashed vertical bar."

	stepLength = length/step
	gap = stepLength/step
	for h in range(median-length/2, median+length/2, stepLength):
		if h+stepLength-gap < length:
			h = h+gap/2
			vertLine(boxPen, (width/2,h), (width/2,h+stepLength-gap), thickness)


def shade(pen, shade):
	"Shading patterns, consisting of little boxes."
	# Not used, but maybe useful for somebody.

	vstep = 50
	hstep = 100
	if shade == '25':
		boxWidth = 20
		boxHeight = 30
	if shade == '50':
		boxWidth = 40
		boxHeight = 50
	if shade == '75':
		boxWidth = 45
		boxHeight = 70

	for w in range(0, width, hstep):
		for h in range(median-blockHeight/2, median+blockHeight/2, vstep*2):
			box(boxPen, (w, h), (w+boxWidth, h+boxHeight))
			box(boxPen, (w+hstep/2, h+vstep), (w+boxWidth+hstep/2, h+boxHeight+vstep))


def diagonalBottomUp(pen, start, end, butt=0): 
	"Diagonal line from bottom left to top right; with overhang."

	startX = start[0]
	startY = start[1]
	endX = end[0]
	endY = end[1]
	
	BL1 = (startX-butt/2, startY+butt/2)
	BL2 = (startX-butt/2, startY-butt/2)
	BL3 = (startX+butt/2, startY-butt/2)
	TR1 = (endX+butt/2, endY-butt/2)
	TR2 = (endX+butt/2, endY+butt/2)
	TR3 = (endX-butt/2, endY+butt/2)
	
	pen.moveTo(BL1) 
	pen.lineTo(BL2)
	pen.lineTo(BL3)
	pen.lineTo(TR1)
	pen.lineTo(TR2)
	pen.lineTo(TR3)
	pen.closePath() 


def diagonalTopDown(pen, start, end, butt=0): 
	"Diagonal line from top left to bottom right; with overhang."

	startX = start[0]
	startY = start[1]
	endX = end[0]
	endY = end[1]
	
	TL1 = (startX+butt/2, startY+butt/2)
	TL2 = (startX-butt/2, startY+butt/2)
	TL3 = (startX-butt/2, startY-butt/2)
	BR1 = (endX-butt/2, endY-butt/2)
	BR2 = (endX+butt/2, endY-butt/2)
	BR3 = (endX+butt/2, endY+butt/2)

	pen.moveTo(TL1)
	pen.lineTo(TL2)
	pen.lineTo(TL3)
	pen.lineTo(BR1) 
	pen.lineTo(BR2)
	pen.lineTo(BR3)
	pen.closePath() 


def arc(pen, start, end, side, thickness, radius, butt=0):
	"Rounded corner."
	
	kappa = 4*(sqrt(2)-1)/3
	# Bezier point distance for drawing circles.
	
	if side == 'TL':
		yflip = 1
		xflip = 1
	if side == 'BL':
		yflip = -1
		xflip = 1
	if side == 'TR':
		yflip = 1
		xflip = -1
	if side == 'BR':
		yflip = -1
		xflip = -1
	
	startX = start[0]
	startY = start[1]
	endX = end[0]
	endY = end[1]

	cStartX = startX
	cStartY = endY-(radius*yflip)
	cEndX = startX+(radius*xflip)
	cEndY = endY

	start1 = (startX-(thickness/2*xflip), startY)
	start2 = (startX+(thickness/2*xflip), startY)
	end1 = (endX+(butt/2*xflip), endY-(thickness/2*yflip))
	end2 = (endX+(butt/2*xflip), endY+(thickness/2*yflip))
	
	IAstart = (cStartX+(thickness/2*xflip),cStartY)
	IApoint1 = (cStartX+(thickness/2*xflip),cStartY+((radius-thickness/2)*kappa*yflip))
	IApoint2 = (cEndX-((radius-thickness/2)*kappa*xflip),cEndY-(thickness/2*yflip))
	IAend =  (cEndX,cEndY-(thickness/2*yflip))

	OAstart = (cEndX,cEndY+(thickness/2*yflip))
	OApoint1 = (cEndX-((radius+thickness/2)*kappa*xflip), cEndY+(thickness/2*yflip))
	OApoint2 = (cStartX-(thickness/2*xflip), cStartY+((radius+thickness/2)*kappa*yflip))
	OAend =  (cStartX-(thickness/2*xflip),cStartY)

	drawArc(pen, start1, start2, end1, end2, IAstart, IApoint1, IApoint2, IAend, OAstart, OApoint1, OApoint2, OAend)


def horBar(fatness=1, buttL=thickness, buttR=thickness):
	"Horizontal bar."

	horLine(boxPen, (0,median), (width,median), thickness*fatness, buttL, buttR)


def vertBar(fatness=1, buttB=0, buttT=0):
	"Vertical bar."

	vertLine(boxPen, (width/2,median-height/2), (width/2,median+height/2), thickness*fatness, buttB, buttT)


def horHalfBar(side, fatness=1, buttL=thickness, buttR=thickness):
	"Half-width horizontal bar, left or right."

	if side == 'left':
		horLine(boxPen, (0,median), (width/2,median), thickness*fatness, buttL, buttR)
	elif side == 'right':
		horLine(boxPen, (width/2,median), (width,median), thickness*fatness, buttL, buttR)


def vertHalfBar(fold, fatness=1, buttB=0, buttT=0):
	"Half-height vertical bar, top or bottom."
	
	if fold == 'top':
		vertLine(boxPen, (width/2,median), (width/2,median+height/2), thickness*fatness, buttB, buttT)
	if fold == 'bottom':
		vertLine(boxPen, (width/2,median-height/2), (width/2,median), thickness*fatness, buttB, buttT)
		

def horSplitBar(fatness=1):
	"Double-stroked horizontal bar, left or right."

	# moving the median up and down. Not very elegant, but it works.
	global median
	median += thickness * fatness
	horBar(fatness)
	median -= thickness * fatness
	
	median -= thickness * fatness
	horBar(fatness)
	median += thickness * fatness


def vertSplitBar(fatness=1, buttB=0, buttT=0):
	"Double-stroked vertical bar, top or bottom."

	leftX = width/2-(thickness*fatness)
	rightX = width/2+(thickness*fatness)
	vertLine(boxPen, (leftX,median-height/2), (leftX,median+height/2), thickness*fatness, buttB, buttT)
	vertLine(boxPen, (rightX,median-height/2), (rightX,median+height/2), thickness*fatness, buttB, buttT)


def horSplitHalfBar(side, fatness=1):
	"Double-stroked half-width horizontal bar, left or right."

	global median
	median += thickness * fatness
	horHalfBar(side)
	median -= thickness * fatness
	
	median -= thickness * fatness
	horHalfBar(side)
	median += thickness * fatness


def vertSplitHalfBar(fold, fatness=1, buttB=0, buttT=0):
	"Double-stroked half-height vertical bar, top or bottom."

	leftX = width/2- thickness*fatness
	rightX = width/2+ thickness*fatness
	if fold == 'top':
		vertLine(boxPen, (leftX,median), (leftX,median+height/2), thickness*fatness, buttB, buttT)
		vertLine(boxPen, (rightX,median), (rightX,median+height/2), thickness*fatness, buttB, buttT)
	if fold == 'bottom':
		vertLine(boxPen, (leftX,median-height/2), (leftX,median), thickness*fatness, buttB, buttT)
		vertLine(boxPen, (rightX,median-height/2), (rightX,median), thickness*fatness, buttB, buttT)


def outerCorner(side, fold, fatness=1):
	"Outer part of a double-stroked corner."

	global median
	
	if fold == 'top':
		median -= thickness * fatness
	if fold == 'bottom':
		median += thickness * fatness

	if side == 'right':
		horHalfBar(side, buttL = 3*thickness)
		x = width/2- thickness*fatness

	if side == 'left':
		horHalfBar(side, buttR = 3*thickness)
		x = width/2+ thickness*fatness

	if fold == 'top':
		median += thickness * fatness
	if fold == 'bottom':
		median -= thickness * fatness

	if fold == 'top':
		vertLine(boxPen, (x,median), (x,median+height/2), thickness*fatness, buttB = 3*thickness)
	if fold == 'bottom':
		vertLine(boxPen, (x,median-height/2), (x,median), thickness*fatness, buttT = 3*thickness)


def innerCorner(side, fold, fatness=1):
	"Inner part of a double-stroked corner."
	
	global median

	if fold == 'top':
		median += thickness * fatness

	if fold == 'bottom':
		median -= thickness * fatness

	if side == 'right':
		horHalfBar(side, buttL = -1*thickness)
		x = width/2+ thickness*fatness

	if side == 'left':
		horHalfBar(side, buttR = -1*thickness)
		x = width/2- thickness*fatness

	if fold == 'top':
		median -= thickness * fatness

	if fold == 'bottom':
		median += thickness * fatness

	if fold == 'top':
		vertLine(boxPen, (x,median), (x,median+height/2), thickness*fatness, buttB = -1*thickness)
	if fold == 'bottom':
		vertLine(boxPen, (x,median-height/2), (x,median), thickness*fatness, buttT = -1*thickness)


def stripedShade(pen, shade):
	"Shading patterns, consisting of diagonal lines boxes."
	# This function assumes a bunch of right triangles being moved across the width of the glyph.
	# Below, the law of sines is used for start-and endpoint calculations.

	if shade == '25':
		step = width/2
	if shade == '50':
		# step = width/10
		step = width/4
	if shade == '75':
		step = width/8

	line = width/20
	diagonal = sqrt(width**2+blockHeight**2)
	angle = asin(blockHeight/diagonal)

	# There is also an an alternative angle, if so desired.
	# angle_alt = asin(width/diagonal)
	
	max = int(round(width + (blockHeight * sin(radians(90)-angle))/sin(angle)))
	# To determine where the iteration below can stop, this is the point where the first diagonal line outside the glyph will cross the given baseline.

	widthSteps = []
	for w in range(0, max, step):
		widthSteps.append(w)

	for first in widthSteps:
		second = first+line
		
		start_x = first
		start_x2 = second
		start_y = blockOrigin[1]
		start_y2 = blockOrigin[1]
		target_x = 0
		target_x2 = 0

		if first >= width:
			# At the point where the diagonal exceeds the width of the glyph, the start points must be moved up the right sidebearing.
			start_x = width
			start_x2 = width
			start_y = blockOrigin[1] + ((first-width) * sin(angle))/sin(radians(90)-angle)
			start_y2 = blockOrigin[1] + ((second-width) * sin(angle))/sin(radians(90)-angle)

		target_y = blockOrigin[1] + (first * sin(angle))/sin(radians(90)-angle)
		target_y2 = blockOrigin[1] + (second * sin(angle))/sin(radians(90)-angle)

		if target_y >= blockOrigin[1] + blockHeight:
			# When the diagonal exceeds the bounding box height, the end points must be moved along the top of the glyph.
			target_x = first - (blockHeight * sin(radians(90)-angle)/sin(angle))
			target_x2 = second - (blockHeight * sin(radians(90)-angle)/sin(angle))
			target_y = blockOrigin[1] + blockHeight
			target_y2 = blockOrigin[1] + blockHeight
		
		BL = (start_x, start_y)
		BR = (start_x2, start_y2)
		TR = (target_x2, target_y2)
		TL = (target_x, target_y)

		if not target_x >= width:
  		    drawRect(pen, BL, BR, TR, TL)


def removeOverlapForGlyphs(glyphname):
	# seriously.
	Glyph = GlyphsFont.glyphs[glyphname]
	Layer = Glyph.layerForKey_(FontMaster.id)
	removeOverlapFilter = NSClassFromString("GlyphsFilterRemoveOverlap").alloc().init()
	removeOverlapFilter.runFilterWithLayer_error_(Layer, None)

	
# Here, the main job is done:

if fontExists:
	print 'Drawing boxes ...'

	generatedGlyphs = []
	# Keeping track of the glyph order

	for name, uni in sorted(names, key=lambda x: int(x[1], 16)):
		# sorting the dictionary by the unicode value of the glyph.
		generatedGlyphs.append(name)
		commands = names[name, uni] 
		print name		
		
		g = f.newGlyph(name, clear=True)
		g.width = width
		boxPen = g.getPen()
		for command in commands:
			exec(command)

		if inGlyphs:
			removeOverlapForGlyphs(name)
			g.correctDirection()

		if any((inRF, inFL)):
			g.removeOverlap()
			g.correctDirection()
		
		g.unicode = int(uni, 16)
		g.update()
			
	f.update()	


	if inShell:
		timeString = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
		fileName = '%s_boxes.ufo' % timeString
		f.lib['public.glyphOrder'] = generatedGlyphs
		f.save(os.path.expanduser('~/Desktop/%s' % fileName))

	if inFL:
		fl.UpdateFont(fl.ifont)

	if inRF:
	    # Modifying the glyph order, so it looks like the glyphs have been appended at the end of the font.
	    oldGlyphOrder = [ g for g in f.lib['public.glyphOrder'] if g not in generatedGlyphs ]
	    newGlyphOrder = oldGlyphOrder + generatedGlyphs 
	    f.glyphOrder = newGlyphOrder
	    f.lib['public.glyphOrder'] = newGlyphOrder

	print '\nDone.'
	    