__author__ = 'chywoo.park'
import  sargetest


out = sargetest.Capture()
p = sargetest.Pipeline("/Users/chywoo.park/tizen23/tools/sdb devices", stdout=out) #, async=True)
o = p.run(async=True)

print( o.stdout.text )

p.close()
print("END")