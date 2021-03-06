# -*- coding: utf-8 -*-
accent_map = {'â': '^a', 'ê': '^e', 'î': '^i', 'ô': '^o', 'û': '^u', 'Â': '^A', 'Ê': '^E', 'Î': '^I', 'Ô': '^O',
              'Û': '^U', }
accent_map2 = {'ë': '¨e', 'ï': '¨i', 'ü': '¨u', 'ÿ': '¨y', 'Ë': '¨E', 'Ï': '¨I', 'Ü': '¨U', 'Ÿ': '¨Y'}

kbrd_keys = [[0, 0, 25, 22, "", "²", "", "", "", "", 0],  # 0
             [30, 0, 25, 22, "1", "&", "", "", "", "", 0],
             [60, 0, 25, 22, "2", 'é', "", "", "", "~", 1],
             [90, 0, 25, 22, "3", '"', "", "", "", "#", 2],
             [120, 0, 25, 22, "4", "'", "", "", "", "{", 3],
             [150, 0, 25, 22, "5", "(", "", "", "", "[", 3],
             [180, 0, 25, 22, "6", "-", "", "", "", "|", 4],
             [210, 0, 25, 22, "7", "è", "", "", "", "`", 4],
             [240, 0, 25, 22, "8", "_", "", "", "", "\\", 5],
             [270, 0, 25, 22, "9", "ç", "", "", "", "^", 6],
             [300, 0, 25, 22, "0", "à", "", "", "", "@", 7],
             [330, 0, 25, 22, "°", ")", "", "", "", "]", 7],
             [360, 0, 25, 22, "+", "=", "", "", "", "}", 7],
             [390, 0, 0, 0, "", "", "", "", "", "", 7],
             [390, 0, 55, 22, "", "", "", "←", "Suppr ", "arrière ", 7],  # 14

             [0, 27, 43, 22, "", "", "Tab", "", "", "", 0],  # 15
             [48, 27, 25, 22, "", "", "", "A", "", "æ", 0],
             [78, 27, 25, 22, "", "", "", "Z", "", "", 1],
             [108, 27, 25, 22, "", "", "", "E", "", "€", 2],
             [138, 27, 25, 22, "", "", "", "R", "", "", 3],
             [168, 27, 25, 22, "", "", "", "T", "", "", 3],
             [198, 27, 25, 22, "", "", "", "Y", "", "", 4],
             [228, 27, 25, 22, "", "", "", "U", "", "", 4],
             [258, 27, 25, 22, "", "", "", "I", "", "", 5],
             [288, 27, 25, 22, "", "", "", "O", "", "", 6],
             [318, 27, 25, 22, "", "", "", "P", "", "", 7],
             [348, 27, 25, 22, "¨", "^", "", "", "", "", 7],
             [378, 27, 25, 22, "£", "$", "", "", "", "¤", 7],
             [408, 27, 37, 22, "", "", "Entrée", "", "", "", 7],  # 28

             [0, 54, 50, 22, "", "", "Verr Maj", "", "", "", 0],  # 29
             [55, 54, 25, 22, "", "", "", "Q", "", "", 0],
             [85, 54, 25, 22, "", "", "", "S", "", "", 1],
             [115, 54, 25, 22, "", "", "", "D", "", "", 2],
             [145, 54, 25, 22, "", "", "", "F", "", "", 3],
             [175, 54, 25, 22, "", "", "", "G", "", "", 3],
             [205, 54, 25, 22, "", "", "", "H", "", "", 4],
             [235, 54, 25, 22, "", "", "", "J", "", "", 4],
             [265, 54, 25, 22, "", "", "", "K", "", "", 5],
             [295, 54, 25, 22, "", "", "", "L", "", "", 6],
             [325, 54, 25, 22, "", "", "", "M", "", "", 7],
             [355, 54, 25, 22, '%', "ù", "", "", "", "", 7],
             [385, 54, 25, 22, "µ", "*", "", "", "", "", 7],
             [415, 48, 30, 28, "", "", "", "", "", "", 7],  # 42

             [0, 81, 60, 22, "", "", "Maj", "", "", "", 0],  # 43
             [65, 81, 25, 22, ">", "<", "", "", "", "", 0],
             [95, 81, 25, 22, "", "", "", "W", "", "", 1],
             [125, 81, 25, 22, "", "", "", "X", "", "", 2],
             [155, 81, 25, 22, "", "", "", "C", "", "", 3],
             [185, 81, 25, 22, "", "", "", "V", "", "", 3],
             [215, 81, 25, 22, "", "", "", "B", "", "", 4],
             [245, 81, 25, 22, "", "", "", "N", "", "", 4],
             [275, 81, 25, 22, "?", ",", "", "", "", "", 5],
             [305, 81, 25, 22, ".", ";", "", "", "", "", 6],
             [335, 81, 25, 22, "/", ":", "", "", "", "", 7],
             [365, 81, 25, 22, "§", "!", "", "", "", "", 7],
             [395, 81, 50, 22, "", "", "Maj", "", "", "", 7],  # 55

             [0, 108, 33, 22, "", "", "Ctrl", "", "", "", 9],  # 56
             [38, 108, 25, 22, "", "", "", "", "", "", 9],
             [68, 108, 25, 22, "", "", "Alt", "", "", "", 9],
             [98, 108, 214, 22, "", "", "Space", "", "", "", 8],
             [317, 108, 25, 22, "", "", "Alt Gr", "", "", "", 8],
             [347, 108, 25, 22, "", "", "", "", "", "", 9],
             [377, 108, 25, 22, "", "", "", "", "", "", 9],
             [407, 108, 38, 22, "", "", "Ctrl", "", "", "", 9],  # 63

             # Hand
             [100, 178, 16, 17, "", "", "", "", "", "", 0],  # 64 x+17
             [122, 151, 17, 19, "", "", "", "", "", "", 1],  # x+4 w-8  x+2 y+2
             [143, 135, 18, 19, "", "", "", "", "", "", 2],  # x y+2
             [169, 140, 16, 18, "", "", "", "", "", "", 3],  # x-1 y+3

             [261, 140, 16, 18, "", "", "", "", "", "", 4],
             [285, 135, 18, 19, "", "", "", "", "", "", 5],
             [307, 151, 17, 19, "", "", "", "", "", "", 6],
             [330, 178, 16, 17, "", "", "", "", "", "", 7],  # 71

             [203, 186, 18, 20, "", "", "", "", "", "", 8],  # Lt Thumb - Space - 72
             [225, 186, 18, 20, "", "", "", "", "", "", 8]]  # Rt Thumb - Alt Gr - 73
