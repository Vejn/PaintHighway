from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image

class Cars(Widget):
    # Numeric attributes
    GAP_SIZE = NumericProperty(60)
    CAR_SIZE = NumericProperty(50)
    road_center = NumericProperty(0)
    bottom_body_position = NumericProperty(0)
    top_body_position = NumericProperty(0)

    # texture
    car_body_texture = ObjectProperty(None)
    truck_body_texture = ObjectProperty(None)
    suv_body_texture = ObjectProperty(None)
    truck_two_texture = ObjectProperty(None)
    car_three_texture = ObjectProperty(None)
    truck_three_texture = ObjectProperty(None)
    suv_two_texture = ObjectProperty(None)
    suv_one_texture = ObjectProperty(None)
    car_four_texture = ObjectProperty(None)
    lower_car_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))
    top_car_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.car_body_texture = Image(source="car_one.png").texture
        self.car_body_texture.wrap = 'repeat'
        self.truck_body_texture = Image(source="truck_one.png").texture
        self.truck_body_texture.wrap = "repeat"
        self.suv_body_texture = Image(source="car_two.png").texture
        self.suv_body_texture.wrap = "repeat"
        self.truck_two_texture = Image(source="truck_two.png").texture
        self.truck_two_texture.wrap = "repeat"
        self.car_three_texture = Image(source="car_three.png").texture
        self.car_three_texture.wrap = "repeat"
        self.truck_three_texture = Image(source="truck_three.png").texture
        self.truck_three_texture.wrap = "repeat"
        self.suv_two_texture = Image(source="suv_two.png").texture
        self.suv_two_texture.wrap = "repeat"
        self.suv_one_texture = Image(source="suv_one.png").texture
        self.suv_one_texture.wrap = "repeat"
        self.car_four_texture = Image(source="suv_two.png").texture
        self.car_four_texture.wrap = "repeat"

