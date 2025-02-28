from sympy import Matrix, Rational  

def rref_fraction(matrix):
    # Convert all elements to fractions
    mat = Matrix([[Rational(num) for num in row] for row in matrix])
    
    # Compute the RREF of the matrix
    rref_matrix, _ = mat.rref()
    
    # Convert the RREF matrix to a string with newlines between rows
    rref_matrix_str = str(rref_matrix).replace('], [', ']\n[')
    
    return rref_matrix_str

# Example usage
matrix = [
    [1, 0, -2, 1, 0, 0],
    [6, 1, 3, 0, 1, 0],
    [2, -7, 3, 0, 0, 1]
]

rref_result = rref_fraction(matrix)
print(rref_result)

import tkinter as tk
from tkinter import messagebox, scrolledtext
from sympy import Matrix, Rational

class MatrixEditor:
    def __init__(self, root):
        self.root = root
        self.rows = 3  # Default number of rows
        self.cols = 3  # Default number of columns
        self.entries = []  # To store the entry widgets (cells)
        
        # Font settings
        self.font = ("Arial", 14)  # Font for input and buttons
        self.output_font = ("Arial", 16)  # Larger font for output
        
        # Create input boxes for matrix size
        self.create_size_inputs()
        
        # Create the matrix input grid
        self.create_matrix_grid()
        
        # Button to calculate RREF
        self.calculate_button = tk.Button(root, text="Calculate RREF", font=self.font, command=self.calculate_rref)
        self.calculate_button.grid(row=self.rows + 2, column=0, columnspan=self.cols + 2)
        
        # Scrollable text box for RREF result
        self.result_text = scrolledtext.ScrolledText(root, width=50, height=10, font=self.output_font)
        self.result_text.grid(row=self.rows + 3, column=0, columnspan=self.cols + 2)
        self.result_text.insert(tk.END, "RREF will appear here")
        self.result_text.config(state=tk.DISABLED)  # Make it read-only
    
    def create_size_inputs(self):
        """Create input boxes for matrix size (rows and columns)."""
        size_frame = tk.Frame(self.root)
        size_frame.grid(row=0, column=0, columnspan=self.cols + 2)
        
        # Label for rows input
        tk.Label(size_frame, text="Rows:", font=self.font).grid(row=0, column=0)
        self.rows_input = tk.Entry(size_frame, width=5, font=self.font)
        self.rows_input.grid(row=0, column=1)
        self.rows_input.insert(0, str(self.rows))
        
        # Label for columns input
        tk.Label(size_frame, text="Columns:", font=self.font).grid(row=0, column=2)
        self.cols_input = tk.Entry(size_frame, width=5, font=self.font)
        self.cols_input.grid(row=0, column=3)
        self.cols_input.insert(0, str(self.cols))
        
        # Button to update matrix size
        self.update_size_button = tk.Button(size_frame, text="Update Size", font=self.font, command=self.update_matrix_size)
        self.update_size_button.grid(row=0, column=4)
    
    def create_matrix_grid(self):
        """Create a grid of Entry widgets for matrix input."""
        # Clear existing entries if any
        for row in self.entries:
            for entry in row:
                entry.destroy()
        self.entries.clear()
        
        # Create new grid
        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                entry = tk.Entry(self.root, width=5, font=self.font)
                entry.grid(row=i + 1, column=j)
                entry.insert(0, "0")  # Default value
                row_entries.append(entry)
            self.entries.append(row_entries)
    
    def update_matrix_size(self):
        """Update the matrix size based on user input."""
        try:
            new_rows = int(self.rows_input.get())
            new_cols = int(self.cols_input.get())
            if new_rows <= 0 or new_cols <= 0:
                raise ValueError("Rows and columns must be positive integers.")
            
            # Update matrix size
            self.rows = new_rows
            self.cols = new_cols
            
            # Recreate the matrix grid
            self.create_matrix_grid()
            
            # Adjust button and result text positions
            self.calculate_button.grid(row=self.rows + 2, column=0, columnspan=self.cols + 2)
            self.result_text.grid(row=self.rows + 3, column=0, columnspan=self.cols + 2)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def calculate_rref(self):
        """Calculate the RREF of the matrix and display the result."""
        try:
            # Read the matrix from the GUI
            matrix = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    value = self.entries[i][j].get()
                    row.append(int(value))  # Convert input to integer
                matrix.append(row)
            
            # Convert to SymPy Matrix with Rational numbers
            mat = Matrix([[Rational(num) for num in row] for row in matrix])
            
            # Compute RREF
            rref_matrix, _ = mat.rref()
            
            # Format the RREF result as a string
            rref_str = str(rref_matrix).replace('], [', ']\n[')
            
            # Update the result text box
            self.result_text.config(state=tk.NORMAL)  # Enable editing
            self.result_text.delete(1.0, tk.END)  # Clear previous content
            self.result_text.insert(tk.END, f"RREF:\n{rref_str}")
            self.result_text.config(state=tk.DISABLED)  # Make it read-only
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def run(self):
        """Run the GUI."""
        self.root.mainloop()

# Main program
if __name__ == "__main__":
    # Create the Tkinter root window
    root = tk.Tk()
    root.title("Matrix RREF Calculator")
    
    # Create the MatrixEditor GUI
    editor = MatrixEditor(root)
    
    # Run the GUI
    editor.run()