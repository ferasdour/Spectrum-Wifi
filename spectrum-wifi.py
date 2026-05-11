import random , argparse

wordlist=set([])
def run():
    words=open("words.txt").read().splitlines()
    # generate spectrum default passwords
    while True:
        # Debugging step:
        # time.sleep(5)
        for i in range(0,9):
            number=f"{i:01}"
            guess=str("{}-{}{}-{}".format(random.choice(words).lower(), random.choice(words).lower(), number, random.choice(words)))
            if guess not in wordlist:
                if len(guess) >= 12 and len(guess) <=30:
                    wordlist.add(guess)
                    print(guess)
                else:
                    pass


parser = argparse.ArgumentParser(description='generate spectrum passwords for cracking')
parser.add_argument('--run', required=False, action='store_true', dest='run', help='run after sorted wordlist into verbs and nouns')
args = parser.parse_args()
if args.run:
    run()
else:
    parser.print_help()
