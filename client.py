import socket

print("Programme Client\n")

separation_embed = "==========================================="

def game():
    global client_socket

    print(separation_embed)

    print("""\nSélectionnez maintenant votre signe.
    [1] Pierre
    [2] Papier
    [3] Ciseaux
Entrez le nombre du signe que vous voulez choisir:""", end=" ")
    
    choice = int(input())
    if choice == 1:
        choice_message = "pierre"
    elif choice == 2:
        choice_message = "papier"
    elif choice == 3:
        choice_message = "ciseaux"
    
    client_socket.send(choice_message.encode('utf-8'))

    print("\nLe seveur est en train de choisir son élément...")
    endgame_status = client_socket.recv(1024).decode('utf-8')
    endgame_msg = client_socket.recv(1024).decode('utf-8')
    if endgame_status == "equal":
        game()
    print(endgame_msg)

    print("Le serveur choisit si il veut relancer une partie...")
    new_game = client_socket.recv(1024).decode('utf-8')
    if new_game == "Y":
        print("Le serveur à lancer une nouvelle partie!\n")
        game()
    elif new_game == "N":
        print("Le serveur n'a pas relancé de nouvelle partie, déconnexion du socket en cours...\n")
        decon_socket()
        exit()

def con_socket():
    global client_socket

    print("Veuillez entrer l'adresse IP su serveur:", end=" ")
    host_ip = input()
    print("Veuillez saisir le port:", end=" ")
    port = int(input())

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_ip, port))
    print("\nLa connection est établie!\n")

def decon_socket():
    global client_socket
    client_socket.close()

con_socket()
game()