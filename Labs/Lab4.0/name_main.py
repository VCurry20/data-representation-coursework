# namemain.py

# https://www.youtube.com/watch?v=g_wlZ9IhbTs

# name page - is the file being run as a script or imported


# the use of this means this is a file that can be used // we can run scipt 
# allows you to check for issues and prevents the code for running and running


print(__name__, type(__name__))


def main ():
    print("Hello, World!")


if __name__ == "__main__":
    main()