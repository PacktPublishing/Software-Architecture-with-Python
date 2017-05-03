# Code Listing #21

"""

Main mandelbrot program using Celery as the distributed, concurrent task queue

"""
import argparse
from celery import group
from PIL import Image
from mandelbrot_tasks import mandelbrot_calc_row

def mandelbrot_main(w, h, max_iterations=1000, output='mandelbrot_celery.png'):
    """ Main function for mandelbrot program with celery """
    
    job = group([mandelbrot_calc_row.s(y, w, h, max_iterations) for y in range(h)])
    result = job.apply_async()

    image = Image.new('RGB', (w, h))
    
    for image_rows in result.join():
        for k,v in image_rows.items():
            k = int(k)
            v = tuple(map(int, v))
            x,y = k % args.width, k // args.width
            image.putpixel((x,y), v)
            
    image.save(output, 'PNG')
    print('Saved to',output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='mandelbrot', description='Mandelbrot fractal generator (parallel version)')
    parser.add_argument('-W','--width',help='Width of the image',type=int, default=640)
    parser.add_argument('-H','--height',help='Height of the image',type=int, default=480) 
    parser.add_argument('-n','--niter',help='Number of iterations',type=int, default=1000)
    parser.add_argument('-o','--output',help='Name of output image file',default='mandelbrot_celery.png')
    
    args = parser.parse_args()
    print('Creating mandelbrot set with size %(width)sx%(height)s, #iterations=%(niter)s' % args.__dict__)
    mandelbrot_main(args.width, args.height, args.niter, args.output)
