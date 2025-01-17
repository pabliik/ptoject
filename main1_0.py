import tkinter as tk
import numpy as np
from random import randint


def create_slider(window, from_value: int, to_value: int, label: str, resolution: float, command, length: float, set_value: float, row:int, column:int ):
    slider = tk.Scale(window,label=label, from_= from_value, to= to_value, orient=tk.HORIZONTAL, resolution= resolution, command=command, length=length)
    slider.set(set_value)
    slider.grid(row=row, column= column, padx=10 , pady=10)

    return slider

def start():
    def exit_app(window):
        window.destroy()

    def centrum_window(window,title: str, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        window.title(title)
        window.resizable(False,False)
        return window

    def restart(window):
        window.destroy()
        start()

    def draw_tree(x, y, length, angle, canvas, iteration, branch_angle , length_ratio: float ,tag, first_iter = True,):
        if iteration == 0:
            return
        
        current_angle = 90 if first_iter else angle
        colour = "brown" if first_iter else "green"

        x_end = x + length * np.cos(np.radians(current_angle))
        y_end = y - length * np.sin(np.radians(current_angle))

        canvas.create_line(x, y, x_end, y_end,width = 3, fill=colour , tags=tag)
    
        draw_tree(x_end, y_end, length * length_ratio, angle + branch_angle, canvas, iteration-1, branch_angle, length_ratio,tag, first_iter= False)
        draw_tree(x_end, y_end, length * length_ratio, angle - branch_angle, canvas, iteration-1, branch_angle, length_ratio,tag, first_iter= False)


    def update_tree():
        # Clear the previous tree
        canvas.delete("updated")
        
        # Get slider values
        length = length_slider.get()
        angle = angle_slider.get()
        iterations = iteration_slider.get()
        branch_angle = branch_angle_slider.get()  # Get angle between branches value
        lengthRatio = length_ratio_slider.get()
        
        # Draw the updated tree
        draw_tree(800, 500, length, angle, canvas, iterations, branch_angle, lengthRatio, tag="updated", first_iter=True,)
        check_match()

    def check_match():
        # try:
        #     # I think we can even assume this is always in globals.
        #     # We can only check if the window object is not destroyed by checking if accessing it causes errors.
        #     if 'congrat_win' in globals() and congrat_win.winfo_exists():
        #         congrat_win.destroy()
        # except tk.TclError:
        #     pass

        tolerance = {
            'length' : 2,
            'angle' : 2,
            'iteration': 0,
            'branch_angle' : 2,
            'length_ratio' : 0.02
        }
       
        diff = {
            'length' : abs(random_params['length'] - length_slider.get()),
            'angle' : abs(random_params['angle'] - angle_slider.get()),
            'iteration': abs(random_params['iteration'] - iteration_slider.get()),
            'branch_angle' : abs(random_params['branch_angle'] - branch_angle_slider.get()),
            'length_ratio' : abs(random_params['length_ratio'] - length_ratio_slider.get())
        }

        if all(diff[key] <= tolerance[key] for key in tolerance):
            for slider in [length_slider, angle_slider, iteration_slider, branch_angle_slider, length_ratio_slider]:
                slider.config(state=tk.DISABLED)
                # slider.config(bg = 'green', fg = 'green ')
            # if 'congrat_win' in globals():
            #     congrat_win.destroy()
            show_congratulations()
        

    def show_congratulations():
        # global congrat_win
        congrat_win = tk.Toplevel(win)
        centrum_window(congrat_win, "Congratulations", 300 , 300)
        congrat_label1 = tk.Label(congrat_win, bg='black')
        restart_button = tk.Button(congrat_label1, text="Restart", command= lambda: restart(win))
        congrat_label = tk.Label(congrat_win, text="Congratulations! \n "
                                'You\'ve matched the random tree!', font=("Arial", 14))
        exit_button = tk.Button(congrat_label1, text='Exit' , command= lambda: exit_app(win))

        congrat_label.pack(padx=10, pady=10)
        congrat_label1.pack(padx=10,pady=10)
        restart_button.pack(padx=10, pady=10)
        exit_button.pack(padx=10 , pady=10)

    def generate_random_tree():
        global random_params
        random_params = {
            'x': 300,
            'y': 500,
            'length': randint(80, 180),
            'angle': randint(0, 180),
            'canvas': canvas,
            'iteration': randint(3, 6),
            'branch_angle': randint(10, 90),
            'length_ratio': randint(1, 100) / 100
        }
        print(random_params)
        draw_tree(**random_params, first_iter=True , tag="random" ,)

    win = tk.Tk()
    win.config(bg='grey')
    width_win = 1200 
    centrum_window(win, "Matching Game" , width_win, 800)   
    #canvas = tk.Canvas(win, bg='green', width=1000, height=600)
    canvas = tk.Canvas(win, bg='#e0f7da', width=width_win, height=500)  # Pale green background

    ScalesLabel = tk.LabelFrame(win, text="Adjust Tree Parameters", font=("Arial", 14), padx=10, pady=10)

    # Create sliders for controlling the tree's parameters
    length_slider = create_slider(ScalesLabel,50,200,"Initial Branch Length", 1, lambda e: update_tree(),200, 100, 0 , 0)
    angle_slider = create_slider(ScalesLabel, 0 , 180, "Branch Angle", 1, lambda e: update_tree(), 200, 45, 0,1)
    iteration_slider = create_slider(ScalesLabel, 1,10,"Iterations", 1, lambda e: update_tree(), 200, 6,0,2)
    # Add a slider for controlling the angle between the branches
    branch_angle_slider = create_slider(ScalesLabel, 0, 90, "Angle Between Branches", 1, lambda e: update_tree(), 200, 30,0,3)
    length_ratio_slider = create_slider(ScalesLabel, 0.01,1,'Length Ratio', 0.01, lambda e: update_tree(), 200, 0.7, 0 ,4)
    
    generate_random_tree()
    update_tree()

    canvas.pack(padx=10, pady=1)
    ScalesLabel.pack(padx=1, pady=10)
    win.mainloop()

start()