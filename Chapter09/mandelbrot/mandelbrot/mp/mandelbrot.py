"""
Program for producing a Mandelbrot fractal set using parallel computation via PyMP

"""

# mandelbrot_mp.py
import sys
from PIL import Image
import pymp
import argparse

def mandelbrot_calc_row(y, w, h, image_rows, max_iteration = 1000):
    """ Calculate one row of the mandelbrot set with size wxh """
    
    y0 = y * (2/float(h)) - 1 # rescale to -1 to 1

    for x in range(w):
        x0 = x * (3.5/float(w)) - 2.5 # rescale to -2.5 to 1
    
        i, z = 0, 0 + 0j
        c = complex(x0, y0)
        while abs(z) < 2 and i < max_iteration:
            z = z**2 + c
            i += 1

        color = (i % 8 * 32, i % 16 * 16, i % 32 * 8)
        image_rows[y*w + x] = color
        
def mandelbrot_calc_set(w, h, max_iteration=10000, output='mandelbrot_mp.png'):
    """ Calculate a mandelbrot set given the width, height and
    maximum number of iterations """

    image = Image.new("RGB", (w, h))
    image_rows = pymp.shared.dict()
    
    with pymp.Parallel(4) as p:
        for y in p.range(0, h):
            mandelbrot_calc_row(y, w, h, image_rows, max_iteration)

    for i in range(w*h):
        x,y = i % w, i // w
        image.putpixel((x,y), image_rows[i])
            
    image.save(output, "PNG")
    print('Saved to',output)

def main():
    parser = argparse.ArgumentParser(prog='mandelbrot', description='Mandelbrot fractal generator (parallel version)')
    parser.add_argument('-W','--width',help='Width of the image',type=int, default=640)
    parser.add_argument('-H','--height',help='Height of the image',type=int, default=480) 
    parser.add_argument('-n','--niter',help='Number of iterations',type=int, default=1000)
    parser.add_argument('-o','--output',help='Name of output image file',default='mandelbrot_mp.png')
    
    args = parser.parse_args()
    print('Creating mandelbrot set with size %(width)sx%(height)s, #iterations=%(niter)s' % args.__dict__)
    mandelbrot_calc_set(args.width, args.height, max_iteration=args.niter, output=args.output) 

    
if __name__ == "__main__":
    main()
