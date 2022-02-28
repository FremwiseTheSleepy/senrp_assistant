
from OneRing.Confinguration.OneRing import WeaponStructure, WeaponDatabase, GANDALF_FEAT_DIE_VALUE


class Weapon(object):
    """ Weapon initialization and upgrade handling """
    def __init__(self, name, weapon_mods=WeaponStructure(damage=0, edge=0, injury=0, hit_bonus=0)):

        self.name = name
        base_weapon_attributes = WeaponDatabase.get(self.name)

        if base_weapon_attributes:
            self.base_damage, self.base_edge, self.base_injury, self.hit_bonus = base_weapon_attributes
        else:
            print("Selected weapon of name: {}, not yet supported!".format(self.name))
            self.base_damage = 0
            self.base_edge = 0
            self.base_injury = 0
            self.hit_bonus = 0

        self.damage = self.base_damage + weapon_mods.damage
        self.injury = self.base_injury + weapon_mods.injury
        # Edge is subtractive and has a gap between Gandalf and Sauron; handle both +1 and -1 as subtracting 1.
        if self.base_edge == 12 and weapon_mods.edge >= 1:
            weapon_mods.edge = abs(weapon_mods.edge) + 1
        self.edge = self.base_edge - abs(weapon_mods.edge)
        self.hit_bonus += weapon_mods.hit_bonus

    def __str__(self):
        out_text = "   Weapon:\n"
        out_text += "     Name: {},   ".format(self.name)
        out_text += "Damage: {} ({} + {}),   ".format(self.damage, self.base_damage, (self.damage - self.base_damage))
        out_text += "Injury: {} ({} + {}),   ".format(self.injury, self.base_injury, (self.injury - self.base_injury))
        # Edge is subtractive and has a gap between Gandalf and Sauron; output rationale for extra subtraction
        if self.base_edge == GANDALF_FEAT_DIE_VALUE and self.edge != self.base_edge:
            out_text += "Edge: {} (12 - {} - 1*  (*11 not used))   ".format(self.edge, (self.base_edge-self.edge-1))
        else:
            out_text += "Edge: {} ({} - {})   ".format(self.edge, self.base_edge, (self.base_edge - self.edge))
        out_text += "Hit Bonus: {}   ".format(self.hit_bonus)
        out_text += "\n"
        return out_text
