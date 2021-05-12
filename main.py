import sys
import pyautogui

import running_functions, Settings

print('If want to exit, close window directly or press ctrl+c')

try: 
    layout = Settings.LayoutSettings()
    print('Press enter to continue, type "layout" to layout settings')
    procedure = input()
    if procedure == 'layout': 
        print("Choose options: ")
        print("1. Update layout   2. Restore layout   3. Update default")
        while True: 
            choice = input()
            if choice == "1": 
                layout.update_layout()
                break
            elif choice == "2": 
                layout.restore_to_default()
                break
            elif choice == "3": 
                layout.update_default()
                break
            else: 
                print("Please enter 1, 2, or 3")
    
    settings = Settings.Settings()
    log_file = running_functions.LogFile(settings.start_wavelength, settings.end_wavelength, settings.wavelength_step, settings.log_path)
    log_file.init_log()
    click_flag = False
    input("Press enter to start. ")
    while True: 
        if pyautogui.pixelMatchesColor(layout.process_bar[0], layout.process_bar[1], layout.process_color, tolerance = 20): 
            if click_flag == False: 
                click_flag = True
                pyautogui.click(layout.lsm_xy[0], layout.lsm_xy[1])
                log_file.log_image()
        else: 
            click_flag = False
except KeyboardInterrupt: 
    print('exit')
    sys.exit()
