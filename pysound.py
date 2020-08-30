#   python code
#   script_name: pysong
#   author: Snehesh_dutta
#   description: Cpmposition practice in pyhon
#   set_up

from earsketch import *

init()
setTempo(120)
# chords
music1 = COMMON_LOVE_DRUMBEAT_1
music2 = DUBSTEP_DRUMLOOP_MAIN_013
music3 = CIARA_SET_THEME_MELSYNTH
# music
fitMedia(music1, 1, 1, 16)
fitMedia(music2, 2, 1, 16)
fitMedia(music3, 3, 1, 16)
# addeffect
setEffect(3, DELAY, DELAY_TIME, 500)
setEffect(2, REVERB, REVERB_TIME, 200)
# volume change
setEffect(2, VOLUME, GAIN, -60, 1, 5, 8)
setEffect(2, VOLUME, GAIN, 5, 8, -60, 16)
# finish
finish()
