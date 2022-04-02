# AutumnLeaf

1. I added the line  *global counter* before counter+=1 in the tester() function. That allowed me to be able to access a global variable counter.
2. I opened my terminal inside the folder that contains question2.py and entered the command *pytest question2.py*
3. I accessed my environment variable from the dockerfile using *os.environ.get['variable name']* and created my while loop that gets halted when the times from docker file is reached.
4.I cretaed a python script that searches if an environment variable already exists in my env list and created a file called dockerQ4 in my directory. I then opened my terminal and run the following command *docker build -t dockerimage .* it gave me an error about permission being denied I then went to my browser to try and find a solution and i found the following command *sudo chmod 666 /var/run/docker.sock* and after this i managed to build my docker image. I then ran docker images found my image on the list
I attached my screenshot for question 4.
