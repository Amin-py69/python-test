

def show_color(name):

    colors = {
        'space': 'blue',
        'mind': 'yellow',
        'reality': 'red',
        'power': 'purple',
        'time': 'green',
        'soul': 'orange',
    }
    return colors.get(name, "unknown")


name = input()
colors = show_color(name)
print(colors)
