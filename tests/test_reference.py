import unittest
from controller.reference import Mode, PortInput, distribute, schedule_fraction

class ControllerTests(unittest.TestCase):
    def test_schedule(self):
        self.assertEqual([schedule_fraction(t) for t in (-1, 0, 1.9, 2, 9.9, 10)],
                         [0, 1, 1, 0.5, 0.5, 0])

    def test_manual_independent(self):
        a, b = distribute(True, 11, (
            PortInput(Mode.MANUAL, True), PortInput(Mode.MANUAL, False)), 30)
        self.assertTrue(a.enabled)
        self.assertFalse(b.enabled)

    def test_auto_override(self):
        a, b = distribute(True, 11, (
            PortInput(Mode.AUTO, True, True),
            PortInput(Mode.AUTO, False)), 30)
        self.assertTrue(a.enabled)
        self.assertFalse(b.enabled)

    def test_equal_sharing(self):
        a, b = distribute(True, 0, (
            PortInput(Mode.AUTO, False), PortInput(Mode.AUTO, False)), 20)
        self.assertAlmostEqual(a.allocated_watts, 10)
        self.assertAlmostEqual(b.allocated_watts, 10)
        self.assertEqual(a.fault, "E14")

    def test_port_short_isolation(self):
        a, b = distribute(True, 0, (
            PortInput(Mode.AUTO, False, shorted=True),
            PortInput(Mode.AUTO, False)), 30)
        self.assertEqual(a.fault, "E14")
        self.assertFalse(a.enabled)
        self.assertTrue(b.enabled)

    def test_master_off(self):
        a, b = distribute(False, 0, (
            PortInput(Mode.MANUAL, True), PortInput(Mode.MANUAL, True)), 30)
        self.assertFalse(a.enabled)
        self.assertFalse(b.enabled)

    def test_low_battery(self):
        a, b = distribute(True, 0, (
            PortInput(Mode.MANUAL, True), PortInput(Mode.MANUAL, True)),
            30, battery_safe=False)
        self.assertFalse(a.enabled)
        self.assertFalse(b.enabled)

    def test_port_symmetry(self):
        x = PortInput(Mode.MANUAL, True)
        y = PortInput(Mode.MANUAL, False)
        left = distribute(True, 5, (x, y), 30)
        right = distribute(True, 5, (y, x), 30)
        self.assertEqual(left, right[::-1])

if __name__ == "__main__":
    unittest.main()
