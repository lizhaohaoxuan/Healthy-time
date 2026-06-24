import tkinter as tk
import time
import file

config = file.config()
config_times = config.read_config()

def extend_time():
    '''
    Extend the time for 5 mins
    '''
    sub.destroy()

def create_subwindow(master):
    '''
    Create a toplevel to reminder user that it's time for a rest
    '''
    global sub
    sub = tk.Toplevel(master=master)
    sub.geometry('{}x{}'.format(screen_width,screen_height))
    sub.title('time out!')
    sub.focus()
    extend_button = tk.Button(sub, text='extend time')

def work():
    '''
    When the time is one of setting times, this function will execute the create_subwindow()
    '''
    time_now = time.strftime('%H:%M', time.localtime())
    if time_now in config_times:
        create_subwindow(main)
    main.after(1000, work)

main = tk.Tk()
main.geometry('500x300')
main.title('Healthy Timer')
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

main.mainloop()