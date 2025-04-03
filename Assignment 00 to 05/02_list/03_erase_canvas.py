import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = canvas.winfo_pointerx()
    mouse_y = canvas.winfo_pointery()
    
    left_x = mouse_x - ERASER_SIZE // 2
    top_y = mouse_y - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Check if any cell overlaps with the eraser
    for item in canvas.find_overlapping(left_x, top_y, right_x, bottom_y):
        canvas.itemconfig(item, fill="white")  # Change color to white (erase it)

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    # Create a grid of rectangles
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue")
    
    root.after(100, erase_objects, canvas, None)  # Start erasing after a delay
    root.mainloop()

if __name__ == '__main__':
    main()
