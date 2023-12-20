
import tkinter as tk


def Admition_Voucher():
  


    def generate_fee_voucher():
        student_name = entry_name.get()
        course_fee = entry_course_fee.get()

        # Validate input
        if not student_name or not course_fee.isdigit():
            result_label.config(text="Invalid input. Please enter valid data.")
            return

        total_fee = int(course_fee)

        # Create fee voucher text
        voucher_text = f"Student Name: {student_name}\nCourse Fee: {course_fee} Rs.\nTotal Fee: {total_fee} Rs."

        # Display the voucher
        result_label.config(text=voucher_text)

    # Create the main window
    root.title("Fee Voucher Generator")

    # Create and place widgets
    label_name = tk.Label(root, text="Student Name:")
    label_name.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1, padx=10, pady=10)

    label_course_fee = tk.Label(root, text="Course Fee:")
    label_course_fee.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    entry_course_fee = tk.Entry(root)
    entry_course_fee.grid(row=2, column=1, padx=10, pady=10)

    generate_button = tk.Button(root, text="Generate Voucher", command=generate_fee_voucher)
    generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)



def Semester_Voucher():
    


    def generate_fee_voucher():

        def   print_fee_voucher():
            out=tk.Label(root,text="Printed").grid(row=9,column=0, columnspan=2, pady=10)

        student_name = entry_name.get()
        course_fee = entry_course_fee.get()
        generate_button = tk.Button(root, text="Print Voucher", command=print_fee_voucher)
        generate_button.grid(row=8, column=0, columnspan=2, pady=10)


        # Validate input
        if not student_name or not course_fee.isdigit():
            result_label.config(text="Invalid input. Please enter valid data.")
            return

        total_fee = int(course_fee)

        # Create fee voucher text
        voucher_text = f"Student Name: {student_name}\nSemester Fee: {course_fee} Rs.\nTotal Fee: {total_fee} Rs."

        # Display the voucher
        result_label.config(text=voucher_text)

    # Create the main window
    root.title("Fee Voucher Generator")

    # Create and place widgets
    label_name = tk.Label(root, text="Student Name:")
    label_name.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1, padx=10, pady=10)

    label_course_fee = tk.Label(root, text="Semester Fee:")
    label_course_fee.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    entry_course_fee = tk.Entry(root)
    entry_course_fee.grid(row=2, column=1, padx=10, pady=10)

    generate_button = tk.Button(root, text="Generate Voucher", command=generate_fee_voucher)
    generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)



def Repeat_course():
    

    def generate_fee_voucher():
        
        student_name = entry_student_name.get()
        course = entry_course.get()
        amount = entry_amount.get()

        # Assuming a simple printout for demonstration purposes
        voucher_text = f"Fee Voucher\n\nStudent Name: {student_name}\nSemeter: {course}\nAmount: {amount}Rs."

        # Display the fee voucher in a new window
        voucher_window = tk.Toplevel(root)
        voucher_window.title("Fee Voucher")
        voucher_label = tk.Label(voucher_window, text=voucher_text, padx=20, pady=20)
        voucher_label.pack()
        
        

    # Create the main window
    root = tk.Tk()
    root.title("Fee Voucher Generator")

    # Create labels and entry widgets
    label_student_name = tk.Label(root, text="Student Name:")
    label_student_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_student_name = tk.Entry(root)
    entry_student_name.grid(row=0, column=1, padx=10, pady=10)

    label_course = tk.Label(root, text="Course:")
    label_course.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_course = tk.Entry(root)
    entry_course.grid(row=1, column=1, padx=10, pady=10)

    label_amount = tk.Label(root, text="Amount:")
    label_amount.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=2, column=1, padx=10, pady=10)

    # Create a button to generate the fee voucher
    generate_button = tk.Button(root, text="Generate Voucher", command=generate_fee_voucher)
    generate_button.grid(row=3, column=0, columnspan=2, pady=20)



# Create the main window
root = tk.Tk()
root.title("Fee Voucher for IUB")
root.iconbitmap('apple.ico')
root.geometry('500x500')
# root.config(background='gray')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# main page 

l=tk.Label(root, text='WELCOME TO IUB PORTAL FOR FEE VOUCHER',).grid(row=0,column=1,padx=10,pady=10)















# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Admition Voucher", command=Admition_Voucher)
file_menu.add_command(label="Semester voucher", command=Semester_Voucher)
file_menu.add_command(label="Rapeat Course Voucher", command=Repeat_course)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create Edit menu


# Run the main loop




root.mainloop()