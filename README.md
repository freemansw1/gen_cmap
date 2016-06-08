# gen_cmap
Generates a new color map in the color.gs style for matplotlib.

Usage: 
```
import gen_cmap
#generates a color map from red->green->blue and calls it test1
gen_cmap.lin_cmap_gen(['red', 'green', 'blue'], "test1")

#generates a color map with the given rgb values and calls it test2
gen_cmap.lin_cmap_gen([(255,255,255), (0,0,255), (0,255,0), (255,0,0)], "test2")

```

Color values: http://kodama.fubuki.info/wiki/wiki.cgi/GrADS/script/color.gs?lang=en 
