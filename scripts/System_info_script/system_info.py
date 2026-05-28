import platform
import psutil 

def main():


    print(platform.system())
    print(platform.version())
    print(platform.node())
    print(platform.architecture())

    print(psutil.cpu_count())
    print(psutil.virtual_memory())
    print(psutil.disk_usage("C:\\"))

     









if __name__ == "__main__":
    main()
   