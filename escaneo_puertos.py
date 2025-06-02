import socket

def escanear_puertos(ip, puerto_inicio, puerto_fin):
    print(f"Escaneando puertos en {ip} del {puerto_inicio} al {puerto_fin}...\n")
    puertos_abiertos = []

    for puerto in range(puerto_inicio, puerto_fin + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Tiempo de espera para no tardar mucho
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            puertos_abiertos.append(puerto)
            print(f"Puerto {puerto} abierto")
        sock.close()

    if not puertos_abiertos:
        print("No se encontraron puertos abiertos en ese rango.")

if __name__ == "__main__":
    objetivo = input("Introduce la IP o dominio a escanear: ")
    inicio = int(input("Puerto inicial: "))
    fin = int(input("Puerto final: "))
    escanear_puertos(objetivo, inicio, fin)
