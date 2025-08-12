import pexpect
import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# -------- Get user input --------
console_ip = "192.168.30.20"
console_pass = "123"
switch_user = "admin"
switch_pass = "zharfpouyan"
webserver_ip = "192.168.0.19"
default_gw = "192.168.30.2"

console_user = input(" Console server username: ")
image_file = input(" Image filename : ")
mgmt_ip = input(" Management IP with subnet (e.g. 192.168.30.34/24): ")

child = None

try:
    logging.info("🔌 Connecting to console server...")
    child = pexpect.spawn(f"ssh {console_user}@{console_ip}", timeout=30, encoding='utf-8')

    child.expect("password:")
    child.sendline(console_pass)

    # Select serial port (default: 1)
    child.expect(r"#\?")
    child.sendline("1")

    # Send ENTERs to trigger login prompt
    child.sendline("")
    child.sendline("")

    # Try to detect switch state
    index = child.expect([
        "login:",
        "Password:",
        "#",  # already in CLI
    ], timeout=10)

    if index == 0:
        child.sendline(switch_user)
        child.expect("Password:")
        child.sendline(switch_pass)
    elif index == 1:
        child.sendline(switch_pass)
    else:
        logging.info(" Already inside switch CLI.")

    # Enter enable and config mode
    child.expect(".*#")
    child.sendline("enable")
    child.expect(".*#")
    child.sendline("configure terminal")
    child.expect(".*\\(config\\)#")

    # Build and send update command
    update_cmd = f"update image http {webserver_ip} {image_file} {mgmt_ip} {default_gw}"
    logging.info(f" Sending update command: {update_cmd}")
    child.sendline(update_cmd)

    # Confirm update
    child.expect("Are you sure to update device\\?\\(yes/no\\)")
    child.sendline("yes")

    # Respond to config/restore question
    child.expect("Would you like to restore config and storage after update image\\?\\(yes/no\\)")
    child.sendline("no")

    logging.info(" Updating... Please wait.")

    child.logfile = sys.stdout

    # Wait for update to complete
    index = child.expect([
        "Update completed",
        pexpect.TIMEOUT,
        pexpect.EOF
    ], timeout=600)

    if index == 0:
        logging.info(" Update completed successfully.")
    else:
        logging.error(" Error or timeout during update.")

except pexpect.exceptions.TIMEOUT:
    logging.error(" Timeout occurred during communication. Please check the device or network.")
except pexpect.exceptions.EOF:
    logging.error(" Connection was closed unexpectedly.")
except Exception as e:
    logging.exception(f" Unexpected error: {e}")
finally:
    if child is not None:
        try:
            child.close()
        except Exception as e:
            logging.warning(f" Failed to close child session cleanly: {e}")
