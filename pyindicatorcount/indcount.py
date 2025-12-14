import tkinter as tk
from tkinter import messagebox

# desc -> ind
indicator_mapping = {
    "Strong Logic": "IND1",
    "Strong Will": "IND2",
    "Strong Physics": "IND3",
    "Strong Emotion": "IND4",
    "Weak Logic": "IND5",
    "Weak Will": "IND6",
    "Weak Physics": "IND7",
    "Weak Emotion": "IND8",
    "Rigid Logic": "IND9",
    "Rigid Will": "IND10",
    "Rigid Physics": "IND11",
    "Rigid Emotion": "IND12",
    "Flexible Logic": "IND13",
    "Flexible Will": "IND14",
    "Flexible Physics": "IND15",
    "Flexible Emotion": "IND16",
    "Result Logic": "IND17",
    "Result Will": "IND18",
    "Result Physics": "IND19",
    "Result Emotion": "IND20",
    "Process Logic": "IND21",
    "Process Will": "IND22",
    "Process Physics": "IND23",
    "Process Emotion": "IND24"
}

def count_occurrences(text, indicators):
    # case insen.
    text_lower = text.lower()
    
  # counting
    counts = {indicator: 0 for indicator in indicators.values()}
    
    
    for desc, ind in indicators.items():
        
        counts[ind] += text_lower.count(f"ind: {desc.lower()}")
        
        counts[ind] += text_lower.count(ind.lower())
    
    return counts

def analyze_text():
    # input
    text = text_input.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Input Error", "hey, enter some text!")
        return
    
    
    occurrences = count_occurrences(text, indicator_mapping)
    
   
    strong_indicators = {k: v for k, v in indicator_mapping.items() if v in ["IND1", "IND2", "IND3", "IND4"]}
    weak_indicators = {k: v for k, v in indicator_mapping.items() if v in ["IND5", "IND6", "IND7", "IND8"]}
    rigid_flexible_indicators = {k: v for k, v in indicator_mapping.items() if v in ["IND9", "IND10", "IND11", "IND12", "IND13", "IND14", "IND15", "IND16"]}
    result_indicators = {k: v for k, v in indicator_mapping.items() if v in ["IND17", "IND18", "IND19", "IND20"]}
    process_indicators = {k: v for k, v in indicator_mapping.items() if v in ["IND21", "IND22", "IND23", "IND24"]}
    
    
    results_output.delete("1.0", tk.END)  # Clear previous results
    
    
    results_output.insert(tk.END, "Strong Indicators:\n")
    for desc, ind in strong_indicators.items():
        results_output.insert(tk.END, f"{ind} = {desc}: {occurrences[ind]} times\n")
    results_output.insert(tk.END, "\n")
    
    
    results_output.insert(tk.END, "Weak Indicators:\n")
    for desc, ind in weak_indicators.items():
        results_output.insert(tk.END, f"{ind} = {desc}: {occurrences[ind]} times\n")
    results_output.insert(tk.END, "\n")
    
   
    results_output.insert(tk.END, "Rigid/Flexible Indicators:\n")
    for desc, ind in rigid_flexible_indicators.items():
        results_output.insert(tk.END, f"{ind} = {desc}: {occurrences[ind]} times\n")
    results_output.insert(tk.END, "\n")
    
    
    results_output.insert(tk.END, "Result Indicators:\n")
    for desc, ind in result_indicators.items():
        results_output.insert(tk.END, f"{ind} = {desc}: {occurrences[ind]} times\n")
    results_output.insert(tk.END, "\n")
    
    
    results_output.insert(tk.END, "Process Indicators:\n")
    for desc, ind in process_indicators.items():
        results_output.insert(tk.END, f"{ind} = {desc}: {occurrences[ind]} times\n")

def make_sheet():
   
    text = text_input.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text!")
        return
    
    
    occurrences = count_occurrences(text, indicator_mapping)
    
    # table
    table = {
        "Strong": {"Logic": occurrences["IND1"], "Will": occurrences["IND2"], "Physics": occurrences["IND3"], "Emotion": occurrences["IND4"]},
        "Weak": {"Logic": occurrences["IND5"], "Will": occurrences["IND6"], "Physics": occurrences["IND7"], "Emotion": occurrences["IND8"]},
        "Rigid": {"Logic": occurrences["IND9"], "Will": occurrences["IND10"], "Physics": occurrences["IND11"], "Emotion": occurrences["IND12"]},
        "Flexible": {"Logic": occurrences["IND13"], "Will": occurrences["IND14"], "Physics": occurrences["IND15"], "Emotion": occurrences["IND16"]},
        "Result": {"Logic": occurrences["IND17"], "Will": occurrences["IND18"], "Physics": occurrences["IND19"], "Emotion": occurrences["IND20"]},
        "Process": {"Logic": occurrences["IND21"], "Will": occurrences["IND22"], "Physics": occurrences["IND23"], "Emotion": occurrences["IND24"]}
    }
    
    
    sheet_window = tk.Toplevel(root)
    sheet_window.title("Results Sheet")
    sheet_window.geometry("500x300")
    
    
    sheet_output = tk.Text(sheet_window, height=20, width=60)
    sheet_output.pack(pady=10)
    
    
    sheet_output.insert(tk.END, f"{'':<12}{'Logic':<10}{'Will':<10}{'Physics':<10}{'Emotion':<10}\n")
    sheet_output.insert(tk.END, "-" * 50 + "\n")
    
   
    for category, values in table.items():
        sheet_output.insert(tk.END, f"{category:<12}")
        for key, value in values.items():
            sheet_output.insert(tk.END, f"{value:<10}")
        sheet_output.insert(tk.END, "\n")

def show_notes():
   
    notes_window = tk.Toplevel(root)
    notes_window.title("Notes")
    notes_window.geometry("400x100")
    
    
    note_text = (
        "Designed for the Psychosophia server.\n"
        "Made for indicator-based Psychosophy typings.\n"
        "Contact Lia / @spe3ctre on Discord for any concerns."
    )
    tk.Label(notes_window, text=note_text, justify=tk.LEFT).pack(pady=10)


root = tk.Tk()
root.title("Psychosophia's Indicator Counter")  # Set the window title
root.geometry("600x500")


tk.Label(root, text="Enter Text:").pack(pady=5)
text_input = tk.Text(root, height=10, width=70)
text_input.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze Text", command=analyze_text)
analyze_button.pack(pady=10)

make_sheet_button = tk.Button(root, text="Make Sheet", command=make_sheet)
make_sheet_button.pack(pady=10)

notes_button = tk.Button(root, text="Notes", command=show_notes)
notes_button.pack(pady=10)

tk.Label(root, text="Results:").pack(pady=5)
results_output = tk.Text(root, height=20, width=70)
results_output.pack(pady=5)

# run
root.mainloop()
