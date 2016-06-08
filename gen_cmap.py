import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def get_rgb(color):
    if color == 'black': return (0.0,0.0,0.0)
    if color == 'navy': return (0.0,0.0,0.501960784314)
    if color == 'darkblue': return (0.0,0.0,0.545098039216)
    if color == 'mediumblue': return (0.0,0.0,0.803921568627)
    if color == 'blue': return (0.0,0.0,1.0)
    if color == 'darkgreen': return (0.0,0.392156862745,0.0)
    if color == 'green': return (0.0,0.501960784314,0.0)
    if color == 'teal': return (0.0,0.501960784314,0.501960784314)
    if color == 'darkcyan': return (0.0,0.545098039216,0.545098039216)
    if color == 'deepskyblue': return (0.0,0.749019607843,1.0)
    if color == 'darkturquoise': return (0.0,0.807843137255,0.819607843137)
    if color == 'mediumspringgreen': return (0.0,0.980392156863,0.603921568627)
    if color == 'lime': return (0.0,1.0,0.0)
    if color == 'springgreen': return (0.0,1.0,0.498039215686)
    if color == 'aqua': return (0.0,1.0,1.0)
    if color == 'cyan': return (0.0,1.0,1.0)
    if color == 'midnightblue': return (0.0980392156863,0.0980392156863,0.439215686275)
    if color == 'dodgerblue': return (0.117647058824,0.564705882353,1.0)
    if color == 'lightseagreen': return (0.125490196078,0.698039215686,0.666666666667)
    if color == 'forestgreen': return (0.133333333333,0.545098039216,0.133333333333)
    if color == 'seagreen': return (0.180392156863,0.545098039216,0.341176470588)
    if color == 'darkslategray': return (0.18431372549,0.309803921569,0.309803921569)
    if color == 'limegreen': return (0.196078431373,0.803921568627,0.196078431373)
    if color == 'mediumseagreen': return (0.235294117647,0.701960784314,0.443137254902)
    if color == 'turquoise': return (0.250980392157,0.878431372549,0.81568627451)
    if color == 'royalblue': return (0.254901960784,0.411764705882,0.882352941176)
    if color == 'steelblue': return (0.274509803922,0.509803921569,0.705882352941)
    if color == 'darkslateblue': return (0.282352941176,0.239215686275,0.545098039216)
    if color == 'mediumturquoise': return (0.282352941176,0.819607843137,0.8)
    if color == 'indigo': return (0.294117647059,0.0,0.509803921569)
    if color == 'darkolivegreen': return (0.333333333333,0.419607843137,0.18431372549)
    if color == 'cadetblue': return (0.372549019608,0.619607843137,0.627450980392)
    if color == 'cornflowerblue': return (0.392156862745,0.58431372549,0.929411764706)
    if color == 'mediumaquamarine': return (0.4,0.803921568627,0.666666666667)
    if color == 'dimgray': return (0.411764705882,0.411764705882,0.411764705882)
    if color == 'slateblue': return (0.41568627451,0.352941176471,0.803921568627)
    if color == 'olivedrab': return (0.419607843137,0.556862745098,0.137254901961)
    if color == 'slategray': return (0.439215686275,0.501960784314,0.564705882353)
    if color == 'lightslategray': return (0.466666666667,0.533333333333,0.6)
    if color == 'mediumslateblue': return (0.482352941176,0.407843137255,0.933333333333)
    if color == 'lawngreen': return (0.486274509804,0.988235294118,0.0)
    if color == 'chartreuse': return (0.498039215686,1.0,0.0)
    if color == 'aquamarine': return (0.498039215686,1.0,0.83137254902)
    if color == 'maroon': return (0.501960784314,0.0,0.0)
    if color == 'purple': return (0.501960784314,0.0,0.501960784314)
    if color == 'olive': return (0.501960784314,0.501960784314,0.0)
    if color == 'gray': return (0.501960784314,0.501960784314,0.501960784314)
    if color == 'skyblue': return (0.529411764706,0.807843137255,0.921568627451)
    if color == 'lightskyblue': return (0.529411764706,0.807843137255,0.980392156863)
    if color == 'blueviolet': return (0.541176470588,0.16862745098,0.886274509804)
    if color == 'darkred': return (0.545098039216,0.0,0.0)
    if color == 'darkmagenta': return (0.545098039216,0.0,0.545098039216)
    if color == 'saddlebrown': return (0.545098039216,0.270588235294,0.0745098039216)
    if color == 'darkseagreen': return (0.560784313725,0.737254901961,0.560784313725)
    if color == 'lightgreen': return (0.564705882353,0.933333333333,0.564705882353)
    if color == 'mediumpurple': return (0.576470588235,0.439215686275,0.858823529412)
    if color == 'darkviolet': return (0.580392156863,0.0,0.827450980392)
    if color == 'palegreen': return (0.596078431373,0.98431372549,0.596078431373)
    if color == 'darkorchid': return (0.6,0.196078431373,0.8)
    if color == 'yellowgreen': return (0.603921568627,0.803921568627,0.196078431373)
    if color == 'sienna': return (0.627450980392,0.321568627451,0.176470588235)
    if color == 'brown': return (0.647058823529,0.164705882353,0.164705882353)
    if color == 'darkgray': return (0.662745098039,0.662745098039,0.662745098039)
    if color == 'lightblue': return (0.678431372549,0.847058823529,0.901960784314)
    if color == 'greenyellow': return (0.678431372549,1.0,0.18431372549)
    if color == 'paleturquoise': return (0.686274509804,0.933333333333,0.933333333333)
    if color == 'lightsteelblue': return (0.690196078431,0.76862745098,0.870588235294)
    if color == 'powderblue': return (0.690196078431,0.878431372549,0.901960784314)
    if color == 'firebrick': return (0.698039215686,0.133333333333,0.133333333333)
    if color == 'darkgoldenrod': return (0.721568627451,0.525490196078,0.043137254902)
    if color == 'mediumorchid': return (0.729411764706,0.333333333333,0.827450980392)
    if color == 'rosybrown': return (0.737254901961,0.560784313725,0.560784313725)
    if color == 'darkkhaki': return (0.741176470588,0.717647058824,0.419607843137)
    if color == 'silver': return (0.752941176471,0.752941176471,0.752941176471)
    if color == 'mediumvioletred': return (0.780392156863,0.0823529411765,0.521568627451)
    if color == 'indianred': return (0.803921568627,0.360784313725,0.360784313725)
    if color == 'peru': return (0.803921568627,0.521568627451,0.247058823529)
    if color == 'chocolate': return (0.823529411765,0.411764705882,0.117647058824)
    if color == 'tan': return (0.823529411765,0.705882352941,0.549019607843)
    if color == 'lightgray': return (0.827450980392,0.827450980392,0.827450980392)
    if color == 'thistle': return (0.847058823529,0.749019607843,0.847058823529)
    if color == 'orchid': return (0.854901960784,0.439215686275,0.839215686275)
    if color == 'goldenrod': return (0.854901960784,0.647058823529,0.125490196078)
    if color == 'palevioletred': return (0.858823529412,0.439215686275,0.576470588235)
    if color == 'crimson': return (0.862745098039,0.078431372549,0.235294117647)
    if color == 'gainsboro': return (0.862745098039,0.862745098039,0.862745098039)
    if color == 'plum': return (0.866666666667,0.627450980392,0.866666666667)
    if color == 'burlywood': return (0.870588235294,0.721568627451,0.529411764706)
    if color == 'lightcyan': return (0.878431372549,1.0,1.0)
    if color == 'lavender': return (0.901960784314,0.901960784314,0.980392156863)
    if color == 'darksalmon': return (0.913725490196,0.588235294118,0.478431372549)
    if color == 'violet': return (0.933333333333,0.509803921569,0.933333333333)
    if color == 'palegoldenrod': return (0.933333333333,0.909803921569,0.666666666667)
    if color == 'lightcoral': return (0.941176470588,0.501960784314,0.501960784314)
    if color == 'khaki': return (0.941176470588,0.901960784314,0.549019607843)
    if color == 'aliceblue': return (0.941176470588,0.972549019608,1.0)
    if color == 'honeydew': return (0.941176470588,1.0,0.941176470588)
    if color == 'azure': return (0.941176470588,1.0,1.0)
    if color == 'sandybrown': return (0.956862745098,0.643137254902,0.376470588235)
    if color == 'wheat': return (0.960784313725,0.870588235294,0.701960784314)
    if color == 'beige': return (0.960784313725,0.960784313725,0.862745098039)
    if color == 'whitesmoke': return (0.960784313725,0.960784313725,0.960784313725)
    if color == 'mintcream': return (0.960784313725,1.0,0.980392156863)
    if color == 'ghostwhite': return (0.972549019608,0.972549019608,1.0)
    if color == 'salmon': return (0.980392156863,0.501960784314,0.447058823529)
    if color == 'antiquewhite': return (0.980392156863,0.921568627451,0.843137254902)
    if color == 'linen': return (0.980392156863,0.941176470588,0.901960784314)
    if color == 'lightgoldenrodyellow': return (0.980392156863,0.980392156863,0.823529411765)
    if color == 'oldlace': return (0.992156862745,0.960784313725,0.901960784314)
    if color == 'red': return (1.0,0.0,0.0)
    if color == 'fuchsia': return (1.0,0.0,1.0)
    if color == 'magenta': return (1.0,0.0,1.0)
    if color == 'deeppink': return (1.0,0.078431372549,0.576470588235)
    if color == 'orangered': return (1.0,0.270588235294,0.0)
    if color == 'tomato': return (1.0,0.388235294118,0.278431372549)
    if color == 'hotpink': return (1.0,0.411764705882,0.705882352941)
    if color == 'coral': return (1.0,0.498039215686,0.313725490196)
    if color == 'darkorange': return (1.0,0.549019607843,0.0)
    if color == 'lightsalmon': return (1.0,0.627450980392,0.478431372549)
    if color == 'orange': return (1.0,0.647058823529,0.0)
    if color == 'lightpink': return (1.0,0.713725490196,0.756862745098)
    if color == 'pink': return (1.0,0.752941176471,0.796078431373)
    if color == 'gold': return (1.0,0.843137254902,0.0)
    if color == 'peachpuff': return (1.0,0.854901960784,0.725490196078)
    if color == 'navajowhite': return (1.0,0.870588235294,0.678431372549)
    if color == 'moccasin': return (1.0,0.894117647059,0.709803921569)
    if color == 'bisque': return (1.0,0.894117647059,0.76862745098)
    if color == 'mistyrose': return (1.0,0.894117647059,0.882352941176)
    if color == 'blanchedalmond': return (1.0,0.921568627451,0.803921568627)
    if color == 'papayawhip': return (1.0,0.937254901961,0.835294117647)
    if color == 'lavenderblush': return (1.0,0.941176470588,0.960784313725)
    if color == 'seashell': return (1.0,0.960784313725,0.933333333333)
    if color == 'cornsilk': return (1.0,0.972549019608,0.862745098039)
    if color == 'lemonchiffon': return (1.0,0.980392156863,0.803921568627)
    if color == 'floralwhite': return (1.0,0.980392156863,0.941176470588)
    if color == 'snow': return (1.0,0.980392156863,0.980392156863)
    if color == 'yellow': return (1.0,1.0,0.0)
    if color == 'lightyellow': return (1.0,1.0,0.878431372549)
    if color == 'ivory': return (1.0,1.0,0.941176470588)
    if color == 'white': return (1.0,1.0,1.0)


def convert_color(color):
    '''
    Converts a color from 0-255 to 0-1
    '''
    return (color[0]/255, color[1]/255, color[2]/255)

def lin_cmap_gen(incolgs, regname, fractions = None):
    '''
    Generates a color map with the given color list (incolgs).
    Accepts a list of color words (defined by the color.gs script:
        http://kodama.fubuki.info/wiki/wiki.cgi/GrADS/script/color.gs?lang=en)
    or a list of (r,g,b) values. The r,g,b values can be either 0<=x<=1 or 0<=x<=255

    input:
        incolgs: Input color map request
        regname: Name for matplotlib to register color map.
        fractions: Fraction for each color to take up- these values must
                   add to 1. If not, a ValueException is raised. (NOT YET IMPLEMENTED)

    returns:
        a LinearSegmentedColormap containing your colors.
    '''
    collists = incolgs
    reds = list()
    greens = list()
    blues = list()
    reds_prep = list()
    greens_prep = list()
    blues_prep = list()

    if fractions != None:
        raise NotImplementedError("Fractional colors are not yet implemented.")

    for i, color in enumerate(collists):
        try:
            if (color[0] >= 0 and color[0] <= 255 and
                color[1] >= 0 and color[1] <= 255 and
                color[2] >= 0 and color[2] <= 255):

                rgb = convert_color(color)
            else:
                raise ValueError("Colors need to be between 0 and 255")

        except TypeError:
            rgb = get_rgb(color)

        reds.append(rgb[0])
        greens.append(rgb[1])
        blues.append(rgb[2])
    for i in range(len(reds)):
        rp = ((float(i)/(len(reds)-1)))
        drp = ((1.0/(len(reds)-1)))
        if rp+drp >=1:
            drp = 0
        reds_prep.append((rp, reds[i],reds[i]))
        blues_prep.append((rp, blues[i], blues[i]))
        greens_prep.append((rp, greens[i], greens[i]))

    cdict = {'red': tuple(reds_prep), 'blue': tuple(blues_prep), 
             'green': tuple(greens_prep)}
    #print(cdict)
    ucmap = LinearSegmentedColormap(regname, cdict)
    plt.register_cmap(cmap=ucmap)
    return ucmap




