from guizero import App, Text, PushButton, TextBox
def hash():
  value = input.value
  hashedd = 0
  hashed = []
  for i in value[::-1]:
       hashed.append((ord(i)) + 10)
  for i in hashed:
    hashedd = i + hashedd + 58
  out.value = hashedd

    
window = App(title = "Hashing Algorithm")
input = TextBox(window)
button = PushButton(window, text = "Hash" ,command=hash)
out = Text(window)
