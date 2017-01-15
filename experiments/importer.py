def importApps():
    # goes every available url, exposes the source, pulls the important info and returns all applicants in an array
    # (str)->(array)

    array = []

    openpage()
    while (True):
        # for (amount of app_ids on page):
        temp = ctrls()
        temp = format(temp)
        array.append(temp)

        # if not last page:
        changepage()
        importApps()
    break

    return array



def openpage():
    # navigates pyautogui to webpage

def changepage():
    # changes page

def ctrls():
    # uses pygui to copy the raw html

def format():
    # interacts with the clipboard to bring in the html and cut out alot of the extra bs.
