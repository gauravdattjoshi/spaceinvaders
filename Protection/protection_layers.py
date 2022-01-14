from Protection.protection_box import ProtectionBox


class ProtectionLayer():
    def __init__(self):
        self.protection_box_list = []
        self.create_protection_layer()

    def create_protection_layer(self):
        run_loop = True
        starting_x, starting_y, count = 380, 200, 0

        while run_loop:
            box = ProtectionBox()
            box.goto(starting_x, starting_y)
            starting_x -= 60
            if starting_x < -360:
                count += 1
                starting_y -= 40
                starting_x = 380
            if count>=7:
                run_loop = False
            box.showturtle()
            self.protection_box_list.append(box)


