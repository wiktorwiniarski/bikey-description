import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip
from colored import fg, bg, attr
from PIL import ImageTk, Image


class ParagraphGenerator:
    def __init__(self):
        self.icon_name = ''
        self.paragraph_title = ''
        self.paragraph_content = ''
        self.image_link = ''

        self.window = tk.Tk()
        self.window.title("BIKEY.PL® | DESCRIPTION GENERATOR")

        # Logo programu - Bikey®
       # frame = Frame(self.window, width=50, height=50)
        #frame.pack()
        #frame.place(anchor='center', relx=0.5, rely=0.5)
        #img = ImageTk.PhotoImage(Image.open("icon.png"))
        #label = Label(frame, image = img)
        #label.pack()

        # Label and Entry for Icon Selection
        icon_label = tk.Label(self.window, text="Icon Name (Font Awesome Library): ")
        icon_label.pack()
        self.icon_entry = tk.Entry(self.window)
        self.icon_entry.pack()
        self.icon_entry.configure(width=20)

        self.icon_clear_button = tk.Button(self.window, text="Clear", command=self.clear_icon_entry)
        self.icon_clear_button.pack()
        self.icon_clear_button.configure(foreground='red')

        # Label and Entry for Paragraph Title
        title_label = tk.Label(self.window, text="Paragraph Title: ")
        title_label.pack()
        self.title_entry = tk.Entry(self.window)
        self.title_entry.pack()
        self.title_entry.configure(width=60)

        self.title_clear_button = tk.Button(self.window, text="Clear", command = self.clear_title_entry)
        self.title_clear_button.pack()
        self.title_clear_button.configure(foreground='red')

        # Label and Entry for Paragraph Content
        content_label = tk.Label(self.window, text="Paragraph Content: ")
        content_label.pack()
        self.content_entry = tk.Entry(self.window, width=60)
        self.content_entry.pack()
       
        self.content_clear_button = tk.Button(self.window, text="Clear", command = self.clear_content_entry)
        self.content_clear_button.pack()
        self.content_clear_button.configure(foreground='red')

        # Label and Entry for Image Link
        image_label = tk.Label(self.window, text="Image Link: ")
        image_label.pack()
        self.image_entry = tk.Entry(self.window)
        self.image_entry.pack()
        self.image_entry.configure(width=60)

        self.img_clear_button = tk.Button(self.window, text = "Clear", command = self.clear_image_entry)
        self.img_clear_button.pack()
        self.img_clear_button.configure(foreground='red')

        # Button to Generate Paragraph
        generate_button = tk.Button(self.window, text="Generate Paragraph", command=self.generate_paragraph)
        generate_button.pack()
        generate_button.configure(foreground='green',pady=8,font='sans 16 bold')

        # Text Box to Display Generated HTML Code
        self.generated_html = tk.Text(self.window, height=15, width=60)
        self.generated_html.pack()

        # Button to Reset Form
       
        reset_button = tk.Button(self.window, text="Reset", command=self.reset_form, bg="red")
        reset_button.pack()
        reset_button.configure(foreground='red')


        # Button to remove last paragraph
        del_last_pg_button = tk.Button(self.window, text="Delete last paragraph", command = self.remove_last_paragraph)
        del_last_pg_button.pack()
        del_last_pg_button.configure(foreground='red')

        # Button to copy all text
        copy_button = tk.Button(self.window, text="Copy all text", command= self.copy_summed_html)
        copy_button.pack()
        copy_button.configure(foreground='green',pady=8,font='sans 16 bold')

        # Text Box to Display Sum of Generated HTML Code
        self.summed_html = tk.Text(self.window, height=30, width=60)
        self.summed_html.pack()

        self.generated_responses = []


        





        self.window.mainloop()

    def generate_paragraph(self):
        self.icon_name = self.icon_entry.get()
        self.paragraph_title = self.title_entry.get()
        self.paragraph_content = self.content_entry.get()
        self.image_link = self.image_entry.get()

        html_code = f'''
         <!--============= SECTION =============-->
            <div class="product-section">
            <div class="product-section-icon">
            <i class="fa-solid fa-{self.icon_name}"></i>
            </div>
            <div class="product-section-content">
            <div class="product-section-title">
            <h2>{self.paragraph_title}</h2>
            </div>
            <div class="product-section-line"></div>
            <div class="product-section-decription">{self.paragraph_content}</div>
            <div class="product-section-image">
            <img src="{self.image_link}" alt="Sklep rowerowy BIKEY.PL - {self.paragraph_title}">
            </div>
        </div>
        </div>
        <!-- ============= END SECTION =============-->


        

        '''
       
        self.generated_html.delete("1.0", tk.END)
        self.generated_html.insert(tk.END, html_code)

        self.generated_responses.append(html_code)
        summed_html = ''.join(self.generated_responses)

        self.summed_html.configure(fg="green")
        self.summed_html.delete("1.0", tk.END)
        self.summed_html.insert(tk.END, summed_html)









    def remove_last_paragraph(self): 
        if len(self.generated_responses) > 0:
            self.generated_responses.pop()
            summed_html = ''.join(self.generated_responses)
            self.summed_html.delete("1.0", tk.END)
            self.summed_html.insert(tk.END, summed_html)
            self.generated_html.delete("1.0", tk.END)
        else:
            tk.messagebox.showwarning("Warning", "No Paragraphs to Remove")
       



    
    def reset_form(self):
        self.icon_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_entry.delete(0, tk.END)
        self.image_entry.delete(0, tk.END)
        self.generated_html.delete("1.0", tk.END)
        self.generated_responses = []
        self.summed_html.delete("1.0", tk.END)

    # Assuming self.paragraphs is a list containing the paragraph IDs
    # and self.paragraph_text is a dictionary mapping paragraph IDs to their text content

    def clear_icon_entry(self):
        self.icon_entry.delete(0, tk.END)

    def clear_title_entry(self):
        self.title_entry.delete(0, tk.END)

    def clear_content_entry(self):
        self.content_entry.delete(0, tk.END)

    def clear_image_entry(self):
        self.image_entry.delete(0, tk.END)




    def copy_summed_html(self):
        summed_html = self.summed_html.get("1.0", tk.END)
        pyperclip.copy(summed_html)
        messagebox.showinfo("Copied to Clipboard", "Copied, insert the product description @ BIKEY.PL")

 
   

if __name__ == '__main__':
    ParagraphGenerator()


    