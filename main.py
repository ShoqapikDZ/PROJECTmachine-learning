# Imports 
from replit import db
#Classes

class User:
  def __init__(self, identifiant, password):
    self.password = password
    self.identifiant = identifiant

  def register(self):
    self.db = open("users.txt","r+" , encoding="utf-8")
    self.db.write(f"{self.identifiant} | {self.password};\n")

class Books: 
  def __init__(self, genre, title, author, book_id, is_emprunté, emprunteur, edition):
    self.genre = genre
    self.title = title
    self.author = author
    self.book_id = book_id
    self.is_emprunté = is_emprunté
    self.emprunteur = emprunteur
    self.edition = edition

#Outils 
def Print_users():
  users = open("users.txt", "r+", encoding="utf-8").read().split(";\n")
  id = 0
  for user in users : 
    id += 1 
    if " | " in user :
      user = user.split(" | ")
      identifiant = user[0]
      password = user[1]
      print(f"    User Number : {id} \nNom d'utilisateur : {identifiant} \nMot de passe : {password} \n\n")


CLI = input("Entrer en mode test ? (y/n) : ")
while CLI != "n":
  CLI = input("Entrez votre code : ")
  if CLI == "exit":
    break
  else :
    exec(CLI)
