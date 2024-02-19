
class Shooter:
    def __init__(self):
        self.gun_name = None
        self.bullet_count = None

    def set_gun_by_name(self, name: str) -> None:
        guns = ['Submachine Gun', 'Assault Rifle', 'Pistol', 'Shotgun', 'Sniper Rifle']

        if name not in guns:
            raise Exception(f"The gun is not in box: {name}")
        else:
            self.gun_name = name

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:

        global gun_bullet_size

        if self.gun_name is None:
            raise Exception("No gun selected.")

        gun_bullet_size = {
            'Submachine Gun': 0.5,
            'Assault Rifle': 1,
            'Pistol': 0.5,
            'Shotgun': 4,
            'Sniper Rifle': 3
        }

        if size != gun_bullet_size[self.gun_name]:
            raise Exception("Your gun and bullet size do not match.")

        if count < 1:
            raise Exception("Your bullet count is not set.")

        self.bullet_count = count

    def shoot_to_target(self, target_x: int, target_y: int, target_distance: int, aim_x: int, aim_y: int) -> float:
        if self.gun_name is None:
            raise Exception("No gun selected.")
        gun_distance = {
            'Submachine Gun': 100,
            'Assault Rifle': 200,
            'Pistol': 80,
            'Shotgun': 50,
            'Sniper Rifle': 1000
        }

        if self.gun_name not in gun_distance:
            raise Exception("No gun selected.")

        if self.bullet_count is None or self.bullet_count < 1:
            raise Exception("No bullets available.")

        gun_power = {
                'Submachine Gun': 2,
                'Assault Rifle': 3,
                'Pistol': 1,
                'Shotgun': 4,
                'Sniper Rifle': 5
            }

        bullet_damage = {
                0.5: 1,
                1: 2,
                4: 5,
                3: 4
            }
        if target_distance > gun_distance[self.gun_name]:
            return 0
        else:
            damage = gun_power[self.gun_name] * bullet_damage[gun_bullet_size[self.gun_name]] * aim_x
            return damage
            # damage = gun_power[self.gun_name] * bullet_damage[gun_bullet_size[self.gun_name]] / target_distance
            # return damage




