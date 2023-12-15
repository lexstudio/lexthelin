import os
import time
while True:
    command = input("> ")

    if command == "set mvap >True":
        print()

    elif command == "conf":
        os.system("nvim config.py")

    elif command == "clear":
        os.system("clear")
    
    elif command == "net -n 'alex 5' -p patra321":
        print("searching")
        time.sleep(0.4)
        print("found")
        print("connecting ...")
        time.sleep(1)
        print("connected")

    elif command == "mods --install plugin.lore":
        print("plugin.lore is installing")
        time.sleep(3)
        print("lore looks good :)")

    elif command == "lore-plug start system":
        print("lore start")

    elif command == "lsb":
        print("sda")

    elif command == "lore auto -configuration sda":
        print("sda")
        print("--sda1")
        print("--sda2")
        print("--sda3")

    elif command == "net catch https://lexpkg/lunx-3232":
        print("wait")
        while True:
            command = input("network::https://lexpkg/lunx-3232--> ")

            if command == "lunx -i minkernel":
                print("catching ...")
                time.sleep(4)
                print("minkernel is redy")

            elif command == "exit":
                break

            
    elif command == "set minkernel -f start":
        print("minkernel is running")

    elif command == "minkernel -all make superusr/rooter/admin/netadmin":
        print("mikernel is superusr/rooter/admin/netadmin")

    elif command == "set boot for boot-all":
        print("ok :)")
    
    elif command == "set usr alex":
        print("ok :)")

    elif command == "set password sun12 usr alex":
        print("ok :)")

    elif command == "set lunx net-catch-install":
        print("ok :)")
        
    elif command == "net set lunx 3333":
        print("lunx is net port 3333")
        print("all is ok :)")

    elif command == "set lunx pkg":
        print("ok :)")

    elif command == "mods --install plugin.https":
        print("https is installing")
        time.sleep(7)
        print("https looks good :)")

    elif command == "https set lunx":
        print("https set lunx")

    elif command == "lunx":
        print("lunx-3232--")

    elif command == "l":
        os.system("ls")

    elif command == "lunx -all pkg":
        print("lunx is all pkg")

    elif command == "lunx -update":
        print("updating lunx from port 3333 in https://lunx-3333/update")
        time.sleep(4)
        print("")
        print("")


    elif command == "lunx -full restart":
        print("lunx is restarting")

    elif command == "minkernel":
        print("minkernel is configurate")

    elif command == "lore -s":
        print(lore is superusr)
    
    elif command == "lunx -Install gams":
        print(":")

    elif command == "super gams":
        print("gams is running")

    elif command == "lunx -System":
        print("installing system")
        time.sleep(300)
        print("finish :)")
        time.sleep(0.4)
        print("reboot")
        time.sleep(3)
        os.system("clear")
        os.system("python config.py")

    elif command == "reset":
        os.system("python config.py")
    else:
        os.system(command)
