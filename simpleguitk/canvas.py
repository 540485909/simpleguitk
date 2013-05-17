import Tkinter

from .timers import create_timer


class Canvas(object):
    Fps = 30
    IntervalMs = 1000 // Fps

    def __init__(self, master, width, height):
        self._canvas = Tkinter.Canvas(master, width=width, height=height,
                                      background='black')
        self._canvas.grid(row=0, column=1, rowspan=2)

        self._draw_handler_fn = None
        self._draw_handler_timer = None

    def _draw_handler(self):
        self._canvas.delete('all')
        if self._draw_handler_fn is not None:
            self._draw_handler_fn(self)

    def destroy(self):
        self._draw_handler_fn = None
        self._draw_handler_timer.stop()

    def set_background(self, color):
        self._canvas.config(background=color)

    def set_draw_handler(self, draw_handler):
        self._draw_handler_fn = draw_handler
        self._draw_handler_timer = create_timer(Canvas.IntervalMs,
                                                self._draw_handler)
        self._draw_handler_timer.start()

    def draw_text(self, text, point, font_size, font_color, font_face='serif'):
        self._canvas.create_text(point, text=text, fill=font_color,
                                 font=(font_face, font_size),
                                 anchor=Tkinter.SW)

    def draw_line(self, point1, point2, line_width, line_color):
        self._canvas.create_line(point1[0], point1[1], point2[0], point2[1],
                                 width=line_width, fill=line_color)

    def draw_polygon(self, point_list, line_width, line_color,
                     fill_color=None):
        points = [y for x in point_list for y in x]
        self._canvas.create_polygon(*points, width=line_width, fill=fill_color,
                                    outline=line_color)

    def draw_circle(self, center_point, radius, line_width, line_color,
                    fill_color=None):
        points = [(center_point[0] - radius), (center_point[1] - radius),
                  (center_point[0] + radius), (center_point[1] + radius)]
        self._canvas.create_oval(points, outline=line_color, fill=fill_color,
                                 width=line_width)
