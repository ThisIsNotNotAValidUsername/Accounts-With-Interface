from gui import *

def main() -> None:
    root = Tk()
    root.title('Account Manager')
    root.geometry(f'500x400')
    Gui(root)

    root.mainloop()

if __name__ == '__main__':
    main()