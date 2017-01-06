### docker_pipreplace.py

This is a tiny Python (2 and 3 compatible) script that I use to solve the annoying problem of Docker
re-downloading and recompiling on **every** image rebuild every dependency in the `requirements.txt`
file of your Python project if you include it in the image using the ADD command and then do a `RUN
pip install -r requirements.txt`

While the usual proposed alternative to avoid that problem is to write all the `pip install`
commands in the Dockerfile, this has the problem that you now have to maintain two lists if you
want to keep the `requirements.txt` file for your project (*and you really want*).

So this script just reads the `requirements.txt` file and a `Dockerfile.template` file and it 
replaced the mark `### PIPREPLACE ###` with the list of pip install commands. So if you change
anything in your dependencies only that dependency will be downloaded and or compiled. Of course
this will generate a lot more caches but the build will be faster and you will avoid downloads,
which is nice if you are on the go and connected though a limited data plan.
