import time, pyautogui

class LogFile(): 
    def __init__(self, start_wavelength, end_wavelength, wavelength_step, path = 'log.txt') -> None:
        '''
        path: string, path for log file
        start_wavelength: string
        end_wavelength: string
        wavelength_step: float
        '''
        self.log_path = path
        self.start_wavelength = start_wavelength
        self.end_wavelength = end_wavelength
        self.wavelength_step = wavelength_step
        self.image_type = "2D"
        self.z_num = 0

    
    def init_log(self): 
        '''
        initialize the log file
        '''
        with open(self.log_path, 'w') as log: 
            log.write(time.strftime("%a, %d %b %Y %H:%M:%S\n"))
            if self.start_wavelength and self.end_wavelength: 
                log.write('Start at '+self.start_wavelength +', end at '+self.end_wavelength+'\n')
            log.write('\n')
    
    def log_image(self, n): 
        '''
        n: int, index of image
        '''
        with open(self.log_path, 'a') as log: 
            log.write(str(n)+'th image at '+time.strftime("%H:%M:%S"))
            if self.image_type == "2D": 
                if self.wavelength_step: 
                    log.write(", at "+str(float(self.start_wavelength)+n*self.wavelength_step))
                log.write("\n\n")
            elif self.image_type == "3D": 
                if self.wavelength_step: 
                    log.write(", " + str(int(n/self.z_num)) + "th z-stack's " + str(n%self.z_num) + "th image, at "+str(float(self.start_wavelength)+int(n/self.z_num)*self.wavelength_step))
                log.write("\n\n")


class ClickLSM(): 
    def __init__(self, layout) -> None:
        self.flag = False
        self.layout = layout
    
    def click(self): 
        if pyautogui.pixelMatchesColor(self.layout.process_bar[0], self.layout.process_bar[1], self.layout.process_color, tolerance = 20): 
            if self.flag == False: 
                self.flag = True
                pyautogui.click(self.layout.lsm_xy[0], self.layout.lsm_xy[1])
        else: 
            self.flag = False


