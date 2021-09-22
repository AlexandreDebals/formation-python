import platform, os

# print(platform.processor())
# print(platform.system())
# print(os.name)
# print(os.getcwd())

for x in range(5):
  #os.mkdir('tmp_' + str(x+1))
  os.rmdir('tmp_' + str(x+1))