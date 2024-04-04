import subprocess

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Run Network Scanner")
        print("2. Run Vulnerability Scanner")
        print("3. Run Port Scanner")
        print("4. Run System Monitoring")
        print("5. Run Networkinfo")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            Network_Scan()
        elif choice == '2':
            Vuln_scan()
        elif choice == '3':
            Port_scan()
        elif choice == '4':
            Monitoring()
        elif choice == '5':
            Networkinfo()
        elif choice == '6':
            print("Exiting the program. Goodbye!")

            break
        else:
            print("Invalid choice. Please try again.")

def Network_Scan():
    try:
        print("Calling networkscanner.py...")
        subprocess.run(["python", "networkscanner.py"])
    except FileNotFoundError:
        print("Error: networkscanner.py not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def Vuln_scan():
    try:
        print("Calling tryvs.py...")
        subprocess.run(["python", "tryvs.py"])
    except FileNotFoundError:
        print("Error: tryvs.py not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def Port_scan():
    try:
        print("Calling tryps.py...")
        subprocess.run(["python", "tryps.py"])
    except FileNotFoundError:
        print("Error: tryvs.py not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def Monitoring():
    try:
        print("Calling Monitoring.py...")
        subprocess.run(["python", "Monitoring.py"])
    except FileNotFoundError:
        print("Error: Monitoring.py.py not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def Networkinfo():
    try:
        print("Calling Networkinfo.py...")
        subprocess.run(["python", "Networkinfo.py"])
    except FileNotFoundError:
        print("Error: Networkinfo.py not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main_menu()
