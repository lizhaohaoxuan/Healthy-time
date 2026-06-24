class config:
    def __init__(self):
        try :
            with open(r'../.config', 'r'):
                pass
        except:
            with open(r'../.config', 'x'):
                pass
    
    def read_config(self) -> list:
        '''
        Read the entire config and return it as a list
        '''
        config_list = []
        with open(r'../.config', 'r', encoding='utf-8') as f:
            lines_num = len(f.readlines())
            for i in range(lines_num):
                config_list.append(f.readline().strip())
        return config_list
    def write_config(self, config_list:list=[]):
        '''
        Write the entire config
        '''
        with open(r'../.config', 'w', encoding='utf-8') as f:
            for line in config_list:
                f.write(line + '\n')
    def add_config(self, text:str):
        '''
        Append a new line to the config
        '''
        with open(r'../.config', 'a', encoding='utf-8') as f:
            f.write(text + '\n')
    def delete_config(self, line_num:int):
        '''
        Delete a line from the config
        '''
        config_list = self.read_config()
        if 0 <= line_num < len(config_list):
            del config_list[line_num]
            self.write_config(config_list)
        elif type(line_num) is not int:
            raise TypeError('line_num must be an integer')