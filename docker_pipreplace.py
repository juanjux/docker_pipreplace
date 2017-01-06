#!/usr/bin/env python3
__author__ = "Juanjo Alvarez <juanjo@juanjoalvarez.net>"
__license__ = "MIT"

"""
Open the Dockerfile.template, replace the mark ### PIPREPLACE ###
with a list of pip install.

Important: the PIPREPLACE mark must be before any ADD command in the
Dockerfile or this will be for nothing (ADD commands invalidate Docker
image catching from that point on)
"""


def main(reqfile='requirements.txt', dockerfile_template='Dockerfile.template',
        dockerfile_output='Dockerfile', pipcmd='pip2', mark='### PIPREPLACE ###'):

    pipcmds = 'RUN pip install --upgrade pip\n'

    # Open the requirements.txt file, generate pip
    with open(reqfile, 'r') as rf:
        reqlines = rf.readlines()

    for requirement in reqlines:
        pipcmds += 'RUN pip install {}'.format(requirement)

    with open(dockerfile_template, 'r') as dt:
        dt_text = dt.read()

    dt_text = dt_text.replace(mark, pipcmds)

    with open(dockerfile_output, 'w') as dout:
        dout.write(dt_text)


if __name__ == '__main__':
    main()
