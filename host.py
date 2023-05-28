import socket

print("Programme Host\n")

separation_embed = "==========================================="

def game():
    global host_socket, new_sokcet

    print(separation_embed)

    print("\nLe client est en train de choisir son élément...")
    client_choice = new_sokcet.recv(1024).decode('utf-8')
    print("Le client à choisit!")

    print("""\nSélectionnez maintenant votre signe.
    [1] Pierre
    [2] Papier
    [3] Ciseaux
Entrez le nombre du signe que vous voulez choisir:""", end=" ")
    choice = int(input())
    if choice == 1:
        host_choice = "pierre"
    elif choice == 2:
        host_choice = "papier"
    elif choice == 3:
        host_choice = "ciseaux"

    if (host_choice == "pierre" and client_choice == "ciseaux") or (host_choice == "papier" and client_choice == "pierre") or (host_choice == "ciseaux" and client_choice == "papier"):
        print("\nVous avez gagné!\n")
        endgame_status = "lose"
        to_client_endgame_msg = "\nVous avez perdu...\n"
        new_sokcet.send(endgame_status.encode('utf-8'))
        new_sokcet.send(to_client_endgame_msg.encode('utf-8'))
    elif (host_choice == "pierre" and client_choice == "pierre") or (host_choice == "papier" and client_choice == "papier") or (host_choice == "ciseaux" and client_choice == "ciseaux"):
        endgame_status = "equal"
        to_client_endgame_msg = "\nIl y a égalité... Recommencez!\n"
        new_sokcet.send(endgame_status.encode('utf-8'))
        new_sokcet.send(to_client_endgame_msg.encode('utf-8'))
        print("\nIl y a égalité... Recommencez!\n")
        game()
    else:
        endgame_status = "win"
        to_client_endgame_msg = "\nVous avez gagné!\n"
        new_sokcet.send(endgame_status.encode('utf-8'))
        new_sokcet.send(to_client_endgame_msg.encode('utf-8'))
        print("\nVous avez perdu...\n")
    
    print("Voulez vous relancer une nouvelle partie (Y/N):", end=" ")
    new_game = input()
    if new_game == "Y":
        print("Très bien, nouvelle partie!\n")
        new_sokcet.send(new_game.encode('utf-8'))
        game()
    elif new_game == "N":
        print("Très bien, déconnexion du socket en cours...\n")
        new_sokcet.send(new_game.encode('utf-8'))
        decon_socket()
        exit()

def con_socket():
    global host_socket, new_sokcet

    host_ip = socket.gethostbyname(socket.gethostname())
    port = 3600
    print(f"L'adresse IP du serveur (cette machine) est: {host_ip}\nLe port est: {port}")

    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_socket.bind(("", port))
    host_socket.listen()
    print("En attente de connection...\n")
    new_sokcet, client_ip = host_socket.accept()
    print(f"La connection est établie avec: {client_ip}\n")

def decon_socket():
    global host_socket, new_sokcet 
    new_sokcet.close()
    host_socket.close()

con_socket()
game()