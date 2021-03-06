"""
This is a brief illustration of
1. the "if __name__ == '__main__'" pattern.
    When the Python interpreter reads a source file, it executes all of the code found in it.
    Before executing the code, it will define a few special variables. For example, if the Python interpreter is running
    that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__".
    If this file is being imported from another module, __name__ will be set to the module's name.
2. The use of functions.
    A function is a block of organized, reusable code that is used to perform a single, related action. Functions
    provide better modularity for your application and a high degree of code reuse.
3. The use of error handling using try...except.
    In Python, exceptions can be handled using a try statement. The critical operation which can raise an exception is
    placed inside the try clause. The code that handles the exceptions is written in the except clause. We can thus
    choose what operations to perform once we have caught the exception.
4. How to read a file from the Internet with 'requests'.
    The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with
    all the response data (content, encoding, status, etc). It is assumed that 'requests' is installed.
5. How to read a file from the computer's file system.
    In Python you need to give access to a file by opening it. You can do it by using the open() function. Open returns
    a file object, which has methods and attributes for getting information about and manipulating the opened file.
    The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks. In addition,
    it will automatically close the file. The with statement provides a way for ensuring that a clean-up is always used.


Mark Foley
October 2020
"""

import requests

def print_error_and_exit(error, return_code):
    print(f"{'='*50}\nSomething bad happened.\n{error}\n{'='*50}")
    quit(return_code)


def get_file_from_net(url):
    try:
        response = requests.get(url)
        if 200 <= response.status_code <= 299:
            if response.headers["Content-Type"] and "text" in response.headers["Content-Type"]:
                return response.text
            else:
                raise ValueError(
                    f"Doesn't look like printable content\nContent-Type is '{response.headers['Content-Type']}'"
                )
        else:
            raise ValueError(f"Bad status code: {response.status_code}")
    except Exception as e:
        print_error_and_exit(e, 1)


def read_any_file(file_name):
    try:
        with open(file_name, "r") as fh:
            data = fh.read()
            return data
    except Exception as e:
        print_error_and_exit(e, 2)

def print_content(content):
    print(f"Content is\n{'='*50}\n{content}")


def main():
    URL = "https://i.dell.com/is/image/DellContent//content/dam/global-asset-library/Products/Notebooks/XPS/13_9300_non-touch/xs9300nt_cnb_00055lf110_gy.psd?fmt=pjpg&pscan=auto&scl=1&hei=402&wid=719&qlt=95,0&resMode=sharp2&op_usm=1.75,0.3,2,0&size=719,402"
    FILE = "hnr1.abc"

    net_content = get_file_from_net(URL)
    file_content = read_any_file(FILE)

    print_content(net_content)
    print_content(file_content)

if __name__ == "__main__":
    main()


