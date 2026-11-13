import socket
import logging
import argparse


logging.basicConfig(
    filename="intrusion.log",
    level=logging.INFO,
    format="%(asctime)s - [ALERT] - %(message)s"
)

def start_honepot(port: int, bind_ip: str = "0.0.0.0"):
    """Deploys a fake vulnerable server to captur attacker data."""
    print(f"---Deploying Honeypot on {bind_ip}:{port} ---")
    print("Listening for incoming connections... (Press Ctrl+C to stop)")
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            server_sock.bind((bind_ip, port))
            
            server_sock.listen(5)
            
            while True:
                client_socket, client_address = server_sock.accept()
                attacker_ip, attacker_port = client_address
                
                print(f"\n[!] INTRUSION ATTEMPT DETECTED from {attacker_ip}:{attacker_port}")
                logging.info(f"Intrusion attempt from IP: {attacker_ip} | Source Port: {attacker_port}")
                
                try: 
                    fake_banner = b"Ubuntu 20.04 LTS (Fake Secure Shell)\nLogin"
                    client_socket.send(fake_banner)
                    
                    data = client_socket.recv(1024)
                    if data: 
                        payload = data.decode('utf-8', errors='ignore').strip()
                        print(f"    [+] Payload captured: {payload}")
                        logging.info(f"Payload captured from {attacker_ip}: {payload}")
                        
                except Exception:
                    pass
                
                finally:
                    client_socket.close()
            
    except KeyboardInterrupt:
        print("\n--- Honeypot deactivated by user ---")
    except Exception as e:
        print(f"[-] Server Error: {e}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Low-Interaction Network Honeypot")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port to deploy honeypot on (default: 8080)")
    args = parser.parse_args()
    
    start_honepot(args.port)