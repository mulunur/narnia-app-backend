def getHueColorName(hue):
    match hue:
        case hue if 0<= hue <= 15:
            return 'red'
        case hue if 16<= hue <= 40:
            return 'orange'
        case hue if 41<= hue <= 70:
            return 'yellow'
        case hue if 71<= hue <= 160:
            return 'green'
        case hue if 161<= hue <= 200:
            return 'blue'
        case hue if 201<= hue <= 260:
            return 'dark_blue'
        case hue if 261<= hue <= 290:
            return 'violet'
        case hue if 291<= hue <= 340:
            return 'pink'
        case hue if 341<= hue <= 360:
            return 'red'
        case _:
            return ''
        
def getSaturationName(sat):
    match sat:
        case sat if 0<= sat <=50:
            return 'muted'
        case sat if 51<= sat <=100:
            return 'saturated'
        
        
def getLightnessName(light):
    match light:
        case sat if 0<= sat <=33:
            return 'dark'
        case sat if 33<= sat <=66:
            return 'normal'
        case sat if 66<= sat <= 100:
            return 'light'
        