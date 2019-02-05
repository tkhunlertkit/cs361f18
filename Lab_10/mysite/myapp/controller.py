from myapp.models import User
from myapp.models import Item
from django.core.exceptions import ObjectDoesNotExist

def addUser(args):
    #if args[0] == addUser, adds user named args[1]
    #returns "User <args[1]> added" or "User <args[1]> exists"
    #else returns ""
    if args[0] == "addUser":
        user_count = User.objects.filter(name=args[1]).count()
        if user_count > 0:
            return "user " + args[1] + " exists"

        user = User(name=args[1])
        user.save()
        return "user " + user.name + " added"
    else:
        return ""

def addItem(args):
    #if args[0] == "addItem", adds item args[1] to user args[2]
    #returns "Item <args[1]> added to user <args[2]>"
    #or "User <args[2]> already has item <args[1]>"
    #or "User <args[2]> does not exist"
    #else returns ""
    if args[0] == "addItem":
        user = User.objects.filter(name=args[2])

        if user.count() < 1:
            return "user " + args[2] + " does not exist"

        user = user[0]
        if user.items.filter(name=args[1]).count() > 0:
            return "Item " + args[1] + " are added to user " + args[2]


        item = Item(name=args[1])
        item.save()
        user.items.add(item)
        user.save()
        return "item " + args[1] + " added to user " + args[2]
    else:
        return ""

def display(args):
    #if args[0] == display
    #return a string with each user followed by their items
    #items are indented
    if args[0] == "display":
        sss = ""
        users = User.objects.all()
        for user in users:
            sss += "<strong>" + user.name + "</strong><br>"
            if user.items:
                for item in user.items.all():
                    sss += "<p style=\"padding: 0px 0px 0px 20px; margin:0 0 0 0px; margin-bottom:-20px;\">" + item.name + "</p><br>"
            else:
                sss += "No items..."

        print(sss)
        return sss if sss else "No users"
    else:
        return ""

commandList = [addUser, addItem, display]
def doStuff(s, commandList):
    args = s.split(" ")
    for i in commandList:
        out= i(args)
        if out != "": #if i matches arg[0], stop looping
            break
    if out == "":
        out = "command not found"

    return out