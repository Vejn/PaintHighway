# Importing needed libraries
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from random import randint
from cars import Cars


class Background(Widget):
    background_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # create texture
        self.background_texture = Image(source="background.png").texture
        self.background_texture.wrap = 'repeat'
        self.background_texture.uvsize = (Window.width / self.background_texture.width, -1)


    # Defining redraw method
    def scroll_textures(self, time_passed):
        # Update the uv position of texture
        self.background_texture.uvpos = \
            ((self.background_texture.uvpos[0] + time_passed/6.0) % Window.width, self.background_texture.uvpos[1])

        # Redraw the texture
        texture = self.property('background_texture')
        texture.dispatch(self)


class Bike(Image):
    velocity = NumericProperty(0)

    def on_touch_down(self, touch):

        self.source = "p3.png"
        self.velocity = 250
        super().on_touch_down(touch)


    def on_touch_up(self, touch):
        self.source = "p3.png"
        self.velocity = -250
        super().on_touch_up(touch)


# Creating app
class MainApp(App):

    collision = False

    def move_bike(self, time_passed):
        bike = self.root.ids.bike
        bike.y = bike.y + bike.velocity * time_passed

        self.check_collision()

    def check_collision(self):
        bike = self.root.ids.bike
        is_collision = False
        for car in self.cars:
            if car.collide_widget(bike):
                is_collision = True
                if bike.y < (car.road_center - 30):
                    self.game_over()

                if bike.y > (car.road_center + car.GAP_SIZE + 20):
                    self.game_over()

        if bike.y < 10:
            self.game_over()

        if bike.top > Window.height:
            self.game_over()

        if self.collision and not is_collision:
            self.root.ids.score.text = str(int(self.root.ids.score.text)+1)
        self.collision = is_collision



    def game_over(self):

        self.root.ids.bike.pos = 20, (self.root.height / 2.0)
        for car in self.cars:
            self.root.remove_widget(car)
        self.frames.cancel()
        self.root.ids.start_button.disabled = False
        self.root.ids.start_button.opacity = 1

    def next_frame(self, time_passed):
        self.move_bike(time_passed)
        self.move_cars(time_passed)
        self.root.ids.background.scroll_textures(time_passed)


    def start_game(self):

        self.root.ids.score.text = "0"
        self.collision = False
        self.frames = Clock.schedule_interval(self.next_frame, 1 / 60.)
        self.cars = []
        # Create the cars
        num_cars = 3
        distance_between_cars = Window.width / (num_cars - 1)
        for i in range(num_cars):
            car = Cars()
            car.road_center = randint(80, self.root.height - 100)
            car.size_hint = (None, None)
            car.pos = (Window.width + i*distance_between_cars, 96)
            car.size = (144, self.root.height - 100)

            self.cars.append(car)
            self.root.add_widget(car)


    def move_cars(self, time_passed):
        # Move cars
        for car in self.cars:
            car.x -= time_passed * 100

        # reposition the car
        num_cars = 3
        distance_between_cars = Window.width / (num_cars - 1)

        car_xs = list(map(lambda car: car.x, self.cars))
        right_most = max(car_xs)
        if right_most <= Window.width - distance_between_cars + 10:
            most_left = self.cars[car_xs.index(min(car_xs))]
            most_left.x = Window.width


if __name__ == "__main__":
    MainApp().run()
