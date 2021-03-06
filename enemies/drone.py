import enemies.enemy
import ship_components.ship_component_laser as smsp
from constants import Resources


class Drone(enemies.enemy.Enemy):
    def __init__(self, x, y):
        super(Drone, self).__init__(x, y, Resources.Image_Ship_Module_Enemy)

        self.base_health = 20

        # just add 1 simple phaser in front of the ship :)
        laser = smsp.ShipComponentLaser(-2, 0, self, smsp.LaserType.SimpleLaser)
        self.upgrade(laser)
