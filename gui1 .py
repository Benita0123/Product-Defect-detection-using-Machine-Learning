def load_first_gui():
    
    window = Tk()

    canvas = Canvas(
        window,
        bg="#0052CC",
        height=642,
        width=787,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    window_width = 787
    window_height = 642

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.configure(bg='white')

    image_image_4 = Image.open(relative_to_assets_1("image_4.png"))
    image_4_resized = image_image_4.resize((795, 652), Image.BILINEAR)
    image_4 = ImageTk.PhotoImage(image_4_resized)
    image_4_label = Label(window, image=image_4, bg="#6B71FF")
    image_4_label.image = image_4
    image_4_label.place(x=-5, y=3)

    button_image_1 = PhotoImage(file=relative_to_assets_1("button_1.png"))
    continue_button = Button(image=button_image_1, font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0,
                      command=lambda: proceedto_second_gui(window), relief="flat")
    continue_button.place(x=550.0, y=465.0, width=190.13, height=56.0)

    button_image_2 = PhotoImage(file=relative_to_assets_1("button_2.png"))
    back_button = Button(image=button_image_2, font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0,
                      command=lambda: window.destroy(), relief="flat")
    back_button.place(x=550.0, y=565.0, width=186.0, height=56.0)

    hlp_button = Button(text="?", borderwidth=0, highlightthickness=0, font=("Arial", 9, "bold"),
                        command=lambda: show_help(), relief="flat")
    hlp_button.place(x=3.0, y=8.0, width=20.00, height=20.0)

    window.resizable(False, False)
    window.mainloop()

load_first_gui()