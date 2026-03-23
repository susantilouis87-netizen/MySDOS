
import socket 
import subprocess
import platform
import os
import shutil
import math
import time
import json
import sys
import http.client
from urllib.parse import urlparse
print("""
   __  ____     __
  /  |/  /\ \   / /
 / /|_/ /  \ \_/ / 
/ /  / /    \   /  
/_/  /_/     /_/   
                   
""") 
print("=== MySDOS ===")
print("By Louis") 
print("Type 'dir' or 'help' to see all of the available commands") 
version = "MySDOS Programming Language, Version 2.40 Extended LTS Original Programming Language Built on Python\n"
folders_dict = {
    "files": ["sdos.exe", "simple.sd", "run.ini"],
    "temp_files": ["important.txt", "win.bt","matomatika.docx"]
}
commands = ["say", "add", "sub", "dir", "exit", "file", "del", "move","perm","grant","ver","open","exp","div","multi","loop","solve","regadd","regcheck","net","color","ls","cd","rename","clear","os","stat","mem","info","sqrt","!","time","json","edit","server","ping","fib","tree","gui","whoami","compare","textclassfi","bot","reverse","ps","train","addstring","len","kernel","env","getcwd","getpid","getuid","listdir", "getgid","pi","e","log","sin","cos","tan","circle","system","python","proc","priority","byteorder","recursive","size","url"]
perm_files = ["RX, R"]
perm_temp_files = ["RX, R"]
sdos_exe = "RUN sdos.exe from run.ini"
run_ini = "MOV A, 5      ; let A = 5MOV B, 10     ; let B = 10ADD A, B      ; A = A + B PRINT A       ; output: 15"
simple_sd = "print hello, del h.exe, perm, ver, exit"
important_txt = "Proyek ini diberhakkan atas nama 7.2 sebagai pembuatan bahasa pemrograman simpel untuk SMP Santo Tarsisius kami berhak dan mendapatkan layaknya gak mengembangkan projek ini lebih lanjut itu aja dari saya ©2026 SDOS | Skeleton"
win_bt = """@echo off
REM Mini SDOS Batch Script
echo Running SDOS Boot Tasks...
echo Loading important files...
open run.ini
open sdos.exe
echo System Ready!"""
# Kode ANSI
colors = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37"
}
current_color = "37"  # default putih
files = folders_dict["files"]
temp_files = folders_dict["temp_files"]
current_dir = "files"  # default folder
directories = "files", "Temporary Files"
khHKEYLCLSYSTEM = ["0x011110", "0xc00008", "0x67000"]
whoami = ["U", "A", "O"]
current_whoami = "U"
texts = ["I love you", "I'm fine", "I hate you"]
labels = ["Baik", "Netral", "Buruk"]
user_name = "Louis Gavriel Hadison"
current_time = time.localtime() 

while True:
    line = input("S:/> ").strip() # Ambil input asli (biar besar/kecil terjaga)
    if not line: continue
    
    parts = line.split()
    cmd = parts[0].lower() # Cuma perintahnya yang dipaksa huruf kecil
    args = parts[1:]       # Argumen (nama file, pesan, dll) tetap asli
    
    if cmd == "exit":
        print("Pepatah mengatakan tak kenal, maka tak tau") 
        break



    if cmd == "say":
        print(" ".join(args))
  
    elif cmd == "add":
          try:
             print(int(args[0]) + int(args[1]))
          except:
              print("Error: add needs 2 numbers") 
        
 
    elif cmd == "sub":
        try:
            print(int(args[0]) - int(args[1]))
        except:
            print("Error: sub needs 2 numbers")

    elif cmd in ["dir","help"]:
        print("Available commands:", ", ".join(commands))
  
    elif cmd == "file":
        print(f"Available", folders_dict)
  
    elif cmd == "del":
        print("Available Files:")
        for i, f in enumerate(folders_dict[current_dir]):
            print(f"{i+1}. {f}")
        try:
            delete = int(input("Choose file number to delete: "))
            if 1 <= delete <= len(files):
                removed = files.pop(delete-1)
                print(f"{removed} deleted")
            else:
                print("Invalid number!")
        except:
            print("Invalid input!")
 
    elif cmd == "move":     
        try:
            print("Available Folders") 
            print(f"{directories}") 
            origin = input("Which One do you want to move: ").lower() 
            name_file = input("Name: ").lower() 
            
            if origin.lower() == "temporary files" or origin == "temporary files":
                temp_files.remove(name_file) 
                files.append(name_file) 
                print(f"{name_file} telah dipindahkan dari {origin} ke files") 
            if origin.lower() == "files" or origin == "Files":
                files.remove(name_file) 
                temp_files.append(name_file)
                print(f"{name_file} telah dipindahkan dari {origin} ke temp_files") 
        except ValueError:
            print("File does not exist")        
   
    elif cmd == "perm":
        print(f"Permissions for {folders_dict}") 
        print(f"Permissions for Files: {perm_files}") 
        print(f"Permissions for Temporary Files: {perm_temp_files}")    

    elif cmd == "grant":
       grant_access = input("Grant Access for:  ") 
       if grant_access == "temp_files" or grant_access == "Temp_files":
           perm_temp_files.append("FO") 
           print("Full Ownership granted to temp_files") 
       if grant_access == "Files" or grant_access == "files":
           perm_files.append("FO") 
           print("Full Ownership granted to files") 

    elif cmd == "ver":
        print(f"{version}")
 
    elif cmd == "open":
       open_files = input("Which files do you want to Open? :").lower() 
       if open_files.lower() == "sdos.exe":
           print("Opening") 
           print(f"{sdos_exe}") 
       if open_files.lower() == "run.ini":
           print("Opening") 
           print(f"{run_ini}") 
       if open_files.lower() == "important.txt":
           print("Opening") 
           print(f"{important_txt}")      
       if open_files.lower() == "simple.sd":
           print("Opening") 
           print(f"{simple_sd}") 
       if open_files.lower() == "win.bt":
           print("Opening") 
           print(f"{win_bt}")      

    elif cmd == "exp":
        try:
            base = int(args[0])      # angka dasar
            power = int(args[1])     # pangkat
            result = base ** power
            print(result)
        except:
            print("Error: exp needs 2 numbers (base power)")
  
    elif cmd == "div":
        try:
            divident = int(args[0]) 
            divisor = int(args[1]) 
            result = divident / divisor
            print(result) 
        except: 
            print("Error: div needs 2 numbers (divident divisor)")
 
    elif cmd == "multi":
        try:
            add = int(args[0])
            sub = int(args[1])
            times = int(args[2])
            divide = int(args[3]) 
            result = add - sub * times / divide
            print(result) 
        except:
            print("Not Enough numbers to count")
 
    elif cmd == "loop":
        try:
            word = args[0]
            count = int(args[1])
            for w in range(count):
                print(word) 
        except:
            print("No words in word or string in count") 
   
    elif cmd == "solve":
        try:
            # Format: solve a b c (ax + b = c)
            a = int(args[0])
            b = int(args[1])
            c = int(args[2])
            x = (c - b) / a
            print(f"Jika {a}x + {b} = {c}, maka x = {x}")
        except ZeroDivisionError:
             print("Error: 'a' tidak boleh 0")
        except:
            print("Gunakan format: solve [a] [b] [c]")
 
    elif cmd in ["regadd","ra"]:
        try:
            value = (args[0]) 
            khHKEYLCLSYSTEM.append(value) 
        except IndexError:
            print("Wrong Value") 
  
    elif cmd in ["regcheck","rc"]:
        print("Current Registry Settings") 
        print(khHKEYLCLSYSTEM)     
 
    elif cmd == "net":
        system = platform.system()
        if system == "Windows":
            cmd_str = "ipconfig"
        else:
        # Android biasanya Linux-based
            cmd_str = "ifconfig"  # atau "ip addr" kalau ifconfig ga ada
            subprocess.call(cmd_str, shell=True)  # langsung tampil di layar
    
    elif cmd in ["color","col"]:
        if args and args[0].lower() in colors:
            color_name = args[0].lower()
            current_color = colors[color_name]
            print(f"\033[{current_color}mColor changed to {color_name}\033[0m")
        else:
            print(f"\033[31mUsage: color <valid color>\033[0m")
 
    elif cmd == "ls":
    # List isi folder saat ini
        print(f"Contents of {current_dir}:")
        for item in folders_dict.get(current_dir, []):
            print(f"- {item}")
 
    elif cmd == "cd":
        if args:
            target = args[0]
        if target in folders_dict:
            current_dir = target
            print(f"Changed directory to {current_dir}")
        else:
            print(f"Directory not found: {target}")
 
    elif cmd == "rename":
        if len(args) < 2:
            print("Usage: rename <old_name> <new_name>")
        else:
            old_name = args[0]
            new_name = args[1]
        
        # Cari folder yang mengandung file
        found = False
        for folder, file_list in folders_dict.items():
            if old_name in file_list:
                # hapus file lama dan tambahkan file baru
                file_list.remove(old_name)
                file_list.append(new_name)
                print(f"✅ '{old_name}' berhasil diganti menjadi '{new_name}' di folder '{folder}'")
                found = True
                break
        
        if not found:
            print(f"❌ File '{old_name}' tidak ditemukan di folder manapun")
  
    elif cmd in ["clear","clr"]:
        os.system('clear') 

    elif cmd == "os":
        print("Environment That You're using is:") 
        print(os.name + "," + " " + sys.platform) 
 
    elif cmd == "stat":
        if len(args) < 1:
            print("Usage: stat <filename>")
        else:
            path = args[0]  # ambil yang pertama aja
            try:
                info = os.stat(path)
                print(info)
            except FileNotFoundError:
                raise FileNotFoundError(f"ERROR 142: NOT FOUND SYSTEM FILE if you are seeing this message call your system administrator now! {info}") 
  
    elif cmd == "mem":
        total, used, free = shutil.disk_usage("/")

        print(f"Total Storage: {total / (1024**3):.2f} GB")
        print(f"Used Storage: {used / (1024**3):.2f} GB")
        print(f"Free Storage: {free / (1024**3):.2f} GB")

        # Cek RAM (Android spesial)
        try:
            with open("/proc/meminfo") as f:
                meminfo = f.readlines()
                mem_total = int(meminfo[0].split()[1]) / 1024  # kB -> MB
                mem_free = int(meminfo[1].split()[1]) / 1024
                print(f"Total RAM: {mem_total:.2f} MB")
                print(f"Free RAM: {mem_free:.2f} MB")
        except:
            print("Failed To Read RAM")
 
    elif cmd == "info":
        print("=== CPU INFO ===")
        try:
            print(f"Arsitektur: {platform.machine()}")
            print(f"Prosesor: {platform.processor()}")
            print(f"Jumlah Core (Logis): {os.cpu_count()}")
        except:
            print("Failed To Read!") 
    
    elif cmd == "sqrt":
        number = int(args[0]) 
        res = math.sqrt(number) 
        print(res) 

    elif cmd == "!":
        n = int(args[0]) 
        re = math.factorial(n) 
        print(re) 
 
    elif cmd == "time":
        now = time.localtime()
        print(f"Sekarang: {now.tm_hour}:{now.tm_min}:{now.tm_sec}") 
 
    elif cmd == "json":
          hp_data = {
                "RAM: 8 GB",
                "Storage: 256 GB",
                "CPU: Snapdragon 7s Gen3",
                "Score : 100"
                }

          with open("hp_test.json", "w") as f:
                json.dump(hp_data, f, indent=4)

                print("Data HP tersimpan di hp_test.json") 

    elif cmd in ["regdel","rd"]:
        try:
            print("Available Registries") 
            print(khHKEYLCLSYSTEM) 
            val = (args[0]) 
            khHKEYLCLSYSTEM.remove(val) 
        except IndexError:
            print("No Value")  
        except ValueError:
            print("Value already deleted")      
 
    elif cmd == "edit":
        file_to_edit = input("Which file do you want to edit?: ").strip()
    
    # Cek folder file
        if file_to_edit in folders_dict["files"]:
            current_perm = perm_files
        elif file_to_edit in folders_dict["temp_files"]:
            current_perm = perm_temp_files
        else:
            print(f"❌ File '{file_to_edit}' tidak ditemukan!")
            continue

    # Cek izin edit
        if "W" not in current_perm and "FO" not in current_perm:
            print(f"❌ You cannot edit {file_to_edit} (Read-only)")
        else:
            new_content = input(f"Type new content for {file_to_edit}: ")
            file_to_edit = new_content  
            print(f"✅ {file_to_edit} updated to: {new_content}")  
  
    elif cmd == "server":
       # 1. Buat socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. Bind ke localhost dan port 12345
        s.bind(('127.0.0.1', 12345))

        # 3. Dengarkan koneksi
        s.listen(1)
        print("Server siap, menunggu client...")

        # 4. Terima koneksi
        conn, addr = s.accept()
        print("Terhubung dengan:", addr)

        # 5. Terima data dari client
        data = conn.recv(1024)  # maksimal 1024 byte
        print("Client bilang:", data.decode())

        # 6. Kirim balasan
        conn.send(b"Server: Pesan diterima!")

        # 7. Tutup koneksi
        conn.close()
        s.close()
  
    elif cmd in ["ping","p!"]:
        host = input("Enter host to ping: ")  # misal 8.8.8.8 atau google.com
        os.system(f"ping -c 4 {host}")  # Linux / macOS
    
    elif cmd == "fib":
        n = int(input("Masukkan jumlah angka Fibonacci: "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
            print()  # Pindah baris setelah selesai
 
    elif cmd == "tree":
        def tree_dict(d):
            for i, (folder, files) in enumerate(d.items()):
                connector = "└── " if i == len(d)-1 else "├── "
                print(connector + folder)
            for j, file in enumerate(files):
                file_connector = "    └── " if j == len(files)-1 else "    ├── "
                print(file_connector + file)
        tree_dict(folders_dict)    
 
    elif cmd == "gui":
        while True:
            os.system('clear') # Bersihkan layar
            print("┌──────────────────────────────────────────┐")
            print("│             MySDOS v2.25 GUI             │")
            print("├──────────────────────────────────────────┤")
            print(f"│ User: {user_name} | Time: {current_time}  │")
            print("│ RAM Usage: [██████░░░░] 60%              │")
            print("├──────────────────────────────────────────┤")
            print("│ > Ketik 'exit' untuk kembali ke CLI      │")
            print("└──────────────────────────────────────────┘")
        
            op = input("Choice: ")
            if op == "exit": break

    elif cmd in ["whoami","who"]:
        print(current_whoami) 
        
    elif cmd == "compare":
        will_compare_to = int(args[0]) 
        comparator = int(args[1]) 
        
        if will_compare_to > comparator:
            print(f"{will_compare_to} is more than {comparator}") 
        else:
            print(f"{will_compare_to} is less than {comparator}") 
    
    elif cmd in ["textclassfi","tc"]:
        # 1️⃣ Buat kamus kata per label
        word_counts = {}
        for text, label in zip(texts, labels):
            words = text.lower().split()  # ubah jadi huruf kecil & pisah kata
            if label not in word_counts:
                word_counts[label] = {}
                for word in words:
                    if word not in word_counts[label]:
                        word_counts[label][word] = 0
                        word_counts[label][word] += 1

        # 2️⃣ Fungsi prediksi sederhana
        def predict(text):
            words = text.lower().split()
            scores = {}
            for label in word_counts:
                scores[label] = 0
                for word in words:
                    if word in word_counts[label]:
                        scores[label] += word_counts[label][word]
        # Pilih label dengan skor tertinggi
                        return max(scores, key=scores.get)

        # 3️⃣ Coba prediksi
        test_texts = ["I love coding", "I feel bad", "I am okay"]
        for t in test_texts:
            print(f"{t} → {predict(t)}")
            
    elif cmd == "bot":
        
        print("=== AI Chat Mode ===")
        print("Ketik 'stop' untuk keluar dari AI chat\n")
    
        # 1. Inisialisasi Data (Tetap di luar loop biar efisien)
        
        word_counts = {}
        for text, label in zip(texts, labels):
            words = text.lower().split()
            if label not in word_counts: word_counts[label] = {}
            for word in words:
                word_counts[label][word] = word_counts[label].get(word, 0) + 1

        def classify(text):
            words = text.lower().split()
            scores = {label: 0 for label in word_counts}
            for label in word_counts:
                for word in words:
                    if word in word_counts[label]:
                        scores[label] += word_counts[label][word]
            return max(scores, key=scores.get)

        # 2. Loop Utama Chat (Semua logika harus di DALAM sini)
        while True:
            user_input = input("Kamu: ").strip()
            if not user_input:
                continue

            if user_input.lower() == "stop":
                print("AI: Keluar dari AI Chat Mode... Bye! 👋")
                break
        
            # --- LOGIKA RESPONS (Sekarang sudah di dalam While) ---
            
            # A. Cek Matematika
            math_response = None
            try:
                # Kita batasi eval agar aman
                math_result = eval(user_input, {"__builtins__": None}, {})
                if isinstance(math_result, (int, float)):
                    math_response = f"AI: Hasilnya adalah {math_result} ✅"
            except:
                math_response = None
        
            # B. Cek Sapaan
            text_lower = user_input.lower()
            greeting_response = None
            if any(word in text_lower for word in ["hello", "hi", "halo"]):
                greeting_response = "AI: Halo! Senang bertemu kamu 🌟"
            
            # C. Gunakan Classifier jika A & B tidak terpenuhi
            class_response = ""
            if not math_response and not greeting_response:
                label = classify(user_input)
                if label == "Baik":
                    class_response = "AI: Wah, itu terdengar positif! 😄"
                elif label == "Netral":
                    class_response = "AI: Hmmm, aku mengerti 😐"
                else:
                    class_response = "AI: Oh, kenapa bisa begitu? 😢"
            
            # D. EKSEKUSI PRINT (Harus sejajar di dalam While)
            if math_response:
                print(math_response)
            elif greeting_response:
                print(greeting_response)
            else:
                print(class_response) 

    elif cmd in ["reverse","rev"]:
        text = args[0]
        print(text[::-1]) 
        
    elif cmd == "ps" and args == ["-aux"]:
             print(f"{'USER':<8} {'PID':<6} {'%CPU':<5} {'%MEM':<5} {'COMMAND'}")
             print("-" * 45)
        # Kita buat simulasi proses yang seolah-olah lagi jalan
             processes = [
            [current_whoami, "1", "0.1", "0.5", "sdos.exe"],
            [current_whoami, "42", "12.5", "8.0", "python3 mysdos.py"],
            ["root", "102", "0.0", "1.2", "/system/bin/surfaceflinger"],
            [current_whoami, "554", "25.0", "15.2", "gui_engine.bin"],
            ["kernel", "2", "0.0", "0.0", "[kthreadd]"]
        ]
        
             for p in processes:
               print(f"{p[0]:<8} {p[1]:<6} {p[2]:<5} {p[3]:<5} {p[4]}")
  
    elif cmd == "train":
        print("=== AI Trainer Mode ===")
        # 1. Ambil Input dari User
        new_text = input("Masukkan kalimat baru: ").lower()
        print("Pilih Label: 1. Baik, 2. Netral, 3. Buruk")
        choice = input("Pilihan (1/2/3): ")

        # 2. Tentukan Label berdasarkan pilihan
        label_map = {"1": "Baik", "2": "Netral", "3": "Buruk"}
        target_label = label_map.get(choice)

        if target_label:
            # 3. Masukkan ke Dataset MySDOS
            texts.append(new_text)
            labels.append(target_label)
            print(f"✅ Berhasil! AI sekarang tahu kalau '{new_text}' itu {target_label}.")
        else:
            print("❌ Pilihan tidak valid!")
 
    elif cmd in ["addstring", "as"]:
        try:
            # Menggabungkan semua argumen yang ada di dalam list args
            result = "".join(args) 
        
            if not result: # Jika user cuma ketik 'as' tanpa kata
                raise IndexError
            print(result)
 
        except IndexError:
            print("Error: Kasih kata dong, Louis!")

    elif cmd == "len":
        try:
            # Kita hitung panjang dari semua argumen yang digabung
            gabung = "".join(args)
            print(len(gabung))
        except Exception:
            print("Error: Expected Words to count")
     
    elif cmd == "kernel":
        print("Platform Kernel Version (based on import platform)") 
        print(platform.version()) 
        print(platform.system() + " " + platform.release()) 
        print("Full Data") 
        print(platform.platform()) 
        print(os.uname()) 
        
    elif cmd in ["env", "environment"]:
        print(os.environ) 
    
    elif cmd == "getcwd":
        print(os.getcwd()) 
        
    elif cmd in ["getpid", "curpid", "pid"]:
        print(os.getpid()) 
        
    elif cmd in ["getuid", "curuid", "uid"]:
        print(os.getuid()) 
     
    elif cmd == "listdir":
        print(os.listdir()) 
        
    elif cmd in ["getgid", "gid", "curgid", "group"]:
        print(os.getgid()) 
        
    elif cmd in ["π", "pi"]:
        print(math.pi) 
        
    elif cmd == "e":
        print(math.e) 
        
    elif cmd in ["log","ln"]:
        value1 = int(args[0]) 
        value2 = int(args[1]) 
        print(math.log(value1, value2)) 
    
    elif cmd in ["sin","s"]:
        try: 
            x = int(args[0]) 
            print(math.sin(math.radians(x))) 
        except:
            print("Value needed!") 
 
    elif cmd in ["cos","c"]:
        try:  
           c = int(args[0]) 
           print(math.cos(math.radians(c))) # Output: 1.0 (sin 90 derajat)
        except:  
           print("Value needed!") 
           

    elif cmd in ["tan","t"]:
        try:
           t = int(args[0]) 
           print(math.tan(math.radians(t))) 
        except:
           print("Value needed!") 
           
    elif cmd in ["circle", "circ"]:
      try: 
         r = int(args[0]) 
         luas = math.pi * math.pow(r, 2) 
         print(f"Luas lingkaran dengan jari-jari {r} adalah: {luas:.2f}") 
      except:
          print("Value needed!") 
          
    elif cmd in ["system", "sys"]:
        print(platform.machine()) 
        print(platform.processor()) 
        print(platform.architecture()) 
    
    elif cmd in ["python", "py"]:
        print(platform.python_version()) 
        print(platform.python_compiler()) 
   
    elif cmd == "proc":
        print(os.times()) 
        
    elif cmd in ["priority","prio"]:
        print(os.getpriority(os.PRIO_USER, 0)) 
     
    elif cmd in ["byteorder", "byte","order","bo","byteord"]:
        print(sys.byteorder) 
        
    elif cmd == "recursive":
        print(sys.getrecursionlimit())  
      
    elif cmd == "size":
     try:
        word = args[0]
        print(sys.getsizeof(word)) 
        print(sys.getsizeof(commands)) 
     except:
         print("Needed Word!") 
         
    elif cmd == "url":
        # 1. Taruh fungsi di paling atas setelah elif
        def handle_curl(u):
            try:
                from urllib.parse import urlparse
                import http.client
                parsed = urlparse(u)
                host = parsed.netloc
                path = parsed.path if parsed.path else "/"
                print(f"Connecting to {host}...")
                conn = http.client.HTTPConnection(host, timeout=5)
                conn.request("GET", path)
                res = conn.getresponse()
                print(f"Status: {res.status} {res.reason}")
                conn.close()
            except Exception as e:
                print(f"Error: {e}")

        # 2. Sekarang IF dan ELSE jadi berdekatan, lebih gampang diluruskan!
        if len(args) > 0:
            url_target = args[0]
            if not url_target.startswith("https"):
                url_target = "https://" + url_target
                handle_curl(url_target)
        else:
            # Luruskan ELSE ini tepat di bawah huruf 'i' pada 'if' di atasnya
            print("Usage: url <address>")
        
    else:
       print(f"Unknown command: {cmd}") 
       
       
       