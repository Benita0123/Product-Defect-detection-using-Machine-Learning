def open_third_gui(image_folder, svc_acc, nb_acc, xgb_acc, svc_prec, nb_prec, xgb_prec, svc_rec,nb_rec,xgb_rec,svc_f1sc,nb_f1sc,xgb_f1sc,spec_svc,spec_nb,spec_xgb,classifiers, processed_image_paths,svc_pred,nb_pred,xgb_pred,y_test):

    third_window = Tk()
    third_window_width = 1359
    third_window_height = 699

    screen_width = third_window.winfo_screenwidth()
    screen_height = third_window.winfo_screenheight()

    x = (screen_width // 2) - (third_window_width // 2)
    y = (screen_height // 2) - (third_window_height // 2)

    third_window.geometry(f"{third_window_width}x{third_window_height}+{x}+{y}")
    third_window.configure(bg="#08092F")


    image_image_3 = Image.open(relative_to_assets_3("IMAGE_8.png"))
    image_3_resized = image_image_3.resize((1359, 899), Image.BILINEAR)
    image_3 = ImageTk.PhotoImage(image_3_resized)
    image_3_label = Label(third_window, image=image_3, bg="#6B71FF")
    image_3_label.image = image_3
    image_3_label.place(x=0, y=0)

    canvas = Canvas(
        third_window,
        bg="#6B71FF",
        width=1359,
        height=899,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)



    canvas.create_image(0, 0, anchor="nw", image=image_3)

    # Display accuracies (already correctly positioned)
    canvas.create_text(473, 239, text=f"{svc_acc * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(473, 329, text=f"{nb_acc * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(473, 422, text=f"{xgb_acc * 100:.2f}%", fill="white", font=("Inter Black", 35))

    # Display precisions
    canvas.create_text(673, 239, text=f"{svc_prec * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(673, 329, text=f"{nb_prec * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(673, 422, text=f"{xgb_prec * 100:.2f}%", fill="white", font=("Inter Black", 35))

    # Display recalls
    canvas.create_text(873, 239, text=f"{svc_rec * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(873, 329, text=f"{nb_rec * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(873, 422, text=f"{xgb_rec * 100:.2f}%", fill="white", font=("Inter Black", 35))

    # Display F1 scores
    canvas.create_text(1073, 239, text=f"{svc_f1sc * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(1073, 329, text=f"{nb_f1sc * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(1073, 422, text=f"{xgb_f1sc * 100:.2f}%", fill="white", font=("Inter Black", 35))

    # Display Spec scores
    canvas.create_text(1273, 239, text=f"{spec_svc * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(1273, 329, text=f"{spec_nb * 100:.2f}%", fill="white", font=("Inter Black", 35))
    canvas.create_text(1273, 422, text=f"{spec_xgb * 100:.2f}%", fill="white", font=("Inter Black", 35))

    button_image_3 = PhotoImage(file=relative_to_assets_3("button_3.png"))
    graph_button = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: plot_graph(svc_acc, nb_acc, xgb_acc), relief="flat")
    graph_button.place(x=1125.0, y=520.0, width=190.13, height=56.0)

    button_image_4 = PhotoImage(file=relative_to_assets_3("button_4.png"))
    result_button = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: display_random_image(processed_image_paths, classifiers), relief="flat")
    result_button.place(x=1125.0, y=620.0, width=190.13, height=56.0)

    button_image_5 = PhotoImage(file=relative_to_assets_3("button_5.png"))
    back_button = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: [ proceedto_second_gui(third_window)], relief="flat")
    back_button.place(x=50.0, y=620.0, width=190.13, height=56.0)

    hlp_button1 = Button(text="?", borderwidth=0, highlightthickness=0, font=("Arial", 9, "bold"),
                        command=lambda: show_help1(), relief="flat")
    hlp_button1.place(x=1315.0, y=28.0, width=26.00, height=26.0)

    #Button in my third GUI :
    button_image_6 = PhotoImage(file=relative_to_assets_3("button_6.png"))
    cnm_button = Button(image=button_image_6, borderwidth=0, highlightthickness=0,
                      command=cnmatrix, relief="flat")
    cnm_button.place(x=855.0, y=620.0, width=190.13, height=56.0)

    button_image_7 = PhotoImage(file=relative_to_assets_3("image_7.png"))
    calc_button = Button(image=button_image_7, borderwidth=0, highlightthickness=0,command=open_metric_calculator, relief="flat")
    calc_button.place(x=855.0, y=520.0, width=190.13, height=56.0)

    button_image_8 = PhotoImage(file=relative_to_assets_3("button_7.png"))
    count_btn = Button(image=button_image_8, borderwidth=0, highlightthickness=0, command=lambda: show_image_counts(image_folder),
                      relief="flat")
    count_btn.place(x=585.0, y=620.0, width=190.13, height=56.0)

    third_window.resizable(False, False)
    third_window.mainloop()