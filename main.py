import socket
import time

HOST = "10.0.2.15"    # The remote host
PORT = 30002              # The same port as used by the server

file = open("/media/sf_UR_Shared/Waypoints.txt", "r")
sr = file.read()
arr = sr.split("\n")
print("Number of waypoints:", len(arr))
time.sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print("\nTrying to connect with robot")
    time.sleep(2)
    s.connect((HOST, PORT))
    time.sleep(2)
    print("Connection established with robot\n")
except:
        print("Robot not activated")
        exit(0)
time.sleep(0.05)

count = 0
while (count < len(arr)):
    # s.send (("set_digital_out(2,True)" + "\n").encode("utf-8"))

    # s.send(("set_digital_in(2,True)" + "\n").encode("utf-8"))
    print("Waypoint "+str(count+1)+":", arr[count])
    s.send (("movej(["+str(arr[count]) +",-2.2775736604458237, 3.3528323423665642, -1.2291967454894914], a=1.3962634015954636, v=1.0471975511965976)" + "\n").encode("utf-8"))
    time.sleep(2)
    data = s.recv(1024)
    print ("Response from robot", str(data)+"\n")


    count += 1
print ("Program finish")
s.close()
