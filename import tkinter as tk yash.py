import tkinter as tk

def convert_to_cfg():
    pda_description = input_text.get(1.0, tk.END)
    
    # Implement the PDA to CFG conversion logic here
    cfg_output = pda_to_cfg_conversion(pda_description)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, cfg_output)

def clear_text():
    input_text.delete(1.0, tk.END)
    output_text.delete(1.0, tk.END)

def pda_to_cfg_conversion(pda_description):
    # Parse the PDA description (replace this with actual parsing logic)
    pda_info = pda_description.splitlines()
    
    # Extract relevant information (modify based on your PDA description format)
    states = pda_info[0].split(": ")[1]
    input_alphabet = pda_info[1].split(": ")[1]
    stack_alphabet = pda_info[2].split(": ")[1]
    
    # Create CFG production rules (modify based on your conversion logic)
    cfg_output = f"S -> {states} | epsilon\n"
    cfg_output += f"a -> {input_alphabet} | epsilon\n"
    cfg_output += f"b -> {stack_alphabet} | epsilon\n"

    return cfg_output

# Create the main application window
app = tk.Tk()
app.title("PDA to CFG Converter")

# Create input and output text areas
input_label = tk.Label(app, text="PDA Description:")
input_label.pack()
input_text = tk.Text(app, width=40, height=10)
input_text.pack()

output_label = tk.Label(app, text="CFG Output:")
output_label.pack()
output_text = tk.Text(app, width=40, height=10)
output_text.pack()

# Create the Convert and Clear buttons
convert_button = tk.Button(app, text="Convert", command=convert_to_cfg)
convert_button.pack()

clear_button = tk.Button(app, text="Clear", command=clear_text)
clear_button.pack()

# Run the application
app.mainloop()
