Here’s your English version with the emojis preserved:

---

````markdown
# 🔄 Switch Image Update via Console Server

This script uses the **`pexpect`** library to connect to a **console server** and perform a **switch firmware update** via an **HTTP server**.  
All output is displayed live in the terminal using the **`logging`** module.  

---

## ✨ Features
- 🔌 **Automatic connection** to the console server via SSH  
- 🖥 **Access serial port** and authenticate to the switch  
- 🚀 Execute the `update image` command via HTTP  
- 👀 **Live output** in the terminal  
- 🛡 **Error handling** with `try/except/finally`  

---

## 📦 Requirements
- 🐍 **Python 3.6+**
- 📚 Install required libraries:
  ```bash
  pip install pexpect
````

* 🌐 Access to:

  * Console server (IP and username/password)
  * Switch login credentials
  * HTTP server hosting the firmware image
  * Switch management IP and default gateway

---

## ⚙ Default Configuration in Code

```python
console_ip = "192.168.30.20"
console_pass = "123"
switch_user = "admin"
switch_pass = "zharfpouyan"
webserver_ip = "192.168.0.19"
default_gw = "192.168.30.2"
```

> 📝 **Note:** Adjust these values according to your network environment.

---

## ▶ How to Run

1. 💾 Save the script to a file, for example:

   ```bash
   nano update_switch.py
   ```

2. ▶ Run it:

   ```bash
   python update_switch.py
   ```

3. ⌨ During execution, you will be prompted to enter:

   * **Console server username** 🧑‍💻
   * **Image filename** 📂 (the file on the HTTP server)
   * **Management IP with subnet** 🌐 (e.g. `192.168.30.34/24`)

4. 🛠 The script will automatically connect to the console server and perform the update.

---

## 📜 Output

* 📡 All messages and switch responses will be shown live in the terminal.
* ⚠ Any errors will be clearly logged.

---

## ⚠ Important Notes

* Before running, make sure the **console server is connected to the switch’s serial port**.
* The **firmware file** must be placed on the **HTTP server** and be accessible via the configured IP.
* The update timeout is set to **10 minutes** ⏳ (`timeout=600`).

---

## 📄 License

This script is **free** for internal use.
For critical environments, test it first in a lab 🧪.

```