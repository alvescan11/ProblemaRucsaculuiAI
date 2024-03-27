from ui.ui import UI


def main():
    ui = UI("files/rucsac20.txt")
    ui.run_menu()

if __name__ == "__main__":
    l = [1,2,3,4]
    l.append(4)
    l.pop(4)
    print(l)
