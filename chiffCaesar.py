#Demandons à l'utilisateur de rentrer le message à entrer et une clé

msg_a_coder = input("Veuillez entrer le texte que vous voulez crypter : ")
clef = int(input("Ecrivez une clé (un chiffre de préférence) : "))

###########Chiffrement du message entré en utilisant la clé entrée

# Décalage des codes ASCII des caractères
msg = [(ord(i)-clef) for i in msg_a_coder]

# Conversion des codes ASCII décalés en caractères
msg_decode = [chr(i) for i in msg]

# Joindre les caractères pour former le message final
final = "".join(msg_decode)

#Affichage du message crypté
print(final)