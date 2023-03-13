from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import Label, Canvas, Tk, Entry, Button


def preview_watermark():
    draw = ImageDraw.Draw(raw_image)
    fnt_size = int(fontsize.get())
    font = ImageFont.truetype("arial.ttf", fnt_size)
    wtrmrk = watermark.get()
    textwidth, textheight = draw.textsize(text=wtrmrk, font=font)
    width, height = raw_image.size
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text=wtrmrk, font=font)
    raw_image.show()

def save():
    raw_image.save("watermarked.jpg")
    exit()


# def clear_wtrmk():
#     new_img = Image.open("batman.jpg")
#     new_pic = new_img.resize((700, 500))
#     prev_pic = ImageTk.PhotoImage(new_pic)
#     picture.config(image=prev_pic)
#     picture.image = prev_pic


# def load_pic():
#     pass


app_window = Tk()
app_window.minsize()
app_window.config(padx=50, pady=50)
app_window.title("Watermarking tool")



# Image resize to fit window

raw_image = Image.open("image.jpg")
images = raw_image.resize((700, 500))
wtr_img = ImageTk.PhotoImage(images)

picture = Label(image=wtr_img)
picture.image = wtr_img
picture.grid(column=0, row=0, columnspan=2)

# Watermark Details

watermark = Entry()
watermark.grid(column=0, row=1)

# watermark label

wtr_label = Label(text="Type in your watermark above", font=("Arial", 12, "bold"))
wtr_label.grid(column=0, row=2)

# watermark preview button

wtr_prev_butt = Button(text="Preview", command=preview_watermark)
wtr_prev_butt.grid(column=0, row=3)

# fontsize entry

fontsize = Entry()
fontsize.grid(column=1, row=1)

# fontsize label

fnt_lbl = Label(text="Specify the font size", font=("Arial", 12, "bold"))
fnt_lbl.grid(column=1, row=2)

# save button

save = Button(text="Save", command=save)
save.grid(column=1, row=3)



# draw = ImageDraw.Draw(resize_images)
#
# watermark = "Property of Chris Mukirae"
# font = ImageFont.truetype("arial.ttf", 25)
# textwidth, textheight = draw.textsize(text=watermark, font=font)
# width, height = raw_image.size
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin
# draw.text((x, y), text=watermark, font=font)
# resize_images.show()
# resize_images.save("watermarked.jpg")
app_window.mainloop()
