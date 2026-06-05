import customtkinter
from pathlib import Path
from PIL import Image
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
FERMACON_ICO = BASE_DIR / "assets" / "images" / ".ico"
FERMACON_PNG = BASE_DIR / "assets" / "images" / "fermacon_white.png"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # self.iconbitmap(FERMACON_ICO)
        self.title("Fermacon Material de Construção")
        self.geometry("720x640")
        self.after(0, lambda: self.state("zoomed"))

        # Frame central
        self.center_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Logo
        img = Image.open(FERMACON_PNG)
        self.logo_image = customtkinter.CTkImage(light_image=img, dark_image=img, size=(450, 450))
        self.logo_label = customtkinter.CTkLabel(self.center_frame, image=self.logo_image, text="")
        self.logo_label.pack(pady=(0, 40))

        # Botão
        self.button = customtkinter.CTkButton(
            self.center_frame,
            text="Criar orçamento",
            command=self.button_callbck,
            width=250,
            height=55,
            font=customtkinter.CTkFont(size=18, weight="bold"),
            corner_radius=13
        )
        self.button.pack()

        # Data e hora — canto inferior direito
        self.datetime_label = customtkinter.CTkLabel(
            self,
            text="",
            font=customtkinter.CTkFont(size=13),
            text_color="gray"
        )
        self.datetime_label.place(relx=1.0, rely=1.0, anchor="se", x=-16, y=-12)
        self._update_datetime()

    def _update_datetime(self):
        now = datetime.now().strftime("%d/%m/%Y   %H:%M:%S")
        self.datetime_label.configure(text=now)
        self.after(1000, self._update_datetime)

    def button_callbck(self):
        print("button clicked")

if __name__ == "__main__":
    app = App()
    app.mainloop()