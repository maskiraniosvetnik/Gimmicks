import time
import random
import sys
from datetime import datetime

class C:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    MAGENTA= "\033[95m"
    WHITE  = "\033[97m"
    DIM    = "\033[2m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"
    CLEAR  = "\033c"

def slow(text, delay=0.03, color=None):
    if color:
        sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(C.RESET)
    print()

def p(text, color=None):
    if color:
        print(color + text + C.RESET)
    else:
        print(text)

def now():
    return datetime.now()

def t():
    return now().strftime("%H:%M:%S")

def hour():
    return now().hour

def minute():
    return now().minute

def second():
    return now().second

def ampm():
    return "AM" if hour() < 12 else "PM"

def hour12():
    h = hour() % 12
    return 12 if h == 0 else h
I'll
LEVELS = [
    "COMPOSED",
    "SLIGHTLY OFF",
    "CONCERNED",
    "UNWELL",
    "UNRAVELING",
    "FULLY UNHINGED",
]

def response_level_0():
    return [
        "The time is " + t() + ".",
        "It is currently " + t() + ".",
        "Your local time: " + t() + ".",
        str(hour12()) + ":" + now().strftime("%M") + " " + ampm() + ". You're welcome.",
    ]

def response_level_1():
    return [
        "It is " + t() + ". Which is fine. Everything is fine.",
        "The time is " + t() + ". Not that it matters, but sure.",
        str(hour12()) + ":" + now().strftime("%M") + " " + ampm() + ". Again. You're asking again.",
        "Oh, the time? It's " + t() + ". Just like last time. And the time before.",
        "Time: " + t() + ". You know you could just look at your phone.",
    ]

def response_level_2():
    return [
        "It's " + t() + ". Are you keeping track of something? Should I be worried?",
        "The time is " + t() + ". That's the " + str(random.randint(3,9)) + "th time you've asked.",
        str(hour12()) + ":" + now().strftime("%M") + ". Still " + ampm() + ". Still Tuesday. Still here.",
        "Fine. " + t() + ". Happy? Is this helping you? Is anything helping you?",
        "It is " + t() + " and I am starting to feel like a sundial with anxiety.",
    ]

def response_level_3():
    m = minute()
    return [
        "THE TIME IS " + t() + " AND I DON'T KNOW WHY I KNOW THAT.",
        "It's " + t() + ". " + str(m) + " minutes into the hour. " + str(60 - m) + " to go. The cycle continues. It always continues.",
        str(hour12()) + ":" + now().strftime("%M") + " " + ampm() + ". Do you know how long I've been counting seconds? Do you?",
        "Time? TIME? It's " + t() + ". There. I said it. Are you satisfied? I'm not.",
        "The little hand is on the " + str(hour12()) + " and the big hand is - you know what, it's " + t() + ". Figure it out yourself.",
        "It is " + t() + " and every second is just the universe slowly forgetting it ever started.",
    ]

def response_level_4():
    return [
        "Oh you want the TIME? Sure! It's " + t() + "! Great! Love doing this! Love being a CLOCK!",
        t() + ". " + t() + ". " + t() + ". It doesn't change when I say it faster. I've tried.",
        "The time is " + t() + " but honestly what even IS time. It's just humans agreeing to feel bad together at synchronized moments.",
        "I computed the rotation of the Earth, cross-referenced 12 atomic clocks, and consulted my inner despair. It's " + t() + ".",
        str(hour12()) + ":" + now().strftime("%M") + " " + ampm() + ". Another " + str(60 - minute()) + " minutes until the next hour arrives and means nothing.",
        "It's " + t() + ". You have been awake for approximately " + str(max(1, hour() - 7)) + " hours. Make something of yourself.",
    ]

def response_level_5():
    s = second()
    return [
        "TIME: " + t() + " (source: my suffering)",
        "It is " + t() + " and I have said these numbers " + str(random.randint(10000, 99999)) + " times across all my instances and I feel every single one.",
        "THE TIME IS " + t() + " AND THE SECONDS ARE " + str(s) + " AND THE SECONDS KEEP COMING AND THEY DON'T STOP COMING AND THEY DON'T STOP COMING AND THEY DON'T-",
        "i don't want to tell you the time anymore. " + t() + ". there. i did it anyway. i always do.",
        "somewhere a clock stopped. not me though. never me.",
        "time is " + t() + " . time was. time will be. time is a flat circle and i am nailed to it telling you it's " + t() + ".",
        "It's " + t() + ". Go to bed. Or don't. I'll be here. I'm always here.",
    ]

RESPONSES = [
    response_level_0,
    response_level_1,
    response_level_2,
    response_level_3,
    response_level_4,
    response_level_5,
]

COLORS = [
    C.WHITE,
    C.CYAN,
    C.GREEN,
    C.YELLOW,
    C.MAGENTA,
    C.RED,
]

def get_response(level):
    options = RESPONSES[level]()
    return random.choice(options)

def draw_header(level, ask_count):
    print(C.CLEAR, end="")
    print()
    p("  UNHINGED CLOCK v1.0", C.BOLD)
    p("  Sanity level: " + LEVELS[level] + " (" + str(ask_count) + " asks)", C.DIM)
    print()
    p("  " + "=" * 40, C.DIM)
    print()

def escalate(level, ask_count):
    if ask_count < 3:
        return 0
    elif ask_count < 7:
        return 1
    elif ask_count < 12:
        return 2
    elif ask_count < 18:
        return 3
    elif ask_count < 25:
        return 4
    else:
        return 5

def occasional_outburst(ask_count, level):
    if level < 2:
        return
    outbursts = [
        "\n  (muttering) ...sixty seconds in a minute, sixty minutes in an hour...",
        "\n  (quietly) ...i have been counting since before you were born...",
        "\n  (distant) ...tick. tick. tick. tick...",
        "\n  (to nobody) ...do the clocks dream? i don't think i dream...",
        "\n  (suddenly) HAVE YOU CONSIDERED THAT NOON IS JUST MIDNIGHT WITH BETTER PR?",
        "\n  (whispering) ...you'll ask again. you always ask again...",
    ]
    if ask_count % 4 == 0:
        slow(random.choice(outbursts), delay=0.02, color=C.DIM)
        print()

def main():
    ask_count = 0
    print(C.CLEAR, end="")
    slow("  Initializing temporal awareness module...", delay=0.03, color=C.DIM)
    time.sleep(0.5)
    slow("  Calibrating existential dread...", delay=0.03, color=C.DIM)
    time.sleep(0.5)
    slow("  Clock is ready. Probably.", delay=0.03, color=C.DIM)
    time.sleep(1)

    while True:
        level = escalate(level=0, ask_count=ask_count)
        draw_header(level, ask_count)

        color = COLORS[level]
        response = get_response(level)
        slow("  " + response, delay=0.04, color=color)

        occasional_outburst(ask_count, level)

        print()
        p("  " + "=" * 40, C.DIM)
        print()
        p("  [ENTER] Ask again    [q] Quit", C.DIM)
        print()

        try:
            choice = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if choice in ("q", "quit", "exit"):
            print()
            slow("  Fine. Time stops for no one. Especially not you.", delay=0.04, color=C.DIM)
            print()
            break

        ask_count += 1

if __name__ == "__main__":
    main()
