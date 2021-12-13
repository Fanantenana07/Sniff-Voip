


import json

def main():
    data = {'item':"concombre",'item2':"carotte",'item3':"courgette"}
    data2 = {'item2':"concombre",'item5':"carotte",'item20':"courgette"}
    jstr  = json.dumps(data)
    with open("Payload/payload.txt","w") as output :
        json.dump(jstr,output)
    
    output.close()

    with open("Payload/payload.txt","w") as output2 :
        json.dump(data2,output2)
    output2.close()

if __name__ == "__main__":
    main()
