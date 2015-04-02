import sys, time, os

# "\033[0;32m done!\033[0m"
#  ^^^^^^^^^^      ^^^^^^^ help me get a green color via ANSI codes
# http://kishorelive.com/2011/12/05/printing-colors-in-the-terminal/

# You have completed x/1000 iterations {done!}
def genericOutput(iterations, iter_time):
    for i in xrange(iterations):
        time.sleep(iter_time)
        sys.stdout.flush()
        sys.stdout.write("\rYou have completed %d/%d iterations " % (i+1, iterations))
    print "\033[0;32m DONE\033[0m"

def hashBar(iterations, iter_time):
    columns = int(os.popen('stty size', 'r').read().split()[1])
    maxWidth = int(7.0*columns/8)

    for i in xrange(iterations):
        ratio = i*1.0/iterations
        hashes = int(ratio*maxWidth)
        bar = hashes * "#" + (maxWidth - hashes) * " "
        sys.stdout.flush()
        sys.stdout.write("\r|%s|" % (bar))
        time.sleep(iter_time)
    print "\033[0;32m done!\033[0m"

#handle input
progressions = {
    "genericOutput" : genericOutput,
    "hashBar" : hashBar,
}
errorMessage = """
###############################################################
# The correct way to call this file is in the form 
# python progressBar.py <iter_time> <iterations> <functionName>
#
# The functions available are:"""

for val in progressions.values():
    errorMessage +=  "\n# " + val.__name__

errorMessage += "\n###############################################################"

# try:
iter_time = float(sys.argv[1])
iterations = int(sys.argv[2])
func = progressions[sys.argv[3]]

func(iterations, iter_time)
# except:
#     print errorMessage