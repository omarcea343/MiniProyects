import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkbootstrap import Style
from PIL import ImageGrab

class Whiteboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Whiteboard")
        self.master.resizable(False, False)
        
        # Set ttkbootstrap style
        self.style = Style(theme="pulse")
        
        # Create Canvas
        self.canvas = tk.Canvas(self.master, width=1200, height=800, bg="white")
        self.canvas.pack()
        
        # Create buttons
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(side="top", pady=10)
        
        # Button configuration
        button_config = {
            "black": ("dark.Tbutton", lambda: self.change_color("black")),
            "red": ("danger.Tbutton", lambda: self.change_color("red")),
            "blue": ("info.Tbutton", lambda: self.change_color("blue")),
            "green": ("success.Tbutton", lambda: self.change_color("green")),
            "clear": ("light.Tbutton", self.clear_canvas),
            "save": ("primary.Tbutton", self.save_image)  # New save button
        }
        
        # Add buttons to the button frame
        for color, (style, command) in button_config.items():
            ttk.Button(self.button_frame, text=color.capitalize(), 
                       command=command, style=style).pack(side="left", padx=5, pady=5)
            
        # Initialize drawing variables
        self.draw_color = "black"
        self.line_width = 5
        self.old_x, self.old_y = None, None
        
        # Add event listeners
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        
    # Save starting point of line
    def start_line(self, event):
        self.old_x, self.old_y = event.x, event.y
        
    # Draw line from starting point to current point and then update starting point
    def draw_line(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, 
                                    width=self.line_width, fill=self.draw_color, 
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.old_x, self.old_y = event.x, event.y
    
    # Update current drawing color
    def change_color(self, new_color):
        self.draw_color = new_color    
    
    # Delete all items on the canvas
    def clear_canvas(self):
        self.canvas.delete("all")
        
    # Save the canvas as an image
    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
        if file_path:
            x = self.master.winfo_rootx() + self.canvas.winfo_x()
            y = self.master.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
        
if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    root.mainloop()
