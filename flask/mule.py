def main():
    while True:
        message = uwsgi.mule_get_msg()
        print(f'Mule received a message: {message}')


if __name__ == '__main__':
    main()

