import subprocess

#subprocess.run("ls")
#subprocess.run(["ls", "-la"]) # liste d'arguments (commande + arguments)
#subprocess.run("ls -la", shell=True)

#out = subprocess.run(["ls", "-la"], capture_output=True, text=True)
#print(out.args)
#print(out.returncode)
#print(out.stdout.decode()) # decode() => byte => str
#print(out.stdout)

# redirection de la sortie standard vers un fichier
# with open("output.txt", "w") as f:
#   out = subprocess.run(["ls", "-la"], stdout=f, text=True)

# stderr=subprocess.DEVNULL
#out = subprocess.run(["ls", "-la", "-z"], capture_output=True, text=True)
#print(out.stderr)
# if out.returncode != 0:
#   print("La commande a échoué")

# https://www.cyberciti.biz/faq/linux-redirect-error-output-to-file/
# équivalent à ls -la -a 2> /dev/null
#out = subprocess.run(["ls", "-la", "-z"], stderr=subprocess.DEVNULL, text=True)


#sp1 = subprocess.run(["cat", "students.txt"], capture_output=True, text=True)
#print(sp1.stdout)

#sp2 = subprocess.run(["cat", "la"], capture_output=True, input=sp1.stdout, text=True)
#print(sp2.stdout)

# les deux commandes ci-dessus peuvent être aussi exécutées en un seule commande:
subprocess.run("cat students.txt | grep la", shell=True)