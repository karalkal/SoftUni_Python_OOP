from project.hero import Hero

import unittest


class TestHero(unittest.TestCase):
    def test__all_properties_initialized_correctly(self):
        bay_huy = Hero("Bay Huy", 8, 99.99, 2.6)
        self.assertEqual(bay_huy.username, "Bay Huy")
        self.assertEqual(bay_huy.level, 8)
        self.assertEqual(bay_huy.health, 99.99)
        self.assertEqual(bay_huy.damage, 2.6)

    def test_fight_meth__if_hero_and_enemy_have_same_name__expect_exception(self):
        bay_huy = Hero("Bay Huy", 8, 99.99, 2.6)
        enemy = Hero("Bay Huy", 4, 44, 12)
        with self.assertRaises(Exception) as context:
            bay_huy.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_fight_meth__if_hero_health_is_zero_or_below__expect_exception(self):
        bay_huy = Hero("Bay Huy", 8, 0, 2.6)
        enemy = Hero("Jenata Myj", 4, 44, 12)
        with self.assertRaises(Exception) as context:
            bay_huy.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

        bay_huy = Hero("Bay Huy", 8, -31, 2.6)
        enemy = Hero("Jenata Myj", 4, 44, 12)
        with self.assertRaises(Exception) as context:
            bay_huy.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_fight_meth__if_enemy_health_is_zero_or_below__expect_exception(self):
        bay_huy = Hero("Bay Huy", 8, 99.99, 2.6)
        enemy = Hero("Jenata Myj", 4, 0, 12)
        with self.assertRaises(Exception) as context:
            bay_huy.battle(enemy)
        self.assertEqual("You cannot fight Jenata Myj. He needs to rest", str(context.exception))

        bay_huy = Hero("Bay Huy", 8, 99.99, 2.6)
        enemy = Hero("Jenata Myj", 4, -22, 12)
        with self.assertRaises(Exception) as context:
            bay_huy.battle(enemy)
        self.assertEqual("You cannot fight Jenata Myj. He needs to rest", str(context.exception))

    def test_fight_meth__if_both_can_fight_end_with_zero_health__expect_zero_health_and_draw(self):
        bay_huy = Hero("Bay Huy", 2, 22, 8)
        enemy = Hero("Jenata Myj", 2, 16, 11)
        func_result = bay_huy.battle(enemy)
        expected_health_bh, expected_health_enemy = 0, 0
        actual_health_bh, actual_health_enemy = bay_huy.health, enemy.health
        self.assertEqual("Draw", func_result)
        self.assertEqual(expected_health_bh, actual_health_bh)
        self.assertEqual(expected_health_enemy, actual_health_enemy)

    def test_fight_meth__if_both_can_fight_end_with_negative_health__expect_negative_health_and_draw(self):
        bay_huy = Hero("Bay Huy", 2, 11, 8)
        enemy = Hero("Jenata Myj", 2, 8, 11)
        func_result = bay_huy.battle(enemy)
        expected_health_bh, expected_health_enemy = -11, -8
        actual_health_bh, actual_health_enemy = bay_huy.health, enemy.health
        self.assertEqual("Draw", func_result)
        self.assertEqual(expected_health_bh, actual_health_bh)
        self.assertEqual(expected_health_enemy, actual_health_enemy)

    def test_fight_meth__if_both_can_fight_end_with_win__expect_higher_values_and_win(self):
        bay_huy = Hero("Bay Huy", 20, 100, 50)
        enemy = Hero("Jenata Myj", 2, 10, 5)
        func_result = bay_huy.battle(enemy)
        expected_health_bh, expected_health_enemy = 90 + 5, -990
        actual_health_bh, actual_health_enemy = bay_huy.health, enemy.health
        self.assertEqual("You win", func_result)
        self.assertEqual(expected_health_bh, actual_health_bh)
        self.assertEqual(expected_health_enemy, actual_health_enemy)
        self.assertEqual(21, bay_huy.level)
        self.assertEqual(55, bay_huy.damage)

    def test_fight_meth__if_both_can_fight_end_with_loss__expect_higher_values_and_loss(self):
        bay_huy = Hero("Bay Huy", 2, 10, 5)
        enemy = Hero("Jenata Myj", 20, 100, 50)
        func_result = bay_huy.battle(enemy)
        expected_health_bh, expected_health_enemy = -990, 90 + 5
        actual_health_bh, actual_health_enemy = bay_huy.health, enemy.health
        self.assertEqual("You lose", func_result)
        self.assertEqual(expected_health_bh, actual_health_bh)
        self.assertEqual(expected_health_enemy, actual_health_enemy)
        self.assertEqual(21, enemy.level)
        self.assertEqual(55, enemy.damage)

    def test_str_method(self):
        bay_huy = Hero("Bay Huy", 2, 10, 5)
        enemy = Hero("Jenata Myj", 20, 100, 50)
        expected = f"Hero Bay Huy: 2 lvl\n" \
                   f"Health: 10\n" \
                   f"Damage: 5\n"
        actual = str(bay_huy)
        self.assertEqual(expected, actual)

    if __name__ == "__main__":
        unittest.main()
