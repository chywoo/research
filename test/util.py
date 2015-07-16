__author__ = 'chywoo.park'

import os
import re
import  psutil

def check_file_list(files):
    """
    Check if specified files exist or not in current directory.

    :type files: list
    :param files: File list to check
    :return: File list found
    :rtype: list
    """
    listdir = os.listdir(".")

    file_list = []
    not_exist_list = []

    for f in listdir:
        if os.path.isfile(f):
            file_list.append(f)

    for file in files:
        if file not in file_list:
            not_exist_list.append(file)

    if len(not_exist_list) == 0:
        return None
    else:
        return not_exist_list


def check_dir_list(dirs):
    """
    Check if specified files exist or not in current directory.

    :type dirs: list
    :param dirs: Directory list to check
    :return: File list found
    :rtype: list
    """
    listdir = os.listdir(".")

    file_list = []
    not_exist_list = []

    for f in listdir:
        if os.path.isdir(f):
            file_list.append(f)

    for file in dirs:
        if file not in file_list:
            not_exist_list.append(file)

    if len(not_exist_list) == 0:
        return None
    else:
        return not_exist_list


def grep(pattern, file, trim=False):
    """
    Search pattern in specified file.

    :type trim: bool
    :type file: str
    :type pattern: str
    :param pattern: Regular expression pattern
    :param file: File to find pattern.
    :param trim: Trim result string
    :return: list of found
    :rtype: list
    """
    if file is None or pattern is None:
        return None

    found_list = []

    f = open(file, "r")

    for line in f.readlines():
        if re.findall(r'^.*%s.*?$' % pattern, line, flags=re.M):
            if trim is True:
                line = line.strip()
            found_list.append(line)
    f.close()

    if len(found_list) == 0:
        return None
    else:
        return found_list

def kill(pid):
    """
    Kill process specified by pid paramter

    :param pid: Process ID to kill
    """
    p = psutil.Process(pid)

    try:
        p.kill()
    except Exception:
        pass

def killall(name, params=None):
        """
        Kill process specified by parameters.

        :type name: Process name to kill
        """
        for ps in psutil.process_iter():
            cmdline = ""
            try:
                if ps.name() != name:
                    continue

                if params:
                    cmdline = ps.cmdline()
            except psutil.AccessDenied:
                continue

            ps_found = True

            if params:  # If you want to compare command line
                check_list = []
                if params is list:
                    check_list = params
                elif params is str:
                    check_list = str.split(",")
                else:
                    check_list.append(str(params))

                # Compare command line's parameters
                for item in check_list:
                    ps_found = False

                    for param in cmdline:
                        if param.find(item):
                            ps_found = True
                            break

                    if ps_found is False:   # Process is not found.
                        break

            if ps_found:
                try:
                    ps.kill()
                except Exception:
                    pass
