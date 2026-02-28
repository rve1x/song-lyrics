import time, sys 

lyrics = [
"One day I'm gonna fly away",
"One day when heaven calls my name",
"I lay down I close my eyes at night",
"I can see moon and light",
"One day I'm gonna fly away",
"One day I'll see your eyes again",
"I lay down I close my eyes at night",
"I can see moon and light",
]
for line in lyrics:
    for ch in line+"\n":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(0.6)
