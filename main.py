from mainwindow import Window

if __name__ == '__main__':
    handle = Window()
    handle2 = Window()

    handle.title('Daw')
    handle.geometry('1280x720')

    handle2.title('Daw')
    handle2.geometry('1280x720')

    assert(handle is handle2)
    # #AssertionError

    handle.mainloop()
    handle2.mainloop()
