import mindwave, time

headset = mindwave.Headset('/dev/tty.MindWaveMobile-DevA')
cflag = 0
time.sleep(2)
print "Connecting..."
while True:
    if cflag == 0:
        cflag = 1
        print "Connected."
    else:
        time.sleep(0.5)
        print "Attention: %s, Meditation: %s" % (headset.attention, headset.meditation)

while headset.status != 'connected':
    time.sleep(2)
    if headset.status == 'standby':
        headset.connect()
        print "Retrying connect..."