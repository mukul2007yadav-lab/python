filenames=["1.txt","2.txt","3.txt"]


for file in filenames:
    try:
        with open(file,"r") as f:
            print(f"reading {file}: {f.read()}")

    except FileNotFoundError:
        print(f"LOG:could not find file{file}")
        
    

    