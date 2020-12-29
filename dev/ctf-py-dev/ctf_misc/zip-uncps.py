import zipfile


def un_cps(name, pwd=None):
    fz = zipfile.ZipFile(name, 'r')
    if pwd is None:
        fz.extractall()
    else:
        fz.extractall(pwd=bytes(pwd, 'utf-8'))
    fz.close()


if __name__ == '__main__':
    pass
